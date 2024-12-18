import pygame
from src.common_variables import *
from src.base_classes.player import player
from src.base_classes.menu import player_mode_choice

size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

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
        self.player_button_clicked_state = False
        self.level_is_running = False

    def update_player_sprite_group(self, new_group=None):
        if new_group:
            game.player_sprite_group.empty()
            for sprite in new_group:
                self.player_sprite_group.add(sprite)
        else:
            print("No changes made to player sprite group")
        return self.player_sprite_group

    # def draw_player_sprite_group(self):
    #     # MAYBE INCLUDE self.update_player_sprite_group()
    #     self.player_sprite_group = self.update_player_sprite_group()
    #     self.player_sprite_group.draw(self.screen)

    def close_player_buttons(self):
        if self.one_player_button:
            self.one_player_button.visible = False
            self.player_button_clicked_state = True

        if self.two_player_button:
            self.two_player_button.visible = False
            self.player_button_clicked_state = True

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

    def create_buttons(self):
        self.one_player_button = player_mode_choice(screen_width / 2 - 150, screen_height - 90,
                                               "One Player", lambda: self.initialize_sprites(1), screen)

        self.two_player_button = player_mode_choice(screen_width / 2 + 150, screen_height - 90,
                                               "Two Players", lambda: self.initialize_sprites(2), screen)

    # When the first line of the enemy script is read, the state variable must be changed in level is running

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