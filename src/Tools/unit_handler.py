from distutils.command.sdist import sdist

import pygame


import numpy
from pygame.display import update


def generate_relative_value_2d(value_2d):
    value_2d = numpy.divide(value_2d, (100, 100))
    value_2d = numpy.multiply(value_2d, pygame.display.get_surface().get_size())
    return value_2d

# SWTH is a custom unit that is measured in as screen_width/100. This enables for various screen sizes to be supported easily
class swth_sprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.super = super()
        self.position = [0,0]
        self.image = image
        self.image = pygame.transform.scale(image, generate_relative_value_2d((5,7)))
        self.rect = self.image.get_rect()


    def generate_relative_coords(self):
        position = numpy.divide(self.position, (100,100))
        position = numpy.multiply(position, pygame.display.get_surface().get_size())
        self.rect.center = position
        return position




    def update_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    # def get_relative_position(self):
    #     return self.generate_relative_coords()

    def get_image(self):
        return self.image

    def get_rect(self):
        return self.rect


    def draw(self):
        screen = pygame.display.get_surface()

        # screen.blit(self.image,(1180,100))
        screen.blit(self.image, self.generate_relative_coords())

    def update(self):

        self.rect.center = self.generate_relative_coords()
