## Blue sky window exercise

import sys
import pygame

from settings import Settings
from character import Character
import game_functions as gp


def run_game():

    """Initialize game settings"""

    pygame.init()
    ai_settings = Settings()
    gp.decide_color(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("You smell like you farded, farded, ab honor role bitch you was retarded")

    character = Character(screen)

    while True:

        gp.check_event()
        gp.draw_screen(ai_settings, screen, character)



run_game()