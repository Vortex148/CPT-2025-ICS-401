import numpy
import pygame
import json

from src.Tools.control_handler import check_dynamic_user_input
from src.BaseClasses.projectile import Projectile
from src.Tools.unit_handler import swth_sprite
from src.Tools.time_handler import Timer

# import pprint

controls_file = open("src/JSON_Files/players.json")
all_controls = json.load(controls_file)

weapons_file = open("src/JSON_Files/weapons.json")
all_weapons = json.load(weapons_file)

player_count = 0

player_sprite_group = pygame.sprite.Group()


class player(swth_sprite):
    MOVEMENT_SPEED = all_controls["Movement_Speed"]

    projectile_group = pygame.sprite.Group()

    def __init__(self,):

        global player_count
        global all_controls
        self.player_number = player_count + 1
        self.controls = all_controls["Player_"  + str(self.player_number)]
        self.image = pygame.image.load(all_controls["Player_"  + str(self.player_number)]["Sprite"])
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        super().__init__(self.image)
        self.position = [0,0]
        self.velocity = [0,0]
        self.current_weapon = "Default"
        self.current_weapon_sprite = pygame.image.load(all_weapons[self.current_weapon]["Sprite"]).convert_alpha()
        player_count = self.player_number

    def update_position(self, event):
        check_dynamic_user_input(self, event)
        # self.rect.center = self.position

    def update(self, *args, **kwargs):
        # Units are in screen % / sec
        self.position = numpy.array(self.position) + numpy.array(self.velocity) * Timer.get_last_frame_time_s()
        super().update_position(self.position)
        super().update()
        self.projectile_group.update()
        self.projectile_group.draw(pygame.display.get_surface())




    def fire_selected_weapon(self):
        projectile = Projectile(self.current_weapon_sprite, self.current_weapon, self.position + [0,-7])
        self.projectile_group.add(projectile)


def initialize_sprites(value):
    global player_sprite_group
    player_sprite_group.empty()
    if value == 1:
        player1 = player()
        player_sprite_group.add(player1)
    if value == 2:
        player1 = player()
        player2 = player()
        player_sprite_group.add(player1, player2)
