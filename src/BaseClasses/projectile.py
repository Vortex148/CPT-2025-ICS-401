import pygame
import json
import numpy

import src.Tools.unit_handler

weapons_file = open("src/JSON_Files/weapons.json")
all_weapons = json.load(weapons_file)

class Projectile(src.Tools.unit_handler.swth_sprite):
    FADE_OUT_SPEED = 5
    def __init__(self, sprite, weapon, starting_position):
        self.sprite = pygame.transform.scale(sprite, (1, 1))
        super().__init__(sprite)
        self.rect = self.image.get_rect()
        super().update_position(starting_position)
        self.velocity = numpy.multiply(all_weapons[weapon]["Velocity"].copy(), [1,-1])
        self.opacity = 255


    def __del__(self):
        self.kill()

    def update(self, *args, **kwargs):
        if self.rect.top < 0:
            self.fade_out()

        else:

            super().update_position( numpy.array(self.velocity) + numpy.array(super().get_position()))
            super().update()

    def fade_out(self):
        self.opacity -= self.FADE_OUT_SPEED

        if self.opacity < 0:
            self.__del__()

        super().get_image().set_alpha(self.opacity)



