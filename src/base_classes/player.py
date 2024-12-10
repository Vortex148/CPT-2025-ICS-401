import numpy
import pygame
import json
from src.tools.control_handler import check_dynamic_user_input
from src.base_classes.projectile import Projectile

# import pprint

# Opening the JSON files storing information about each player and the game's weapons.


# Initializing a player count so that each player can be assigned a value which is
# associated with the index and thus, characteristics of a certain sprite.

class player(pygame.sprite.Sprite):
    player_count = 0
    controls_file = open("src/JSON_Files/players.json")
    all_controls = json.load(controls_file)
    MOVEMENT_SPEED = all_controls["Movement_Speed"]

    def __init__(self,):
        super().__init__()

        weapons_file = open("src/JSON_Files/weapons.json")
        self.all_weapons = json.load(weapons_file)

        self.SPRITE = self.all_controls["Sprite"]

        self.projectile_group = pygame.sprite.Group()

        # Making player count and all-controls accessible to the method.
        player.player_count
        self.player_number = player.player_count + 1
        self.controls = self.all_controls["Player_"  + str(self.player_number)] # Assigning the player controls

        # Loading the image for that player and sizing it.
        self.image = pygame.image.load(self.SPRITE)
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.position = [50,50]
        self.velocity = [0,0]
        self.health = 100
        self.current_weapon = "Default"
        self.current_weapon_sprite = pygame.image.load(self.all_weapons[self.current_weapon]["Sprite"])
        player.player_count = self.player_number

        self.coin_balance = 100000

    def update_position(self, event):
        check_dynamic_user_input(self, event)
        # self.rect.center = self.position

    def update(self, *args, **kwargs):
        self.position = numpy.array(self.position) + numpy.array(self.velocity) # Moving the player by a predetermined amount
        # from its previous position when the appropriate keys are pressed. These keys are specified in the control-handler file
        self.rect.center = self.position
        self.projectile_group.draw(pygame.display.get_surface())
        self.projectile_group.update()

    def fire_selected_weapon(self):
        # Generating the appropriate projectile based on the weapon of the
        # player and starting it at the position of the player.
        projectile = Projectile(self.current_weapon_sprite, self.current_weapon, self.position)
        self.projectile_group.add(projectile)
