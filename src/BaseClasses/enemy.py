import pygame.sprite
import json

pygame.init()

queue_file = open("BaseClasses/enemy_queue.json")
queue = json.load(queue_file)

enemy_count = 0
class Enemy(pygame.sprite.Sprite):
    position = (0,0)
    def __init__(self, position, image, health = 10, size=(30,30), score_value = 100):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha() # Loading the image for the sprite and
        # making it memory friendly.
        self.image = pygame.transform.scale(self.image, size) # Sizing the image
        self.health = health
        self.score_value = score_value
        self.rect = self.image.get_rect(center=position) # Positioning it on the screen
        self.active = False # Ensuring the enemies aren't drawn until it is necessary to load them
        # This is further managed using a queue in the attached json file.

    def activate(self):
        self.active = True

    def update(self):
        if self.active:
            pass # code for enemy animation is linked here

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()

class classicAlien(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/classicAlien.png")

class batBoss(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/batBass.png", size = (50, 50))

class beeEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/beeEnemy.png")

class butterflyEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/butterflyEnemy.png")

class flyEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/flyEnemy.png")

class greenBoss(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/greenBoss.png", size = (50, 50))

class orangeAlien(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/orangeAlien.png")

class purpleShip_Alien(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/purple_shipAlien.png", size = (50, 50))

class redAlien(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/redAlien.png")

class spider(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/spider.png")









