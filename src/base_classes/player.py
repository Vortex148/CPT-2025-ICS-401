import numpy
import pygame
import json
from src.Tools.control_handler import check_dynamic_user_input
from src.base_classes.projectile import Projectile
from src.common_variables import SCREEN_WIDTH


class player(pygame.sprite.Sprite):
    player_count = 0 # Determines which controls are assigned

    def __init__(self, weapon="Default"):
        super().__init__() # For grouping

        # Initializing json modules in the constructor ensures the most recent
        # values can be accessed when the players are recreated after a purchase
        self.controls_file = open("src/JSON_Files/players.json")
        self.all_controls = json.load(self.controls_file)
        self.MOVEMENT_SPEED = self.all_controls["Movement_Speed"]
        self.weapons_file = open("src/JSON_Files/weapons.json")
        self.all_weapons = json.load(self.weapons_file)
        self.SPRITE = self.all_controls["Sprite"]

        self.projectile_group = pygame.sprite.Group()

        player.player_count += 1
        if player.player_count > 2:
            player.player_count = 0
            player.player_count += 1

        self.controls = self.all_controls["Player_"  + str(player.player_count)] # Assigning the player controls

        # Loading players and sizing them.
        self.sprite_width = 100
        self.sprite_height = 100
        self.image = pygame.image.load(self.SPRITE)
        self.image = pygame.transform.scale(self.image, (self.sprite_width, self.sprite_height))
        self.rect = self.image.get_rect()
        self.player_number = player.player_count
        self.position = [350 + 100 * self.player_number, 500]
        self.velocity = [0,0]
        self.health = 100
        self.current_weapon = weapon
        self.current_weapon_sprite = pygame.image.load(self.all_weapons[self.current_weapon]["Sprite"])
        self.coin_balance = 10000

    def update_position(self, event):
        check_dynamic_user_input(self, event)

    def update(self, *args, **kwargs):
        # Ensuring that position and fired projectiles are updated each frame
        last_position = self.position.copy()
        self.position = numpy.array(self.position) + numpy.array(self.velocity)

        # Ensuring the players can't move off-screen
        if self.position[0] > SCREEN_WIDTH - (self.sprite_width/2) or self.position[0] < 0 + (self.sprite_width/2):
            self.position[0] = last_position[0]

        self.rect.center = self.position
        self.projectile_group.draw(pygame.display.get_surface())
        self.projectile_group.update()

    # Fires the projectile of the weapon the player is currently using
    def fire_selected_weapon(self):
        projectile = Projectile(self.current_weapon_sprite, self.current_weapon, self.position)
        self.projectile_group.add(projectile)