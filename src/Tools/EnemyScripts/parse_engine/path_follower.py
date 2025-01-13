import numpy
import pygame.draw
import math

from src.Tools.EnemyScripts.parse_engine.tools.conversion_tools import tools
from src.BaseClasses.Entities import enemy



class PathFollower:
    def __init__(self, enemy_data, index):

        self.enemy_data = tools.char_array_to_enemy_data(enemy_data, index)

        self.starting_dist = 30


        self.initial_pos_heading = numpy.subtract(self.enemy_data.nodes[1], self.enemy_data.nodes[0])
        self.initial_pos_heading = math.atan2(self.initial_pos_heading[1], self.initial_pos_heading[0])
        self.initial_pos_heading = - self.initial_pos_heading - math.pi / 2

        self.initial_pos = [math.sin(self.initial_pos_heading) * self.starting_dist, math.cos(self.initial_pos_heading) * self.starting_dist]
        self.initial_pos = numpy.add(self.initial_pos, self.enemy_data.nodes[0])


        self.follower = enemy.generate_enemy(self.enemy_data.type, self.initial_pos)

    def get_projectile_group(self):
        return self.follower.get_projectile_group()

    def update(self):
        self.follower.follow_trajectory(self.enemy_data.nodes)
        self.follower.generate_relative_coords()
        self.follower.draw()
        # print(self.follower.get_rect())
        # pygame.draw.circle(pygame.display.get_surface(), (255,0,0),self.follower.get_rect().center, 10)
        # print(self.follower.get_position())
