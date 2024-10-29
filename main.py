import random

import pygame
import math

import sprite_testing

pygame.init()

# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space Defenders")

mouse_x = 0
mouse_y = 0
# Loop until the user clicks the close button.
done = False

player = sprite_testing.player()
enemy = sprite_testing.enemy()

group = pygame.sprite.Group()


# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:

    # --- Main event loop
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            player.generate_projectile()
        if event.type == pygame.QUIT:
            done = True



    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill((0,0,0))

    player.update_mouse_heading()

    player.update_group()

    # --- Drawing code should go here
    player.update()

    hit = False
    screen.blit(player.image, player.rect)
    for i in player.sprite_list:
        if i.rect.colliderect(enemy.rect):
            hit = True


    if not hit:
        screen.blit(enemy.image, enemy.rect)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    pygame.display.set_caption(f"Space Defenders -- FPS {clock.get_fps()}")
    clock.tick(120)

# Close the window and quit.
pygame.quit()