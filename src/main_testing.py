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
from src.Tools.json_handler import copy_default_json, rewrite_default_json

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
menu = Menu()
game_shop = open_and_background(ships_group,
            weapons_group, upgrades_group, buttons_group)

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# read json command

copy_default_json()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    events = pygame.event.get()
    for event in events:  # User did something
        # Window closing code
        if event.type == pygame.QUIT:
            rewrite_default_json()
            done = True
            # json rewrite function
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

        # Updating the position of the players with each frame
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for sprite in game.player_sprite_group:
                sprite.update_position(event)

    # Setting the background to black
    screen.fill(BLACK)

    # Drawing the players and game shop button
    game.player_sprite_group.draw(screen)

    # Drawing the game shop, next level buttons and main menu whenever a level is not running
    if not game.level_is_running:
        game.update()
        menu.update()
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
            for button in buttons_group:
                button.draw()
                button.check_click()

            # Looped drawing of the game items
            for group in [ships_group, weapons_group, upgrades_group]:
                rest_unequipped = False
                equipped_sprite = None

                for sprite in list(group):
                    sprite.draw()
                        # group.remove(sprite)
                        # group.add(sprite)

                    sprite.update(events)

                    if rest_unequipped:
                        sprite.equipped = False
                    if sprite.equipped:
                        rest_unequipped = True
                        equipped_sprite = sprite

                if equipped_sprite:
                    group.remove(equipped_sprite)
                    group.add(equipped_sprite)

        # Drawing the purchase and equipping screens
        if shop_items.purchase_background_visibility:
            draw_choice_screen(shop_items.current_item.purchase_button_yes,
                   shop_items.current_item.purchase_button_no,
                   shop_items.current_item.purchase_background_surface,
            )

        if shop_items.equipping_background_visibility:
            draw_choice_screen(shop_items.current_item.equip_confirm,
                    shop_items.current_item.equip_deny,
                    shop_items.current_item.equipping_background_surface
                               )

    # Updating the position of each player.
    for player in game.player_sprite_group:
        player.update()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()

