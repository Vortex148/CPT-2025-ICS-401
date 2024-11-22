import pygame

from src.tools.time_handler import Timer
from src.tools.unit_handler import swth_sprite
from src.tools.trajectory_handler import trajectory_handler


# queue_file = open("src/JSON_Files/enemy_queue.json")
# queue = json.load(queue_file)
# queue = json.load(queue_file)

enemy_count = 0

class Enemy(swth_sprite):
    def __init__(self, image, size=(30,30)):
        global enemy_count
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        super().__init__(self.image)
        self.traj_handle = trajectory_handler(30, 0, 180, [0, 0], super().get_rect(), self)
        self.active = False # Ensuring the enemies aren't drawn until it is necessary to load them
        # This is further managed using a queue in the attached json file.
        enemy_count += 1
        self.id = enemy_count
    def activate(self):
        self.active = True

    # def update(self):
    #     if self.active:
    #         pass # code for enemy animation goes here

    def follow_trajectory(self, trajectory):
        super().update_position(self.traj_handle.follow_trajectory(trajectory, super().get_position()))



class classicAlien(Enemy):
    def __init__(self):
        super().__init__("Images/Sprites/Enemies/classicAlien.png")

class batBoss(Enemy):
    def __init__(self):
        super().__init__("Images/Sprites/Enemies/batBass.png", size = (50, 50))

class beeEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/Enemies/beeEnemy.png")

class butterflyEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/Enemies/butterflyEnemy.png")

class flyEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/Enemies/flyEnemy.png")

class greenBoss(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/Enemies/greenBoss.png", size = (50, 50))

class orangeAlien(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/Enemies/orangeAlien.png")

class purpleShip_Alien(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/Enemies/purple_shipAlien.png", size = (50, 50))

class redAlien(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/Enemies/redAlien.png")

class spider(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/Enemies/spider.png")









