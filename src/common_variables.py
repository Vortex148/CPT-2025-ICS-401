import os

# Using the os package to generate file paths to each folder
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
json_directory = os.path.join(PROJECT_ROOT, "src", "JSON_Files")
images_directory = os.path.join(PROJECT_ROOT, "images")
hover_images_directory = os.path.join(PROJECT_ROOT, "images", "Game_Shop", "Hover Images")
videos_directory = os.path.join(PROJECT_ROOT, "Videos")
sounds_directory = os.path.join(PROJECT_ROOT, "Sounds")
buttons_directory = os.path.join(images_directory, "Game_Shop", "Buttons")

screen_width = 800
screen_height = 600
menu_button_width, menu_button_height = 50, 50
rules_width, rules_height = 400, 400
close_button_width, close_button_height = 30, 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Primary Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
PINK = (255, 192, 203)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
WHITE = (0, 0, 0)