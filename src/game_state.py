import random

from src.BaseClasses.player import *

from src.BaseClasses.enemy import classicAlien
from src.Tools.time_handler import Timer
from src.BaseClasses.menu import *
from src.Tools.EnemyScripts.parse_engine.tools import parse_engine

screen = pygame.display.get_surface()
menu = Menu(screen)

def initialize_game():
    global screen, menu
    screen = pygame.display.get_surface()
    menu = Menu(screen)
    one_player_button = player_mode_choice(20, 70,
                                           "One Player", screen=screen)
    two_player_button = player_mode_choice(70, 70,
                                           "Two Players", screen=screen)

    while True:
        events = pygame.event.get()
        menu.update(events)

        if one_player_button.bool_val(events):
            initialize_sprites(1)
            break
        elif two_player_button.bool_val(events):
            initialize_sprites(2)
            break
        menu.draw()
        one_player_button.draw()
        two_player_button.draw()
        pygame.display.flip()
        Timer.update()