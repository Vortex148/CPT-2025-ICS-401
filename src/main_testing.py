'''
-----------------------------------------------------------

Name:  Space Defenders

Purpose: For our CPT we created a Galaga-type game. This was
an incredible learning experience both inside and out of programming.
Intensive use of classes and animation techniques no doubt improved our
ability as programmers. However, there was equal learning in working as a team.

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
from src.common_variables import screen

# Initializing the game engine.
pygame.init()

# Playing the intro video.
'''intro_video = VideoFileClip("Videos/intro_animation.mp4").resize(height = screen_height, width = screen_width)
intro_video.preview()
intro_video.close()'''

# Creating player mode choice buttons, the menu and game shop
game.create_buttons()
menu = Menu()
game_shop = open_and_background(ships_group,
            weapons_group, upgrades_group, buttons_group)

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

copy_default_json()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    events = pygame.event.get()

    for event in events:

        # Window closing code. JSON data rewritten
        if event.type == pygame.QUIT:
            rewrite_default_json()
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

        # Updating the position of the players with each frame
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for sprite in game.player_sprite_group:
                sprite.update_position(event)

    # Setting the background to black -- all drawing code beneath
    screen.fill(BLACK)

    # Drawing the players and game shop button
    game.player_sprite_group.draw(screen)

    # Drawing the game shop, next level buttons and
    # main menu whenever a level is not running
    if not game.level_is_running:
        # UPDATE BLOCK: ensures fresh values
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
                    sprite.update(events)

                    # Ensuring only one sprite of each category can be equipped
                    if sprite.equipped:
                        rest_unequipped = True
                        equipped_sprite = sprite

                    if rest_unequipped:
                        sprite.equipped = False

                # Moving the equipped sprite to the end of this list so that all
                # the other sprites are updated before the loop ends.
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

