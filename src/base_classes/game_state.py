import pygame
from src.common_variables import *
from src.base_classes.player import player
from src.base_classes.menu import player_mode_choice

size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_sprite_group = pygame.sprite.Group()
        self.player_count = 0
        self.player1 = None
        self.player2 = None
        self.one_player_button = None
        self.two_player_button = None

    def initialize_sprites(self, value):
        self.player_sprite_group.empty()
        if value == 1:
            self.player1 = player()
            self.player_sprite_group.add(self.player1)
            self.player_count = 1
        elif value == 2:
            self.player1 = player()
            self.player2 = player()
            self.player_sprite_group.add(self.player1,self.player2)
            self.player_count = 2

    # Once either button has been clicked, both disappear.
    def create_buttons(self):
        self.one_player_button = player_mode_choice(screen_width / 2 - 150, screen_height - 90,
                                               "One Player", lambda: self.initialize_sprites(1), screen)

        self.two_player_button = player_mode_choice(screen_width / 2 + 150, screen_height - 90,
                                               "Two Players", lambda: self.initialize_sprites(2), screen)
game = Game()