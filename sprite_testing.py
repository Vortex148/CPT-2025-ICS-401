import pygame.sprite
import math


class projectile(pygame.sprite.Sprite):
    rect = None
    image = None
    sprite = None
    last_position = (0, 0)

    def __init__(self, sprite):
        super().__init__()
        self.image = sprite
        self.sprite = sprite
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 640 - self.rect.width/2
        self.rect.y = 360 - self.rect.height/2

    def set_position(self, x, y, theta):
        mouse_pos = pygame.mouse.get_pos()
        if not math.isclose(self.last_position[0], mouse_pos[0], abs_tol=5) and not math.isclose(self.last_position[1], mouse_pos[1], abs_tol=5):
            self.image = self.sprite
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.image = pygame.transform.rotate(self.image, theta)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.rect.center = (x, y)
            self.last_position = (x, y)
            print(self.last_position)


class player(pygame.sprite.Sprite):
    rect = None
    image = None

    sprite_list = []

    projectile_group = pygame.sprite.Group()
    projectile_sprite = None

    last_bearing = 0.0
    bearing = 0.0
    projectile_speed = 4

    last_relative_mouse_pos = (0, 0)

    def __init__(self, ):
        super().__init__()
        self.projectile_sprite = pygame.image.load("images/player/projectiles/projectile.png").convert_alpha()

        self.image = pygame.image.load("images/player/Ship Rev 1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 640 - self.rect.width / 2
        self.rect.y = 360 - self.rect.height / 2

    def update_mouse_heading(self):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        mouse_x = mouse_x - self.rect.center[0]
        mouse_y = mouse_y - self.rect.center[1]

        self.last_relative_mouse_pos = (mouse_x, mouse_y)

        if mouse_x == 0:
            heading = 0

        else:
            heading = math.atan(mouse_y / mouse_x)
            heading = -heading * 180 / math.pi + 90

        if mouse_x > 0:
            heading = heading - 180

        self.last_bearing = self.bearing
        self.bearing = heading
        if self.last_bearing != self.bearing:
            self.image = pygame.image.load("images/player/Ship Rev 1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.image = pygame.transform.rotate(self.image, heading)
            self.rect = self.image.get_rect(center=self.rect.center)

    def generate_projectile(self):

        bullet = projectile(self.projectile_sprite)
        self.projectile_group.add(bullet)
        self.sprite_list.append(bullet)

    def update_group(self):
        self.projectile_group.draw(surface=pygame.display.get_surface())

        for i in self.sprite_list:
            x_pos = pygame.mouse.get_pos()[0] - i.rect.center[0]
            y_pos = pygame.mouse.get_pos()[1] - i.rect.center[1]

            theta = math.atan2(y_pos, x_pos)

            translation = (
                math.cos(theta) * self.projectile_speed,
                math.sin(theta) * self.projectile_speed
            )

            i.set_position(i.rect.center[0] + translation[0], i.rect.center[1] + translation[1],
                           -math.degrees(theta + math.pi / 2))

class enemy(pygame.sprite.Sprite):

    rect = None
    image = None

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/player/Bad Dude Ship Rev 1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 100 - self.rect.width / 2
        self.rect.y = 100 - self.rect.height / 2