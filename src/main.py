import pygame
import pygame.event
from moviepy.editor import * # Library for mp4 player
from pygame import KEYDOWN
from common_variables import *

from base_classes.player import player
from base_classes.menu import *
import time
import os

# Center the pygame window on the screen
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

menu = Menu(screen) # Game menu

player_sprite_group = pygame.sprite.Group()

# Drawing one or both players depending on the value given.
# This is then passed into the player modw button as its callback.
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

    # Once either button has been clicked, both disappear.
    if one_player_button:
       one_player_button.visible = False
    if two_player_button:
        two_player_button.visible = False


# placeholder actions to be replaced with class creation
one_player_button = player_mode_choice(screen_width/2 - 150, screen_height - 90,
"One Player", lambda: initialize_sprites(1), screen)

two_player_button = player_mode_choice(screen_width/2 + 150, screen_height - 90,
"Two Players",lambda: initialize_sprites(2), screen)


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

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    menu.update(events)
    one_player_button.update(events)
    two_player_button.update(events)

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill((0,0,0))

    menu.draw()
    one_player_button.draw()
    two_player_button.draw()

    player_sprite_group.draw(screen)

    for sprite in player_sprite_group:
        sprite.update()

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 120 frames per second
    clock.tick(120)

# Close the window and quit.
pygame.quit()