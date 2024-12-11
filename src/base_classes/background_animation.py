import pygame
import random
from src.common_variables import *

star_group = pygame.sprite.Group()

class star(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = self.height = 15
        self.animation_speed = random.randint(1, 3)

        if self.animation_speed == 1:
            self.width = self.height = 10

        self.image = pygame.image.load("images/Sprites/background_star.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update_position(self):
        self.y += self.animation_speed * 0.8
        self.rect.center = (self.x, self.y)
        if self.y > screen_height + 50:
            self.y = random.randrange (-50, -10)
            self.x = random.randrange(-30, 1000)
        self.rect.center = (self.x, self.y)

    def update(self):
        self.update_position()

def create_stars():
    for i in range(50):
        x_pos = random.randrange(-30, screen_width + 30 )
        y_pos = random.randrange(-30, screen_height + 30)
        Star = star(x_pos, y_pos)
        star_group.add(Star)

create_stars()
