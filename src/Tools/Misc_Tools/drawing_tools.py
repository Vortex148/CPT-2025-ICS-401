import json

import numpy
import pygame
import numpy as np
from src.Tools.Misc_Tools.unit_handler import swth_object, generate_relative_value_2d

player_data = json.load(open("src/JSON_Files/game_data.json"))
screen = pygame.display.get_surface()

common_resource_sprite = swth_object("Images/Sprites/Resources/common_resource", size=[6 * 0.8, 8 * 0.8],opacity=0)
rare_resource_sprite = swth_object("Images/Sprites/Resources/rare_resource",size=[6 * 0.8, 8 * 0.8], opacity=0)
legendary_resource_sprite = swth_object("Images/Sprites/Resources/legendary_resource",size=[6 * 0.8, 8 * 0.8], opacity=0)
text = pygame.sysfont.SysFont("calibri", 30)

resources = [common_resource_sprite, rare_resource_sprite, legendary_resource_sprite]

def draw_resource_overlay(pos):
    element_pos = [[0,0], [10,0], [20,0]]
    player_resource_data = player_data["resources"]
    update_group_opacity(resources, 255)

    for i in range(len(element_pos)):
        element_pos[i] = np.add(element_pos[i], pos)

    for i in range(len(player_resource_data)):
        offset = numpy.add(element_pos[i], [5, 4])

        # Prevents clipping when user has large quantity of a resource
        text_data = player_resource_data[list(player_resource_data.keys())[i]]
        text_data = text_data if text_data < 1000 else 999

        rendered_text = text.render(f"{text_data}", True, (255,255,255))
        screen.blit(rendered_text, generate_relative_value_2d(offset))

    update_group_position(resources, element_pos)
    group_draw(resources)

def update_group_opacity(group, opacity):
    for i in group:
        i.set_opacity(opacity)

def update_group_position(group, pos):
    for i in range(len(group)):
        group[i].update_position(pos[i])

def group_draw(group):
    for i in group:
        i.draw()
