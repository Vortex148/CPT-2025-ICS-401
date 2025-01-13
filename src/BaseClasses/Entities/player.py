import numpy
import pygame
import json

from src.Tools.Misc_Tools.control_handler import check_dynamic_user_input
from src.BaseClasses.Entities.projectile import Projectile
from src.Tools.Misc_Tools.unit_handler import swth_sprite
from src.Tools.Misc_Tools.time_handler import Timer



player_data = json.load(open("src/JSON_Files/players.json"))

ship_data = json.load(open("src/JSON_Files/ships.json"))
weapon_data = json.load(open("src/JSON_Files/weapons.json"))

player_count = 0

player_sprite_group = pygame.sprite.Group()


class player(swth_sprite):
    MOVEMENT_SPEED = [50, 50]

    projectile_group = pygame.sprite.Group()

    def __init__(self, starting_position = [50,70]):

        global player_count
        global player_data
        self.player_number = player_count + 1
        self.controls = player_data["Player_"  + str(self.player_number)]["Controls"]
        self.current_ship = player_data["Player_" + str(self.player_number)]["current_ship"]
        self.image = pygame.image.load(self.get_ship_path())
        self.rect = self.image.get_rect()
        super().__init__(self.image, size=[5,6])
        self.position = starting_position
        self.velocity = [0,0]
        self.health = ship_data[self.current_ship]["Health"]
        self.max_health = ship_data[self.current_ship]["Health"]
        self.current_weapon = "Default"
        self.current_weapon_sprite = pygame.image.load(weapon_data[self.current_weapon]["Sprite"]).convert_alpha()
        player_count = self.player_number
        self.alive = True


    def set_alive(self, state):
        self.alive = state
        super().set_visible(state)

    def set_ship(self, ship_name):
        file = open("src/JSON_Files/players.json", "w")
        player_data["Player_" + str(self.player_number)]["current_ship"] = ship_name
        json.dump(player_data, file)

        self.current_ship = ship_name
        self.image = pygame.image.load(self.get_ship_path())
        self.health = ship_data[self.current_ship]["Health"]
        self.max_health = ship_data[self.current_ship]["Health"]

        super().set_image(self.image)

    def set_weapon(self, weapon_name):
        self.current_weapon = weapon_name
        self.current_weapon_sprite = pygame.image.load(weapon_data[self.current_weapon]["Sprite"]).convert_alpha()


    def get_ship_path(self):
        return ship_data[self.current_ship]["Sprite_P" + str(self.player_number)]

    def get_weapon_path(self):
        return weapon_data[self.current_weapon]["Sprite"]


    def update(self, *args, **kwargs):
        # Units are in screen % / sec
        if self.alive:
            self.position = numpy.array(self.position) + numpy.array(self.velocity) * Timer.get_last_frame_time_s()
            if self.position[0] > 100 - self.size[0] / 2:
                self.position[0] = 100 - self.size[0] / 2
            elif self.position[0] < self.size[0] / 2:
                self.position[0] = self.size[0] / 2

            if self.position[1] > 100 - self.size[1] / 2:
                self.position[1] = 100 - self.size[1] / 2
            elif self.position[1] < self.size[1] / 2:
                self.position[1] = self.size[1] / 2

            self.projectile_group.update()
            self.projectile_group.draw(pygame.display.get_surface())
            super().update_position(self.position)
            super().update()
            super().draw()
        # print(self.health)

    def update_position(self, event):
        check_dynamic_user_input(self, event)
        # self.rect.center = self.position

    def reset(self):
        self.health = ship_data[self.current_ship]["Health"]

    def fire_selected_weapon(self):
        offset = [self.position[0], self.position[1] - self.size[1] / 2]
        projectile = Projectile(self.current_weapon_sprite, self.current_weapon, offset)
        self.projectile_group.add(projectile)

    def check_collision(self, projectile : Projectile, ):
        if self.rect.colliderect(projectile.rect):
            self.health -= projectile.damage
            projectile.kill()
            if self.health <= 0:
                return True
        return False

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
