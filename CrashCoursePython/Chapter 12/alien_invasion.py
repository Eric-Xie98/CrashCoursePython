## Creating a Pygame Window and responding to User Input

# First, we'll create a game window. Here's the basic structure of a game written in Pygame:

import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf                                                                         # We're doing this probably because we're going to add more to game_functions

def run_game():

    """Runs the game and creates a screen object"""

    # Initializes Pygame background settings
   
    pygame.init()                           
    ai_settings = Settings()                                    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))         # This sets the display's size with a tuple of (1200, 800) width by height
    pygame.display.set_caption("im shidding and pissing all over the floor")                        # Screen object is a surface in Pygame, where game elements are displayed

    # Make a ship
    ship = Ship(ai_settings, screen)


    # Starts the main loop for the game

    while True:                                       

        gf.check_event(ship)                                                                        # Watch for keyboard and mouse events
        ship.update()                                                                               # Update ship position based on event triggers
        gf.update_screen(ai_settings, screen, ship)                                                 # Update the screen elements each iteration of the loop



run_game()

# This for loop is an event loop, it listens for and detects events caused by mouse/keyboard inputs
# and acts accordingly based on the code; in this case, any mouse or keyboard movement will cause the for
# loop to run and if the game window close button is clicked, pygame.QUIT event is detected


# Now that we have the settings page completed, we'll be adding a ship image. You can use almost any type of image
# in your game, but .bmp or bitmap is the easiest because Python loads them by default

# After choosing an image for the ship, a monkey in this case, we'll create a module class for it that 
# will control its behavior and attributes. Next, we'll add a ship image into the game.

# We imported Ship, created a Ship instance with the argument of our screen, and blitme every 
# runthrough of the while loop.


## We've centered the image to a scale on the game screen, but now we need to refactor the game code.
## The game_functions module will clear up space in the alien_invasion.py logic to make it easier to follow.

    ## let's start with a check_events() function that can simplify checking whether the event is a quit
    ## let's also add a refresh screen option in game_functions called update_screen

## Now we add response to key inputs, and we'll be able to move the ship around. We first added the K_RIGHT event check
## and increment the ship.rect.centerx to the right by 1

## What if we want continuous movement?
    
    ## We need to use a movement flag to ensure that whenever the key is pressed down, the flag is true, otherwise it's false
    ## Once we modify the ship and game functions to check for the flag and KEYUP/KEYDOWN, we place the ship.update() right after gf.check_events()

## Let's add movement to the left

    # One thing we need to ensure is that we use two if statements in update() rather than elif, otherwise the right key will
    # hold priority over left key, so if both are held down at the same time, the ship will move right

## We should now have succesfully implemented movement for the ship, so let's dive into more minute details like
## the ship's speed and boundaries off the screen; we'll set a speed factor that'll control how many pixels it moves instead of just 1

    # We limit the ship's boundaries by adding an AND statement that ensures you aren't past the screen.rect

## We're going to now refactor the check_events() funciton in game_functions.py because they are starting to grow larger than necessary