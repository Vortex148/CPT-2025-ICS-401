import pygame.draw

from src.Tools.EnemyScripts.parse_engine.tools.conversion_tools import tools
from src.BaseClasses import enemy

class PathFollower:
    def __init__(self, enemy_data, index):

        self.enemy_data = tools.char_array_to_enemy_data(enemy_data, index)
        self.follower = enemy.generate_enemy(self.enemy_data.type)

    def update(self):
        self.follower.follow_trajectory(self.enemy_data.nodes)
        self.follower.generate_relative_coords()
        self.follower.draw()
        # print(self.follower.get_rect())
        pygame.draw.circle(pygame.display.get_surface(), (255,0,0),self.follower.get_rect().center, 10)
        # print(self.follower.get_position())

