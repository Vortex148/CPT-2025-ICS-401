import pygame

# Initialize Pygame
from src.base_classes.item_shop import *
from src.base_classes.menu import *

pygame.init()

# Screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main_Testing")

# Groups for each category of items
weapons_group = pygame.sprite.Group()
ships_group = pygame.sprite.Group()
upgrades_group = pygame.sprite.Group()
buttons_group = pygame.sprite.Group()
# Loop until the user clicks the close button

game_shop = open_and_background(screen)

# Creating instances of each weapon.

gatlin_laser_gun = weapons(screen,"images/Game_Shop/Blasters/gatlin_laser_gun.png",
                           200, [10, 10], 15, 10)

purple_blaster = weapons(screen,"images/Game_Shop/Blasters/purple_blaster.png",
                         150, [10, 20], 10, 20)

rocket_launcher = weapons(screen,"images/Game_Shop/Blasters/rocket_launcher.png",
                         100, f"Name: Rocket Launcher\n Price: ", 10, 10)

weapons_placeholder = weapons(screen,"images/Game_Shop/Upgrades/placeholder.png",
                         450, f"Placeholder", "Placeholder", 10, 10)

# Creating instances of each ship.
black_ship = ships(screen,"images/Game_Shop/Ships/black_ship.png",
                           500, [], 10, 10)

orange_ship = ships(screen,"images/Game_Shop/Ships/orange_ship.png",
                         550, [], 10, 10)

red_spider_ship = ships(screen,"images/Game_Shop/Ships/red_spider_ship.png",
                         450, [], 10, 10)

white_ship = ships(screen,"images/Game_Shop/Ships/white_ship.png",
                         450, [], 10, 10)

# Creating instances of each upgrade.
decrease_cooldown = upgrades(screen,"images/Game_Shop/Upgrades/decrease_cooldown.png",
                           500, [], 10, 10)

increase_damage = upgrades(screen,"images/Game_Shop/Upgrades/increase_damage.png",
                         550, [], 10, 10)

increase_health = upgrades(screen,"images/Game_Shop/Upgrades/increase_health.png",
                         450, [], 10, 10)

upgrades_placeholder = upgrades(screen,"images/Game_Shop/Upgrades/placeholder.png",
                         450, [], 10, 10)

weapons_group.add(gatlin_laser_gun, purple_blaster, rocket_launcher, weapons_placeholder)
ships_group.add(black_ship, orange_ship, red_spider_ship, white_ship)
upgrades_group.add(increase_health, increase_damage, upgrades_placeholder, decrease_cooldown)

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

weapons_category_button = item_category_button(300, 520, "Weapons",
                                               lambda: toggle_weapons(), screen)

ships_category_button = item_category_button(400, 520, "Ships",
                                             lambda: toggle_ships(), screen)

upgrades_category_button = item_category_button(500, 520, "Upgrades",
                                                lambda: toggle_upgrades(), screen)

buttons_group.add(weapons_category_button, ships_category_button, upgrades_category_button)

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    events = pygame.event.get()
    for event in events:  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # --- Game logic should go here
    # (Add any movement, collisions, or updates to game objects)

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    game_shop.update(events)

    for button in buttons_group:
        button.update(events)

    screen.fill(BLACK)

    game_shop.draw()

    for button_sprite in buttons_group:
        button_sprite.draw()

    for group in [weapons_group, ships_group, upgrades_group]:
        for sprite in group:
            sprite.update(events)
            if sprite.visible:
                sprite.draw()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
