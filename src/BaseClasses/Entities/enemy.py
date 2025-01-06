from src.Tools.Misc_Tools.unit_handler import *
from src.Tools.Misc_Tools.trajectory_handler import trajectory_handler
from src.BaseClasses.Entities.projectile import Projectile
import json

enemy_count = 0
enemy_data = json.load(open("src/JSON_Files/enemies.json"))
screen = pygame.display.get_surface()

class Enemy(swth_sprite):
    def __init__(self, data, size=(30,30)):
        global enemy_count
        self.image = pygame.image.load(enemy_data[data]["Image_Path"]).convert_alpha()
        self.health = enemy_data[data]["Health"]
        self.type = data
        super().__init__(self.image, size = size)

        # Initializes the current_trajectory generation. Can be changed in future
        self.traj_handle = trajectory_handler(30, 10000, [0, 0], super().get_rect(), self)
        self.active = True # Ensuring the enemies aren't drawn until it is necessary to load them
        # This is further managed using a quesue in the attached json file.
        enemy_count += 1
        self.id = enemy_count

    def activate(self):
        self.active = True

    def kill(self):
        self.active = False
        super().kill()

    def draw(self):
        pygame.display.get_surface().blit(self.image, self.rect)
        if self.health < enemy_data[self.type]["Health"]:
            self.draw_health_bar()


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

    def check_collision(self, projectile : Projectile, ):
        if self.rect.colliderect(projectile.rect):
            self.health -= projectile.damage
            projectile.kill()
            if self.health <= 0:
                return True
        return False

    def draw_health_bar(self):

        tl_corner_offset = generate_relative_value_2d([super().get_position()[0] - 2, super().get_position()[1] + super().get_size()[1]])
        width_height = generate_relative_value_2d([super().get_size()[0] + 4, 1])

        tl_corner_offset_infill = generate_relative_value_2d([super().get_position()[0] - 1.5, super().get_position()[1] + super().get_size()[1] + 0.25])
        bar_width_ratio = self.health / enemy_data[self.type]["Health"]
        width_height_infill = generate_relative_value_2d([(super().get_size()[0] + 3) * bar_width_ratio, 0.5])

        pygame.draw.rect(screen, (20,20,20), [tl_corner_offset, width_height])
        pygame.draw.rect(screen, (220,20,20), [tl_corner_offset_infill, width_height_infill])

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
        super().__init__("Alien", [7, 10])

class batBoss(Enemy):
    def __init__(self):
        super().__init__("Images/Sprites/Enemies/batBass.png", size = (50, 50))

class beeEnemy(Enemy):
    def __init__(self, ):
        super().__init__("Bee")

class butterflyEnemy(Enemy):
    def __init__(self):
        super().__init__("Images/Sprites/Enemies/butterflyEnemy.png")

class flyEnemy(Enemy):
    def __init__(self, position):
        super().__init__(position, "Fly")

class greenBoss(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/Enemies/greenBoss.png", size = (50, 50))

class orangeAlien(Enemy):
    def __init__(self, position):
        super().__init__(position, "OrangeAlien")

class purpleShip_Alien(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/Enemies/purple_shipAlien.png", size = (50, 50))

class redAlien(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/Enemies/redAlien.png")

class spider(Enemy):
    def __init__(self, position):
        super().__init__(position, "Images/Sprites/Enemies/spider.png")









