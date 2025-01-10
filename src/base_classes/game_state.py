import pygame
from src.base_classes.button_classes import basic_button
from src.base_classes.revised_buttons import BASIC_BUTTON
from src.common_variables import *
from src.base_classes.player import player
from src.Tools.global_tools import get_path

size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

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

    # Creating the players. Executed by the player-mode choice buttons when they are clicked
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

    # Creating the player mode choice and begin/next level buttons
    # They all inherit from the basic button class, giving them the same structure.
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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Creating the screen and setting a caption
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game = Game(screen)