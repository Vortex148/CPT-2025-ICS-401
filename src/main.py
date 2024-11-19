import pygame
import pygame.event
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





pygame.display.set_caption("Space Defenders")

# intro_video = VideoFileClip("Videos/intro_animation.mp4")
# intro_video.preview()
# intro_video.close()


player1 = player()
player2 = player()

enemy = classicAlien((100,100))

player_sprite_group = pygame.sprite.Group(player1, player2)
enemy_sprite_group = pygame.sprite.Group(enemy)

fps_limit = 120
Timer(fps_limit)

done = False

# Loop until the user clicks the close button.




# Used to manage how fast the screen updates
clock = pygame.time.Clock()



while not done:



    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            player1.update_position(event)
            player2.update_position(event)




    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill((0,0,0))




    pygame.display.set_caption(f"Space Defenders -- FPS {clock.get_fps()}")


    player_sprite_group.draw(screen)
    enemy_sprite_group.draw(screen)


    player1.update()
    player2.update()

    # testing_sprite.update()
    # screen.blit(player1.image, player1.rect)

    enemy_sprite_group.update()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(fps_limit)
    Timer.update()
# Close the window and quit.
pygame.quit()