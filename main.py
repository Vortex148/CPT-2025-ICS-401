import pygame
from moviepy.editor import VideoFileClip

from base_classes.player import player
from base_classes.enemy import Enemy

pygame.init()

# Initializing the game clock
clock = pygame.time.Clock()

# Set the width and height of the screen [width, height]
screen_width = 1280
screen_height = 720
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Defenders")

player1 = player()
player2 = player()


def play_intro_animation(video_path):
    intro_animation = VideoFileClip(video_path)
    intro_animation = intro_animation.resize(size)

    for frame in intro_animation.iter_frames(fps=24, dtype="uint8"):
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Convert the frame to a surface and blit it on the screen
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

    # Close the clip after playing
    intro_animation.close()


# Main function
def main():
    # Play the startup video
    play_intro_animation("Intro Animation.mp4")

    # Main game loop
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Clear the screen with a color (e.g., black)
        screen.fill((0, 0, 0))

        # Update the caption with FPS
        pygame.display.set_caption(f"Space Defenders -- FPS {clock.get_fps():.2f}")
        pygame.display.flip()

        clock.tick(120)

    # Run the main function
    main()
pygame.quit()
