import pygame
from src.base_classes.item_shop import *
from src.base_classes.menu import *
from src.Tools.global_tools import toggle_group_visibility
from src.Tools.json_handler import read_json_2
import json
from src.Tools.global_tools import create_instance


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Function for changing the visibility of the entire group

# Using the visibility function to display only the category selected
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

# Instantiating groups to add the items to.
weapons_group = pygame.sprite.Group()
ships_group = pygame.sprite.Group()
upgrades_group = pygame.sprite.Group()
buttons_group = pygame.sprite.Group()


weapons_list = ["Gatlin Gun", "Purple Blaster", "Rocket Launcher", "Yellow Blaster"]
ships_list = ["Black Ship", "Orange Ship", "White Ship", "Red Spider Ship"]
upgrades_list = ["Health Increase", "Damage Increase", "Movement Speed Increase"]

for i in enumerate(weapons_list + ships_list): # + upgrades_list
    name = weapons_list[i] if i < 4 else ships_list[i-4] # if i <8 else weapons_list[i-8]

    if i < 4:
        searches = [f"{name}.Ship Sprite", f"{name}.Price", f"{name}.Damage", f"{name}.Velocity"]
        GROUP = weapons_group
        LIST = weapons_list
        class_type = weapons
        item_info = ["Damage", "Velocity"]
    elif 4 < i <= 8:
        searches = [f"{name}.Ship Sprite", f"{name}.Price", f"{name}.Health", f"{name}.Velocity"]
        GROUP = ships_group
        LIST = ships_list
        class_type = ships
        item_info = ["Health", "Movement Speed"]
    elif 8 < i <= 12:
        # searches = [f"{name}.Ship Sprite", f"{name}.Price", f"{name}.Health", f"{name}.Velocity"]
        # GROUP = upgrades_group
        # LIST = upgrades_list
        # class_type = upgrades
        # item_info = ["Upgrade"]
        pass

    results = read_json_2("weapons" if i < 4 else "ships", searches)

    # weapons(screen, attr1, attr2, {"Damage": attr3, "Velocity": attr4}, NAME)

    attr1 = results[0]
    attr2 = results[1]
    attr3 = results[2]
    attr4 = results[3]

    # looped append and variable def
    attributes = [attr1, attr2, attr3, attr4]
    NAME = f"{name}"

    x = len(item_info)
    ITEM_INFO = {}

    for y in range(x):
        ITEM_INFO[y] = attributes[y+2]

    instance = create_instance(class_type, screen, attr1, attr2, ITEM_INFO, NAME)

    LIST[i] = instance
    instance = LIST[i]
    GROUP.add(instance)

# Defining some weapons
'''gatlin_laser_gun = weapons(screen,"images/Game_Shop/Blasters/gatlin_laser_gun.png",
                           200, {"Damage": 250, "Velocity": 10}, "Gatlin Gun")

purple_blaster = weapons(screen,"images/Game_Shop/Blasters/purple_blaster.png",
                         150, {"Damage": 150, "Velocity": 15}, "Purple Blaster")

rocket_launcher = weapons(screen,"images/Game_Shop/Blasters/rocket_launcher.png",100,
                {"Damage": 500, "Velocity": 5}, "Rocket Launcher")

yellow_blaster = weapons(screen,"images/Game_Shop/Blasters/yellow_blaster.png",450,
        {"Damage": 300, "Velocity": 12}, "Yellow Blaster")
'''
# Defining some ships
black_ship = ships(screen,"images/Game_Shop/Ships/black_ship.png",
                           500, {"Health": 400, "Velocity": 10}, "Black Ship")

orange_ship = ships(screen,"images/Game_Shop/Ships/orange_ship.png",
                         550, {"Health": 300, "Velocity": 15}, "Orange Ship")

red_spider_ship = ships(screen,"images/Game_Shop/Ships/red_spider_ship.png",
                         450, {"Health": 700, "Velocity": 5}, "Red Spider Ship")

white_ship = ships(screen,"images/Game_Shop/Ships/white_ship.png",
                         450, {"Health": 500, "Velocity": 10}, "White Ship")

# Defining some upgrades
increase_movement_speed = upgrades(screen,"images/Game_Shop/Upgrades/increase_movement_speed.png",500,
        {"Movement Speed Increase": 2}, "Movement Speed Increase")

increase_damage = upgrades(screen,"images/Game_Shop/Upgrades/increase_damage.png",550,
        {"Damage Increase": 30}, "Increase Damage")

increase_health = upgrades(screen,"images/Game_Shop/Upgrades/increase_health.png",450,
        {"Health Increase": 100}, "Increase Health")

upgrades_placeholder = upgrades(screen,"images/Game_Shop/Upgrades/placeholder.png",450,
        {"Placeholder" : "x"}, "Upgrades Placeholder")

# Defining some buttons
weapons_category_button = basic_button(300, 540, "Weapons",
                                               lambda: toggle_weapons(), screen, 60, 20)

ships_category_button = basic_button(400, 540, "Ships",
                                             lambda: toggle_ships(), screen, 60, 20)

upgrades_category_button = basic_button(500, 540, "Upgrades",
                                                lambda: toggle_upgrades(), screen, 60, 20)

# Adding the items to their respective groups

# weapons_group.add(gatlin_laser_gun, purple_blaster, rocket_launcher, yellow_blaster)
ships_group.add(black_ship, orange_ship, red_spider_ship, white_ship)
upgrades_group.add(increase_health, increase_damage, upgrades_placeholder, increase_movement_speed)
buttons_group.add(weapons_category_button, ships_category_button, upgrades_category_button)


# Toggling the ships when the module is initialized to draw the ships by default when the shop is opened.
toggle_ships()



