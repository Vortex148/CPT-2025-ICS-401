from tokenize import group

import pygame
from common_variables import *
from menu import Clickability

item_counter = 0

# Creating the visibility function globally so it can be accessed in each class. It is like a switch.
def visibility(target1, group_target = None):
    target1.visible = not target1.visible

    if group_target:
        for sprite in group_target:
            sprite.visible = not sprite.visible

def display_info(item_counter):
    font = pygame.font.SysFont('Comic Sans', 20)
    stats = f"Name: {shop_items.name}, Price: {shop_items.price} ,Stats: {shop_items.stats}"
    info_surface = font.render(stats, True, (255, 255, 255))
    screen.blit(info_surface, (info_x, info_y))
    pass

class open_and_background:
    def __init__(self, screen):
        self.screen = screen
        open_button = pygame.image.load("images/buttons_and_menus/shopping_cart.png")
        open_button = pygame.transform.scale(open_button, (menu_button_width, menu_button_height))

        self.open_button_sprite = Clickability(
            open_button,
            700,
            100,
            lambda: visibility(self.background_sprite)
        )

        shop_background = pygame.image.load("images/buttons_and_menus/shop_background.png")
        shop_background = pygame.transform.scale(shop_background, (600, 600))
        self.background_sprite = Clickability(
            shop_background,
            400,
            screen_height/2,
            None
        )

        self.background_sprite.visible = False

        close_button_image = pygame.image.load("images/buttons_and_menus/Close.png")
        close_button_image = pygame.transform.scale(close_button_image, (close_button_width, close_button_height))

        self.close_button_sprite = Clickability(
            close_button_image,
            550,
            70,
            lambda: visibility(self.background_sprite, item_group))

    def update(self, events):
        self.open_button_sprite.check_click(events)

        if self.background_sprite.visible:
            self.close_button_sprite.check_click(events)

    def draw(self):
        self.open_button_sprite.draw(self.screen)

        if self.background_sprite.visible:
            self.background_sprite.draw(self.screen)
            self.close_button_sprite.draw(self.screen)

class shop_items(pygame.sprite.Sprite):
    item_counter = 0
    item_counter += 1
    def __init__(self, screen, path, price):
        super().__init__()
        self.item_number = item_counter
        self.screen = screen
        self.price = price
        item_image = pygame.image.load(path)
        item_image = pygame.transform.scale(item_image, (item_width, item_height))
        self.hover_image = pygame.draw.rect(screen, RED, [100, 100, 50, 50])
        self.visible = False


        if self.item_number <= 2:
            pos_x = 150 * self.item_number
            pos_y = 130 * self.item_number
        elif self.item_number > 2:
            pos_x = 150 * (self.item_number - 2)
            pos_y = 130 * self.item_number

        self.item_sprite = Clickability(
            item_image,
            pos_x,
            pos_y,
            lambda: None, # to be replaced with purchase function
            self.hover_image,
            lambda: None # to be replaced with hover drawing code
        )

class weapons(shop_items):
    def __init__(self, screen , path, price, damage, velocity):
        super().__init__()
        self.damage = damage
        self.velocity = velocity

class ships(shop_items):
    def __init__(self, screen , path, price, health, velocity):
        super().__init__()
        self.health = health
        self.velocity = velocity

class upgrades(shop_items):
    def __init__(self, screen , path, price, health_increase, velocity_increase):
        super().__init__()
        self.health_increase = health_increase
        self.velocity_increase = velocity_increase

weapons_group = pygame.sprite.Group()
weapon = weapons()
weapons_group.add(weapon)

ships_group = pygame.sprite.Group()
ship = ships()
ships_group.add(ship)

upgrade_group = pygame.sprite.Group()
upgrade = upgrades()
upgrade_group.add(upgrade)















