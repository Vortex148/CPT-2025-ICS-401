import pygame
import json
# import pprint

controls_file = open("base_classes/control_schemes.json")
all_controls = json.load(controls_file)

player_count = 0

class player(pygame.sprite.Sprite):
    position = (0,0)
    controls = None
    player_number = None

    def __init__(self,):
        super().__init__()
        global player_count
        global all_controls
        self.player_number = player_count + 1
        self.controls = all_controls["Player_"  + str(self.player_number)]
        player_count = self.player_number

    def update_position(self):
        pass
