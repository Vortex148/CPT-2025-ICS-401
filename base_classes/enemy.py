import pygame
import json

pygame.init()

queue_file = open("base_classes/enemy_queue.json")
queue = json.load(queue_file)

enemy_count = 0
class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, image, size=(30,30)):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=position)
        self.active = False # Ensuring the enemies aren't drawn until it is necessary to load them
        # This is further managed using a queue in the attached json file.

    def activate(self):
        self.active = True

    def update(self):
        if self.active:
            pass # code for enemy animation goes here

class classicAlien(Enemy):
    def __init__(self, position):
        super().__init__(position, "images/Sprites/classicAlien.png")

class batBoss(Enemy):
    def __init__(self, position):
        super().__init__(position, "images/Sprites/batBass.png", size = (50, 50))

class beeEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "images/Sprites/beeEnemy.png")

class butterflyEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "images/Sprites/butterflyEnemy.png")

class flyEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "images/Sprites/flyEnemy.png")

class greenBoss(Enemy):
    def __init__(self, position):
        super().__init__(position, "images/Sprites/greenBoss.png", size = (50, 50))

class orangeAlien(Enemy):
    def __init__(self, position):
        super().__init__(position, "images/Sprites/orangeAlien.png")

class purpleShip_Alien(Enemy):
    def __init__(self, position):
        super().__init__(position, "images/Sprites/purple_shipAlien.png", size = (50, 50))

class redAlien(Enemy):
    def __init__(self, position):
        super().__init__(position, "images/Sprites/redAlien.png")

class spider(Enemy):
    def __init__(self, position):
        super().__init__(position, "images/Sprites/spider.png")









