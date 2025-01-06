import os

# Using the os package to generate file paths to each folder
PROJECT_ROOT = os.path.join(os.path.dirname(__file__))
json_directory = os.path.join(PROJECT_ROOT, "JSON_Files")
images_directory = os.path.join(PROJECT_ROOT, "images")
videos_directory = os.path.join(PROJECT_ROOT, "Videos")
sounds_directory = os.path.join(PROJECT_ROOT, "Sounds")

screen_dimensions = (1920, 1080)
research_tree_max = 2