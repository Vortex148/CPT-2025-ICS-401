'''

-----------------------------------------------------------

Name:  Space Defenders

Purpose: For our CPT we created a Galaga-type game. This was
an incredible learning experience both inside and out of programming.
Intensive use of classes and animation techniques no doubt improved our
ability as programmers. However, there was equal learning in working as a team
We both agree we

Authors:   Charlie Blackburn, John Szewczyk

Created From:  10/28/2024 to 01/17/2025

-----------------------------------------------------------

'''
import pygame
from src.base_classes.item_shop import *
from src.base_classes.menu import *
from src.item_shop_instances import (buttons_group, weapons_group,
        ships_group, upgrades_group)
# from moviepy.editor import *
from src.base_classes.game_state import game
from src.base_classes.item_shop import shop_items
from src.Tools.global_tools import draw_choice_screen

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
    game.update(events)

    for button in buttons_group:
        if button.visible:
            button.update(events)

    # Setting the background to black
    screen.fill(BLACK)

    # Drawing the players and game shop button
    game.player_sprite_group.draw(screen)

    # Drawing the game shop, next level buttons and main menu whenever a level is not running
    if not game.level_is_running:
        menu.update(events)
        game_shop.update(events)

        # Drawing the menu and game shop
        menu.draw()
        game_shop.draw()

        # Drawing the player mode choice buttons if they are visible
        if game.one_player_button.visible or game.two_player_button.visible:
            game.one_player_button.draw()
            game.two_player_button.draw()

        # Drawing the item shop if the state tracker for it is true.
        if game_shop.item_shop_visible:
            for button_sprite in buttons_group:
                button_sprite.draw()

            # Looped drawing of the game items
            for group in [weapons_group, ships_group, upgrades_group]:
                for sprite in group:
                    sprite.item_sprite.check_hover()
                    sprite.update(events) # checking for clicks
                    if sprite.visible:
                        sprite.draw()

        # If the yes/no background is showing, the "yes", "no" buttons are drawn.
        # This handles both the purchase and equipping menus.
        if shop_items.purchase_background_visibility:
            draw_choice_screen(shop_items, "purchase_background_visibility", shop_items.current_item.purchase_button_yes,
                               shop_items.current_item.purchase_button_no, shop_items.current_item.purchase_background_surface,
                               events, screen,lambda: draw_choice_buttons(shop_items, "purchase_button_yes", "purchase_button_no"))
        if shop_items.equipping_background_visibility:
            draw_choice_screen(shop_items, "equipping_background_visibility", shop_items.current_item.equip_confirm,
                               shop_items.current_item.equip_deny, shop_items.current_item.purchase_background_surface,
                               events, screen, lambda: draw_choice_buttons(shop_items, "equip_confirm", "equip_deny"))

        # Once the players have been initialized, the start level button is drawn.
        # It is only drawn when the item shop is inivisible so that it is not accidentally clicked.
        if game.player_button_clicked_state and not game_shop.item_shop_visible:
            game.start_game_button.draw()

    # Updating the position of each player.
    for player in game.player_sprite_group:
        player.update()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()

