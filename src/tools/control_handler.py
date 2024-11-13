from src.base_classes.player import player
import pygame

def check_dynamic_user_input(player: player):
    # Do refactor in future to optimize performance
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if player.player_number == 1:
                if event.key == pygame.K_w:
                    player.position[1] += player.MOVEMENT_SPEED
                if event.key == pygame.K_s:
                    player.position[1] -= player.MOVEMENT_SPEED
                if event.key == pygame.K_a:
                    player.position[0] -= player.MOVEMENT_SPEED
                if event.key == pygame.K_d:
                    player.position[0] += player.MOVEMENT_SPEED