import pygame
from src.common_variables import *
from src.base_classes.player import player
from src.base_classes.menu import player_mode_choice

size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_sprite_group = pygame.sprite.Group
        self.player_count = 0
        self.player1 = None
        self.player2 = None

    one_player_button = player_mode_choice(screen_width / 2 - 150, screen_height - 90,
                                           "One Player", lambda: initialize_sprites(1), screen)

    two_player_button = player_mode_choice(screen_width / 2 + 150, screen_height - 90,
                                           "Two Players", lambda: initialize_sprites(2), screen)

    # Once either button has been clicked, both disappear.
    if one_player_button:
       one_player_button.visible = False
    if two_player_button:
        two_player_button.visible = False

    def initialize_sprites(value):
        global player_sprite_group, one_player_button, two_player_button, player_count, player1, player2
        player_sprite_group.empty()
        if value == 1:
            player1 = player()
            player_sprite_group.add(player1)
            player_count = 1
        if value == 2:
            player1 = player()
            player2 = player()
            player_sprite_group.add(player1, player2)
            player_count = 2

    def update_player_info(self, item_type)
        if item_type.lower() == "blaster":
            attributes = ["current_weapon"]
        elif item_type.lower() == "ship":
            attributes = ["health", "velocity"]
        elif item_type.lower() == "upgrade":
            attributes = ["increase_damage", "increase_health", "decrease_cooldown"]

        if self.player_count == 1:
            for attribute in attributes:
                self.player1.attribute = value
        elif self.player_count == 2:
            for sprite in self.player_sprite_group:
                for attribute in attributes:
                    self.sprite.attribute = value