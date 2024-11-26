import pygame

# Initialize Pygame
from src.base_classes.item_shop import open_and_background

pygame.init()

# Screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main_Testing")

# Loop until the user clicks the close button

game_shop = open_and_background(screen)

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # --- Game logic should go here
    # (Add any movement, collisions, or updates to game objects)

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    game_shop.update(events)

    screen.fill(WHITE)

    game_shop.draw()

    # Draw other game objects here
    # Example: pygame.draw.rect(screen, (0, 0, 255), [50, 50, 100, 100])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
