import pygame.sprite
import json

pygame.init()

queue_file = open("base_classes/enemy_queue.json")
queue = json.load(queue_file)

enemy_count = 0
class Enemy(pygame.sprite.Sprite):
    position = (0,0)
    # Default parameters are set so that specifying values for common attributes isn't necessary in child classes.
    def __init__(self, position, image, health = 10, size = (30,30), score_value = 100):
        super().__init__()
        self.image = pygame.image.load(image) # Loading the image for the sprite
        self.image = pygame.transform.scale(self.image, size) # Sizing the image

        # Giving it a health value, a score value, and positioning it on the screen
        self.health = health
        self.score_value = score_value
        self.rect = self.image.get_rect(center=position)

        # Ensuring the enemies aren't drawn until it is necessary to load them
        # This is further managed using a queue in the attached json file.
        self.active = False

    def activate(self):
        self.active = True

    def update(self):
        if self.active:
            pass # code for enemy animation is linked here

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()

# Using the basic attributes from the enemy class and applying them to individual
# aliens. Optional parameters are given in needed.
class classicAlien(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/classicAlien.png")

class batBoss(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/batBass.png", size = (50, 50), health = 25)

class beeEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/beeEnemy.png", health = 5)

class butterflyEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/butterflyEnemy.png", health = 7)

class flyEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/flyEnemy.png")

class greenBoss(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/greenBoss.png", size = (50, 50), health = 30)

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









