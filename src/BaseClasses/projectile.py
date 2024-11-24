import pygame
import json
import numpy

weapons_file = open("src/JSON_Files/weapons.json")
all_weapons = json.load(weapons_file)

class Projectile(pygame.sprite.Sprite):
    FADE_OUT_SPEED = 10
    def __init__(self, sprite, weapon, starting_position):
        super().__init__()
        self.image = sprite
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.position = starting_position.copy()
        self.rect.center = self.position
        self.velocity = numpy.multiply(all_weapons[weapon]["Velocity"].copy(), [1,-1])
        self.opacity = 255


    def __del__(self):

        self.kill()

    def update(self, *args, **kwargs):
        if self.rect.top < 0:
            self.fade_out()

        else:
            self.position = numpy.array(self.velocity) + numpy.array(self.position)
            self.rect.center = self.position



    def fade_out(self):
        self.opacity -= self.FADE_OUT_SPEED

        if self.opacity < 0:
            self.__del__()

        self.image.set_alpha(self.opacity)



