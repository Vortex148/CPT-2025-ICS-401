import pygame
from winsound import PlaySound

from base_classes.player import player

pygame.init()

# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Space Defenders")
player1 = player()
player2 = player()

# Loop until the user clicks the close button.
done = False



# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:

    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill((0,0,0))




    pygame.display.set_caption(f"Space Defenders -- FPS {clock.get_fps()}")

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(120)

# Close the window and quit.
pygame.quit()