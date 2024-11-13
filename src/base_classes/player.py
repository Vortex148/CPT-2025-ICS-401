import pygame
import json
import src.tools.control_handler
from src.tools.control_handler import check_dynamic_user_input

# import pprint

controls_file = open("base_classes/players.json")
all_controls = json.load(controls_file)

player_count = 0

class player(pygame.sprite.Sprite):
    MOVEMENT_SPEED = all_controls["Movement_Speed"]
    position = (0,0)
    controls = None
    player_number = None

    def __init__(self,):
        super().__init__()
        global player_count
        global all_controls
        self.player_number = player_count + 1
        self.controls = all_controls["Player_"  + str(self.player_number)]
        self.sprite = pygame.image.load()
        player_count = self.player_number

    def update_position(self):
        check_dynamic_user_input(self)


