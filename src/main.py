import pygame

pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)

from src.game_state import initialize_game
import random
from src.BaseClasses.player import *
from src.BaseClasses.enemy import classicAlien
from src.Tools.time_handler import Timer
from src.BaseClasses.menu import *
from src.Tools.EnemyScripts.parse_engine.tools import parse_engine
import game_state

# Set the width and height of the screen [width, height]

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

initialize_game()

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
                    script.check_collision(y.rect)
                if hit:
                    i.kill()



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 120 frames per second
    clock.tick(120)
    Timer.update()
# Close the window and quit.
pygame.quit()