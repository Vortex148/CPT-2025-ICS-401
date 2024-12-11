import pygame

from src.Tools.unit_handler import swth_sprite
from src.Tools.trajectory_handler import trajectory_handler

enemy_count = 0

class Enemy(swth_sprite):
    def __init__(self, image, size=(30,30)):
        global enemy_count
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        super().__init__(self.image)
        # Initializes the current_trajectory generation. Can be changed in future
        self.traj_handle = trajectory_handler(30, 10000, [0, 0], super().get_rect(), self)
        self.active = True # Ensuring the enemies aren't drawn until it is necessary to load them
        # This is further managed using a queue in the attached json file.
        enemy_count += 1
        self.id = enemy_count

    def activate(self):
        self.active = True

    def kill(self):
        self.active = False
        super().kill()

    def draw(self):
        pygame.display.get_surface().blit(self.image, self.rect)

    # Gets rect from the swth_sprite super class
    def get_rect(self):
        return super().get_rect()

    # Follows current_trajectory. Note: Must run each frame until completion as it runs linearly, not in parallel (Not multithreaded)
    def follow_trajectory(self, trajectory):
        position = self.traj_handle.follow_trajectory(trajectory, super().get_position())
        self.update_position(position)

    def update_trajectory_generator(self, speed = 0, acceleration = 0):
        # Checks that speed and acceleration values are valid, and updates accordingly
        if speed > 0:
            self.traj_handle.update_max_speed(speed)

        if acceleration > 0:
            self.traj_handle.update_acceleration(acceleration)

    def update_position(self, position):
        super().update_position(position)

    def check_collision(self, rect):
        return self.rect.colliderect(rect)

def generate_enemy(type):
    match(type):
        case "alien":
            return classicAlien()
        case "batboss":
            return batBoss()
        case "bee":
            return beeEnemy()
        case "alien":
            return classicAlien()
        case "alien":
            return classicAlien()
        case "alien":
            return classicAlien()
        case "alien":
            return classicAlien()
        case "alien":
            return classicAlien()
        case _:
            return classicAlien()

class classicAlien(Enemy):
    def __init__(self):
        super().__init__("Images/Sprites/Enemies/classicAlien.png")

class batBoss(Enemy):
    def __init__(self):
        super().__init__("Images/Sprites/Enemies/batBass.png", size = (50, 50))

class beeEnemy(Enemy):
    def __init__(self, ):
        super().__init__("Images/Sprites/Enemies/beeEnemy.png")

class butterflyEnemy(Enemy):
    def __init__(self):
        super().__init__("Images/Sprites/Enemies/butterflyEnemy.png")

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









