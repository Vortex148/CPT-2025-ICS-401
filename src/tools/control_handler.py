from time import perf_counter

import pygame

def check_dynamic_user_input(selected_player, event):
    from src.base_classes.player import player

    if event.type == pygame.KEYDOWN:

        if selected_player.player_number == 1:
            if event.key == pygame.K_w:
                selected_player.velocity[1] = -selected_player.MOVEMENT_SPEED
            elif event.key == pygame.K_s:
                selected_player.velocity[1] = selected_player.MOVEMENT_SPEED
            elif event.key == pygame.K_a:
                selected_player.velocity[0] = -selected_player.MOVEMENT_SPEED
            elif event.key == pygame.K_d:
                selected_player.velocity[0] = selected_player.MOVEMENT_SPEED
            elif event.key == pygame.K_x:
                selected_player.fire_selected_weapon()

        elif selected_player.player_number == 2:
            if event.key == pygame.K_UP:
                selected_player.velocity[1] = -selected_player.MOVEMENT_SPEED
            elif event.key == pygame.K_DOWN:
                selected_player.velocity[1] = selected_player.MOVEMENT_SPEED
            elif event.key == pygame.K_LEFT:
                 selected_player.velocity[0] = -selected_player.MOVEMENT_SPEED
            elif event.key == pygame.K_RIGHT:
                selected_player.velocity[0] = selected_player.MOVEMENT_SPEED
            elif event.key == pygame.K_SPACE:
                selected_player.fire_selected_weapon()

    elif event.type == pygame.KEYUP:
        if selected_player.player_number == 1:
            if event.key == pygame.K_w:
                selected_player.velocity[1] = 0
            elif event.key == pygame.K_s:
                selected_player.velocity[1] = 0
            elif event.key == pygame.K_a:
                selected_player.velocity[0] = 0
            elif event.key == pygame.K_d:
                selected_player.velocity[0] = 0

        elif selected_player.player_number == 2:
            if event.key == pygame.K_UP:
                selected_player.velocity[1] = 0
            elif event.key == pygame.K_DOWN:
                selected_player.velocity[1] = 0
            elif event.key == pygame.K_LEFT:
                selected_player.velocity[0] = 0
            elif event.key == pygame.K_RIGHT:
                selected_player.velocity[0] = 0
