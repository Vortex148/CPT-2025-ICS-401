import pygame
import json
import numpy

# Opening the json weapons file.
weapons_file = open("src/JSON_Files/weapons.json")
all_weapons = json.load(weapons_file)


class Projectile(pygame.sprite.Sprite):
    FADE_OUT_SPEED = 10

    def __init__(self, sprite, weapon, starting_position):
        super().__init__() # Allowing access to the
        self.image = sprite
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.position = starting_position.copy() # Copying the starting position of the
        self.rect.center = self.position
        self.velocity = numpy.multiply(all_weapons[weapon]["Velocity"].copy(), [1,-1])
        self.opacity = 255


    def __del__(self):

        self.kill()

    def update(self, *args, **kwargs):
        # If the top of the projectile is at the edge of the screen, begin fadeout.
        if self.rect.top < 0:
            self.fade_out()

        else:
            # Animating the projectile to move by its velocity from its starting position each frame.
            self.position = numpy.array(self.velocity) + numpy.array(self.position)
            self.rect.center = self.position


    # Decreasing the opacity of the sprite gradually when it hits the top of the screen
    def fade_out(self):
        self.opacity -= self.FADE_OUT_SPEED

        # Deleting the sprite when it is completely transparent.
        if self.opacity < 0:
            self.__del__()

        self.image.set_alpha(self.opacity)



