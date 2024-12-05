import pygame
from src.base_classes.item_shop import *
from src.base_classes.menu import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def toggle_group_visibility(group, state):
    for sprite in group:
        sprite.visible = state

def toggle_weapons():
    toggle_group_visibility(weapons_group, True)
    toggle_group_visibility(ships_group, False)
    toggle_group_visibility(upgrades_group, False)

def toggle_ships():
    toggle_group_visibility(weapons_group, False)
    toggle_group_visibility(ships_group, True)
    toggle_group_visibility(upgrades_group, False)

def toggle_upgrades():
    toggle_group_visibility(weapons_group, False)
    toggle_group_visibility(ships_group, False)
    toggle_group_visibility(upgrades_group, True)

weapons_group = pygame.sprite.Group()
ships_group = pygame.sprite.Group()
upgrades_group = pygame.sprite.Group()
buttons_group = pygame.sprite.Group()

gatlin_laser_gun = weapons(screen,"images/Game_Shop/Blasters/gatlin_laser_gun.png",
                           200, {"Damage": 250, "Velocity": 10}, "Gatlin Gun")

purple_blaster = weapons(screen,"images/Game_Shop/Blasters/purple_blaster.png",
                         150, {"Damage": 150, "Velocity": 15}, "Purple Blaster")

rocket_launcher = weapons(screen,"images/Game_Shop/Blasters/rocket_launcher.png",100,
                {"Damage": 500, "Velocity": 3}, "Rocket Launcher")

yellow_blaster = weapons(screen,"images/Game_Shop/Blasters/yellow_blaster.png",450,
        {"Damage": 300, "Velocity": 12}, "Yellow_Blaster")

# Creating instances of each ship.
black_ship = ships(screen,"images/Game_Shop/Ships/black_ship.png",
                           500, {"Health": 400, "Velocity": 10}, "Black Ship")

orange_ship = ships(screen,"images/Game_Shop/Ships/orange_ship.png",
                         550, {"Health": 300, "Velocity": 15}, "Orange Ship")

red_spider_ship = ships(screen,"images/Game_Shop/Ships/red_spider_ship.png",
                         450, {"Health": 700, "Velocity": 5}, "Red Spider Ship")

white_ship = ships(screen,"images/Game_Shop/Ships/white_ship.png",
                         450, {"Health": 500, "Velocity": 10}, "White Ship")

# Creating instances of each upgrade.
decrease_cooldown = upgrades(screen,"images/Game_Shop/Upgrades/decrease_cooldown.png",500,
        {"Cooldown Decrease": 200}, "Cooldown Decrease")

increase_damage = upgrades(screen,"images/Game_Shop/Upgrades/increase_damage.png",550,
        {"Damage Increase": 30}, "Increase Damage")

increase_health = upgrades(screen,"images/Game_Shop/Upgrades/increase_health.png",450,
        {"Health Increase": 100}, "Increase Health")

upgrades_placeholder = upgrades(screen,"images/Game_Shop/Upgrades/placeholder.png",450,
        {"Placeholder" : "x"}, "Upgrades Placeholder")

weapons_group.add(gatlin_laser_gun, purple_blaster, rocket_launcher, yellow_blaster)
ships_group.add(black_ship, orange_ship, red_spider_ship, white_ship)
upgrades_group.add(increase_health, increase_damage, upgrades_placeholder, decrease_cooldown)

weapons_category_button = item_category_button(300, 520, "Weapons",
                                               lambda: toggle_weapons(), screen)

ships_category_button = item_category_button(400, 520, "Ships",
                                             lambda: toggle_ships(), screen)

upgrades_category_button = item_category_button(500, 520, "Upgrades",
                                                lambda: toggle_upgrades(), screen)

buttons_group.add(weapons_category_button, ships_category_button, upgrades_category_button)