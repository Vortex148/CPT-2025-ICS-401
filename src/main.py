import pygame
import pygame.event
from moviepy.editor import *
from pygame import KEYDOWN
from common_variables import *

from base_classes.player import player
from base_classes.menu import Menu, Clickability
import time
import os

from src.base_classes.menu import player_mode_choice

# Center the Pygame window on the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'


pygame.init()


# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Defenders")

# Playing the intro animation and closing it once done.
intro_video = VideoFileClip("Videos/intro_animation.mp4").resize(height = screen_height, width = screen_width)
intro_video.preview()
intro_video.close()

menu = Menu(screen)

one_player_button = player_mode_choice(screen_width/2, screen_height - 30, "One Player", print("Placeholder action"))
two_player_button = player_mode_choice(screen_width/2, screen_height - 30, "Two Players", print("Placeholder action"))

player1 = player()
player2 = player()

player_sprite_group = pygame.sprite.Group(player1, player2)



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
            player1.update_position(event)
            player2.update_position(event)




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

    player1.update()
    player2.update()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 120 frames per second
    clock.tick(120)

# Close the window and quit.
pygame.quit()