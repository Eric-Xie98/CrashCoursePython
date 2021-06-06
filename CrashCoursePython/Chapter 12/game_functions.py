import sys
import pygame

def check_keydown_events(event, ship):

    """Respond to keys being pressed down"""

    if event.key == pygame.K_RIGHT:
        # Set moving_right flag to True so update() triggers
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Set moving_left flag to True
        ship.moving_left = True


def check_keyup_events(event, ship):

    """Respond to keys releases"""

    if event.key == pygame.K_RIGHT:
        # Set moving_right flag to False so update() stops triggering
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Set moving_left flag to False
        ship.moving_left = False


def check_event(ship):
    
    """Respond to key events and user input"""

    for event in pygame.event.get():                    # This for loop is an event loop

        if event.type == pygame.QUIT:

            sys.exit()

        elif event.type == pygame.KEYDOWN:
            
            check_keydown_events(event, ship)
        
        elif event.type == pygame.KEYUP:

            check_keyup_events(event, ship)
        
def update_screen(ai_settings, screen, ship):

    """Update the game elements on the screen"""

    # Redraw the screen and the ship
        
    screen.fill(ai_settings.bg_color)
    ship.blitme()
        
    # Make the most recent screen display
        
    pygame.display.flip()                               # Will constantly update the screen elements because of while loop until pygame.QUIT