from time import time_ns

import pygame
import random

from moviepy.editor import *
from pygame import KEYDOWN, FULLSCREEN
import src.tools.unit_handler as uh
import src.tools.time_handler

from base_classes.player import player
import time

from src.base_classes.enemy import classicAlien
from src.tools.time_handler import Timer

pygame.init()

# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)

enemy_3_nodes = []
for i in range(0,1000):
    enemy_3_nodes.append([random.randrange(10,90,1), random.randrange(10,90,1)])


pygame.display.set_caption("Space Defenders")

# Playing the intro animation and closing it once done.
intro_video = VideoFileClip("Videos/intro_animation.mp4").resize(height = screen_height, width = screen_width)
intro_video.preview()
intro_video.close()

menu = Menu(screen)

player_sprite_group = pygame.sprite.Group()

def initialize_sprites(value):
    global player_sprite_group, one_player_button, two_player_button
    player_sprite_group.empty()
    if value == 1:
        player1 = player()
        player_sprite_group.add(player1)
    if value == 2:
        player1 = player()
        player2 = player()
        player_sprite_group.add(player1, player2)
    if one_player_button:
       one_player_button.visible = False
    if two_player_button:
        two_player_button.visible = False

enemy = classicAlien()
enemy2 = classicAlien()
enemy3 = classicAlien()

enemy.update_position([90,90])
enemy2.update_position([10,10])

enemy3.update_position([random.randrange(10,90,1), random.randrange(10,90,1)])

player_sprite_group = pygame.sprite.Group(player1, player2)
enemy_sprite_group = pygame.sprite.Group(enemy, enemy2, enemy3)

# placeholder actions to be replaced with class creation
one_player_button = player_mode_choice(screen_width/2 - 150, screen_height - 90,
"One Player", lambda: initialize_sprites(1), screen)
two_player_button = player_mode_choice(screen_width/2 + 150, screen_height - 90,
"Two Players",lambda: initialize_sprites(2), screen)

fps_limit = 120
Timer(fps_limit)

done = False

# Loop until the user clicks the close button.




# Used to manage how fast the screen updates
clock = pygame.time.Clock()



while not done:



    # --- Main event loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for sprite in player_sprite_group:
                sprite.update_position(event)




    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    menu.update(events)
    one_player_button.update(events)
    two_player_button.update(events)

    screen.fill((0,0,0))

    # pygame.display.set_caption(f"Space Defenders -- FPS {clock.get_fps()}")

    menu.draw()
    one_player_button.draw()
    two_player_button.draw()

    player_sprite_group.draw(screen)
    enemy_sprite_group.draw(screen)


    for sprite in player_sprite_group:
        sprite.update()
    player1.update()
    player2.update()

    enemy.follow_trajectory([[50,50], [80,60], [10,20], [90,10], [70,50]]) if enemy.active else None
    enemy2.follow_trajectory([[10,10], [90,90], [10,90], [90,10], [50,50]]) if enemy2.active else None
    enemy3.follow_trajectory(enemy_3_nodes) if enemy3.active else None
    # testing_sprite.update()
    # screen.blit(player1.image, player1.rect)
    enemy_sprite_group.update()
    for i in enemy_sprite_group:
        for x in player1.projectile_group:
            hit = i.get_rect().colliderect(x.rect)
            if hit:
                i.kill()

        for x in player2.projectile_group:
            hit = i.get_rect().colliderect(x.rect)
            if hit:
                i.kill()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 120 frames per second
    clock.tick(120)

# Close the window and quit.
pygame.quit()