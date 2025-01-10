import pygame
from src.base_classes.revised_buttons import BASIC_BUTTON
from src.common_variables import *
from src.base_classes.player import player
from src.Tools.global_tools import get_path
from src.common_variables import screen

# Defining a game class to store all global game values and organize the code.
class Game:

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.player_sprite_group = pygame.sprite.Group()
        self.number_of_players = 0
        self.player1 = None
        self.player2 = None
        self.one_player_button = None
        self.two_player_button = None
        self.next_level_button = None
        self.player_button_clicked_state = False
        self.level_is_running = False

    # Closing the player buttons if they have been clicked
    def close_player_buttons(self):
        if self.one_player_button:
            self.one_player_button.visible = False
            self.player_button_clicked_state = True

        if self.two_player_button:
            self.two_player_button.visible = False
            self.player_button_clicked_state = True

    # Call to create players
    def initialize_sprites(self, value):
        self.player_sprite_group.empty()
        if value == 1:
            self.player1 = player()
            self.player_sprite_group.add(self.player1)
            self.number_of_players = 1
        if value == 2:
            self.player1 = player()
            self.player2 = player()
            self.player_sprite_group.add(self.player1,self.player2)
            self.number_of_players = 2

        self.close_player_buttons()
        self.player_button_clicked_state = True

    # Creating player mode choice buttons
    def create_buttons(self):
        one_player_button_path = get_path("One Player Button", buttons_and_menus_directory, "png")
        two_player_button_path = get_path("Two Players Button", buttons_and_menus_directory, "png")
        self.one_player_button = BASIC_BUTTON(one_player_button_path, (30, 85),
    (20, 13), execute_click=lambda: self.initialize_sprites(1))

        self.two_player_button = BASIC_BUTTON(two_player_button_path, (55, 85),
            (20, 13), execute_click=lambda: self.initialize_sprites(2))

    # Checking for button clicks
    def update(self):
        if self.one_player_button.visible:
            self.one_player_button.check_click()

        if self.two_player_button.visible:
            self.two_player_button.check_click()

game = Game(screen)