import numpy
import pygame
import json
from src.tools.control_handler import check_dynamic_user_input
from src.base_classes.projectile import Projectile

# import pprint

controls_file = open("src/JSON_Files/players.json")
all_controls = json.load(controls_file)

weapons_file = open("src/JSON_Files/weapons.json")
all_weapons = json.load(weapons_file)

player_count = 0

class player(pygame.sprite.Sprite):
    MOVEMENT_SPEED = all_controls["Movement_Speed"]

    projectile_group = pygame.sprite.Group()

    def __init__(self,):
        super().__init__()
        global player_count
        global all_controls
        self.player_number = player_count + 1
        self.controls = all_controls["Player_"  + str(self.player_number)]
        self.image = pygame.image.load(all_controls["Player_"  + str(self.player_number)]["Sprite"])
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.position = [0,0]
        self.velocity = [0,0]
        self.current_weapon = "Default"
        self.current_weapon_sprite = pygame.image.load(all_weapons[self.current_weapon]["Sprite"])
        player_count = self.player_number

    def update_position(self, event):
        check_dynamic_user_input(self, event)
        # self.rect.center = self.position

    def update(self, *args, **kwargs):
        self.position = numpy.array(self.position) + numpy.array(self.velocity)
        self.rect.center = self.position
        self.projectile_group.draw(pygame.display.get_surface())
        self.projectile_group.update()


    def fire_selected_weapon(self):
        projectile = Projectile(self.current_weapon_sprite, self.current_weapon, self.position)
        self.projectile_group.add(projectile)
