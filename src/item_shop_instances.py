import pygame
from src.base_classes.item_shop import *
from src.base_classes.menu import *
from src.Tools.global_tools import toggle_group_visibility
from src.Tools.json_handler import read_json
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
upgrades_list = ["Increase Health", "Increase Damage", "Movement Speed Increase"]

# Looped creation of items in the shop
for index, _ in enumerate(weapons_list + ships_list + upgrades_list):
    length_2 = len(weapons_list) + len(ships_list)
    length_3 = length_2 + len(upgrades_list)

    # Defining item specific attributes based on the index (and thus the list currently being iterated)
    if index < len(weapons_list):
        name = weapons_list[index]
        # Defining searches to extract JSON attributes (done in the following two elifs as well)
        searches = [f"{name}.Weapon Sprite", f"{name}.Price", f"{name}.Damage", f"{name}.Velocity"]
        GROUP = weapons_group
        LIST = weapons_list
        class_type = weapons
        item_info = ["Damage", "Velocity"]
        local_index = index
        reading_file = "weapons"
    elif len(weapons_list) <= index < length_2:
        local_index = index - len(weapons_list)
        name = ships_list[local_index]
        searches = [f"{name}.Sprite", f"{name}.Price", f"{name}.Health", f"{name}.Velocity"]
        GROUP = ships_group
        LIST = ships_list
        class_type = ships
        item_info = ["Health", "Movement Speed"]
        reading_file = "ships"
    elif length_2 <= index < length_3:
        local_index = index - length_2
        name = upgrades_list[local_index]
        searches = [f"{name}.Sprite", f"{name}.Price", f"{name}.{name}"]
        GROUP = upgrades_group
        LIST = upgrades_list
        class_type = upgrades
        item_info = [f"{name}"]
        reading_file = "upgrades"

    print("Reading JSON")
    results = read_json(reading_file, searches)

    # Copying the results of the search to variables for use in instantiation
    attr1 = results[0]
    attr2 = results[1]
    attr3 = results[2]
    if len(LIST) >= 4:
        attr4 = results[3]

    attributes = [attr1, attr2, attr3, attr4]
    print(f"Attributes: {attributes}")
    NAME = f"{name}"

    x = len(item_info)
    ITEM_INFO = {}

    # Defining "item info" as one variable to fit the format of classes' arguments
    for y in range(x):
        ITEM_INFO[item_info[y]] = attributes[y+2]

    print(f"Item Info: {ITEM_INFO}")

    # Creating instances of each item and adding them to the respective group
    instance = create_instance(class_type, screen, NAME, attr1, attr2, ITEM_INFO)
    LIST[local_index] = instance
    instance = LIST[local_index]
    GROUP.add(instance)

# Defining some buttons
weapons_category_button = basic_button(300, 540, "Weapons",
                                               lambda: toggle_weapons(), screen, 60, 20)

ships_category_button = basic_button(400, 540, "Ships",
                                             lambda: toggle_ships(), screen, 60, 20)

upgrades_category_button = basic_button(500, 540, "Upgrades",
                                                lambda: toggle_upgrades(), screen, 60, 20)

buttons_group.add(weapons_category_button, ships_category_button, upgrades_category_button)


# Toggling the ships when the module is initialized to draw the ships by default when the shop is opened.
toggle_ships()



