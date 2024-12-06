import pygame
from src.base_classes.item_shop import *
from src.base_classes.menu import *
from src.item_shop_instances import buttons_group, weapons_group, ships_group, upgrades_group
# from moviepy.editor import *
from src.base_classes.game_state import game

pygame.init()

# Screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main_Testing")

'''intro_video = VideoFileClip("Videos/intro_animation.mp4").resize(height = screen_height, width = screen_width)
intro_video.preview()
intro_video.close()'''

game.create_buttons()

player_sprite_group = pygame.sprite.Group()

menu = Menu(screen)

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for sprite in player_sprite_group:
                sprite.update_position(event)

    # --- Game logic should go here
    # (Add any movement, collisions, or updates to game objects)

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    menu.update(events)
    game.one_player_button.update(events)
    game.two_player_button.update(events)

    game_shop.update(events)

    for button in buttons_group:
        button.update(events)

    screen.fill(BLACK)

    menu.draw()
    game.one_player_button.draw()
    game.two_player_button.draw()

    player_sprite_group.draw(screen)

    for sprite in player_sprite_group:
        sprite.update()

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

