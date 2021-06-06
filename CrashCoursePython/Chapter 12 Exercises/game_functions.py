import sys
import pygame

def check_event():

    """Checks if end event is triggered whenever user input is detected"""

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()


def draw_screen(ai_settings, screen, character):

    """Draws the screen elements"""

    screen.fill(ai_settings.bg_color)
    character.blitme()

    pygame.display.flip()


def decide_color(ai_settings):

    user_color = input("What color do you want the background to be? ")
    ai_settings.bg_color = user_color
