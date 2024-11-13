import numpy
import pygame
import json
from src.tools.control_handler import check_dynamic_user_input

# import pprint

controls_file = open("src/JSON_Files/players.json")
all_controls = json.load(controls_file)

player_count = 0

class player(pygame.sprite.Sprite):
    MOVEMENT_SPEED = all_controls["Movement_Speed"]

    position = (0,0)
    velocity = (0,0)
    controls = None
    player_number = None
    image = None
    rect = None

    def __init__(self,):
        super().__init__()
        global player_count
        global all_controls
        self.player_number = player_count + 1
        self.controls = all_controls["Player_"  + str(self.player_number)]
        self.image = pygame.image.load(all_controls["Player_"  + str(self.player_number)]["Sprite"])
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        player_count = self.player_number

    def update_position(self, event):
        check_dynamic_user_input(self, event)
        self.rect.center = self.position

    def update(self, *args, **kwargs):

        self.position = numpy.add(self.position, self.velocity)
