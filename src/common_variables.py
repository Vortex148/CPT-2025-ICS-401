import os
import pygame

# Using the os package to generate file paths to each folder
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
json_directory = os.path.join(PROJECT_ROOT, "src", "JSON_Files")
images_directory = os.path.join(PROJECT_ROOT, "images")
game_shop_directory = os.path.join(images_directory, "Game_Shop")
hover_images_directory = os.path.join(game_shop_directory, "Hover Images")
buttons_and_menus_directory = os.path.join(images_directory, "buttons_and_menus")
buttons_directory = os.path.join(game_shop_directory, "Buttons")

# Screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Creating the screen and setting a caption so it can be accessed globally
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f"Main Testing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
PINK = (255, 192, 203)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)