import pygame
from moviepy.video.io.VideoFileClip import VideoFileClip

import src.common_variables
from src.common_variables import *

pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
# screen = pygame.display.set_mode(screen_dimensions, pygame.FULLSCREEN, 32)

from src.game_state import *
from src.BaseClasses.Entities.player import *
from src.Tools.Misc_Tools.time_handler import Timer
from src.Tools.EnemyScripts.parse_engine.tools import parse_engine
from src.Tools.Misc_Tools.unit_handler import *

pygame.display.set_caption("Space Defenders")

# Playing the intro animation and closing it once done.
# intro_video = VideoFileClip("Videos/intro_animation.mp4")
# intro_video.preview()
# intro_video.close()

script = parse_engine.engine.read_script("src/Tools/EnemyScripts/scripts/test.emscrpt")


# Initializes players and adds them to player_sprite_group

# placeholder actions to be replaced with class creation

fps_limit = 120
# Sets fps limit of global clock
Timer(fps_limit)

done = False

# Loop until the user clicks the close button.


# Used to manage how fast the screen updates
clock = pygame.time.Clock()


load_game_init()
load_intermediate()

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

    pygame.display.set_caption(f"Space Defenders -- {1/Timer.get_last_frame_time_s()}")

    screen.fill((0,0,0))

    player_sprite_group.draw(screen)


    for sprite in player_sprite_group:
        sprite.update()

    script.update()

    for i in player_sprite_group:
        for x in player_sprite_group:
            for y in x.projectile_group:
                hit = i.get_rect().colliderect(y.rect)
                if script.current_operation.type == "WAIT":
                    script.check_collision(y)




    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 120 frames per second
    clock.tick(120)
    Timer.update()
# Close the window and quit.
pygame.quit()