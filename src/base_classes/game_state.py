import pygame
from src.base_classes.button_classes import basic_button
from src.common_variables import *
from src.base_classes.player import player

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
        self.one_player_button = basic_button(screen_width / 2 - 150, screen_height - 90,
                                               "One Player", lambda: self.initialize_sprites(1), screen)

        self.two_player_button = basic_button(screen_width / 2 + 150, screen_height - 90,
                                               "Two Players", lambda: self.initialize_sprites(2), screen)

        self.start_game_button = basic_button(screen_width/2, screen_height/2,
                            "Start Next Level", lambda: self.start_level(),
                                              self.screen)

    # When the first line of the enemy script is read, the state variable must be changed in level is running
    def start_level(self, level_number):
        if self.level_number == 1:
            pass
        elif self.level_number == 2:
            pass
        elif self.level_number == 3:
            pass

    def update(self, events):
        if self.one_player_button.visible:
            self.one_player_button.update(events)

        if self.two_player_button.visible:
            self.two_player_button.update(events)

    def re_initalize_json_to_default(self):
        pass


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Creating the screen and setting a caption
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game = Game(screen)