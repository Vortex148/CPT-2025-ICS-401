from time import perf_counter

import pygame

def check_dynamic_user_input(player, event):
    from src.base_classes.player import player

    if event.type == pygame.KEYDOWN:
        print(player.player_number)
        if player.player_number == 1:

            if event.key == pygame.K_w:
                print(player.MOVEMENT_SPEED)
                player.velocity[1] = player.MOVEMENT_SPEED
            if event.key == pygame.K_s:
                player.velocity[1] = -player.MOVEMENT_SPEED
            if event.key == pygame.K_a:
                player.velocity[0] = -player.MOVEMENT_SPEED
            if event.key == pygame.K_d:
                player.velocity[0] = player.MOVEMENT_SPEED

        elif player.player_number == 2:
            if event.key == pygame.K_UP:
                player.velocity[1] = player.MOVEMENT_SPEED
            if event.key == pygame.K_DOWN:
                player.velocity[1] = -player.MOVEMENT_SPEED
            if event.key == pygame.K_LEFT:
                 player.velocity[0] = -player.MOVEMENT_SPEED
            if event.key == pygame.K_RIGHT:
                player.velocity[0] = player.MOVEMENT_SPEED

    elif event.type == pygame.KEYUP:
        if player.player_number == 1:
            if event.key == pygame.K_w:
                print("w")
                player.velocity[1] = 0
            if event.key == pygame.K_s:
                player.velocity[1] = 0
            if event.key == pygame.K_a:
                player.velocity[0] = 0
            if event.key == pygame.K_d:
                player.velocity[0] = 0

        elif player.player_number == 2:
            if event.key == pygame.K_UP:
                player.velocity[1] = 0
            if event.key == pygame.K_DOWN:
                player.velocity[1] = 0
            if event.key == pygame.K_LEFT:
                player.velocity[0] = 0
            if event.key == pygame.K_RIGHT:
                player.velocity[0] = 0
