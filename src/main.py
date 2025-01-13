import pygame
from moviepy.video.io.VideoFileClip import VideoFileClip

pygame.init()

size = (1280, 720)
pygame.display.set_mode(size, pygame.FULLSCREEN, 32)

from src.game_state import *
from src.BaseClasses.Entities.player import *
from src.Tools.Misc_Tools.time_handler import Timer
from src.Tools.EnemyScripts.parse_engine.tools import parse_engine
from src.Tools.Misc_Tools.unit_handler import *



# Playing the intro animation and closing it once done.
# intro_video = VideoFileClip("Videos/intro_animation.mp4")
# intro_video.preview()
# intro_video.close()

# Sets fps limit of global clock
Timer(120)

load_game_init()
load_intermediate()

pygame.quit()