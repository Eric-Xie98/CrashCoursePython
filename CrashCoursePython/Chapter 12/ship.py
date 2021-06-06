## The module that stores the attributes and behavior of the ship / chimp

import pygame

class Ship():

    def __init__(self, ai_settings, screen):

        """Initialize the ship and set its starting position"""

        self.screen = screen
        self.ai_settings = ai_settings

        # Load the screen and get the ship/image rect:

        self.image = pygame.image.load('images/chimpship.png')          # Pygame loads the image and returns it as a surface to be stored as an attribute
        self.image = pygame.transform.scale(self.image, (100, 100))       # Transforms the image size to a smaller scale
        self.rect = self.image.get_rect()                               # get_rect() access rectangle attributes
        self.screen_rect = screen.get_rect()

        # Start each ship at the bottom of the page centered

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center

        self.center = float(self.rect.centerx)

        # Movement flags

        self.moving_right = False
        self.moving_left = False

    
    def update(self):

        """Update the ship's position based on the movement flag"""

        # Update the ship's center not the rect

        if self.moving_right and self.rect.right < self.screen_rect.right:

            self.center += self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:

            self.center -= self.ai_settings.ship_speed_factor

        # Update the rect object from self.center

        self.rect.centerx = self.center

    
    def blitme(self):
        
        """Draw the ship at its current location"""

        self.screen.blit(self.image, self.rect)


## So what's rect mean? Pygame is efficient because it treats game elemnts like rectangles (rects), which are simple geometric
## shapes. We can work with rects with coordinates x and y along with commands like centerx, center, centery.
## Some other placement commands or left, right, top, bottom, and if you want more horizontal or vertical use x or y

# In Pygame, the coordinate system origin is at the top left, (0,0), and goes positive moving y down and positive moving x right
