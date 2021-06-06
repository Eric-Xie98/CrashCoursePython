## Character image we're putting in

import pygame

class Character():

    """Class for attributes and behavior of character"""
    
    def __init__(self, screen):
        
        """Initializing attributes/behaviors"""

        self.screen = screen

        self.image = pygame.image.load('images/chimpship.png')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = self.screen_rect.center
    

    def blitme(self):

        """Draw myself on the screen"""

        self.screen.blit(self.image, self.rect)

    
    