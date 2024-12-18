import pygame
from src.base_classes.item_shop import *
from src.base_classes.menu import *
from src.item_shop_instances import (buttons_group, weapons_group,
        ships_group, upgrades_group)
# from moviepy.editor import *
from src.base_classes.game_state import game
from src.base_classes.item_shop import shop_items

# Initializing the game engine.
pygame.init()

# Screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Creating the screen and setting a caption
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main_Testing")

# Playing the intro video.
'''intro_video = VideoFileClip("Videos/intro_animation.mp4").resize(height = screen_height, width = screen_width)
intro_video.preview()
intro_video.close()'''

# Creating  player mode choice buttons, the menu and game shop
game.create_buttons()
menu = Menu(screen)
game_shop = open_and_background(screen, ships_group,
            weapons_group, upgrades_group, buttons_group)

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    events = pygame.event.get()
    for event in events:  # User did something
        # Window closing code
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

        # Updating the position of the players with each frame
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for sprite in game.player_sprite_group:
                sprite.update_position(event)


    # UPDATE BLOCK FOR MENU AND ITEM SHOP
    # Checking for hover and clicks on buttons
    game.update(events)

    for button in buttons_group:
        if button.visible:
            button.update(events)

    # Setting the background to black
    screen.fill(BLACK)

    # Drawing the players and game shop button
    game.player_sprite_group.draw(screen)

    # Drawing the menu and player buttons on startup
    if not game.level_is_running:
        menu.update(events)
        game_shop.update(events)

        menu.draw()
        game_shop.draw()

        if game.one_player_button.visible:
            game.one_player_button.draw()
            game.two_player_button.draw()

        if game_shop.item_shop_visible:
            for button_sprite in buttons_group:
                button_sprite.draw()

            for group in [weapons_group, ships_group, upgrades_group]:
                for sprite in group:
                    sprite.item_sprite.check_hover()
                    sprite.update(events)
                    if sprite.visible:
                        sprite.draw()
            # if

        # If the purchase confirmation background is showing, the "yes", "no" buttons are drawn
        if shop_items.purchase_background_visibility:
            screen.blit(shop_items.current_item.purchase_background_surface, (100, 100))
            shop_items.purchase_button_yes.update(events)
            shop_items.purchase_button_no.update(events)
            draw_choice_buttons(shop_items, "purchase_button_yes", "purchase_button_no")


    for player in game.player_sprite_group:
        player.update()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()

