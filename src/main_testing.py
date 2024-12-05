import pygame
from src.base_classes.item_shop import *
from src.base_classes.menu import *
from src.item_shop_instances import buttons_group, weapons_group, ships_group, upgrades_group

pygame.init()

# Screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main_Testing")

game_shop = open_and_background(screen)

# Groups for each category of items

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
            sprite.item_sprite.check_hover()
            sprite.update(events)
            if sprite.visible:
                sprite.draw()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()

