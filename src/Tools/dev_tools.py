import math
import pygame
import numpy
from numpy.ma.core import array
from src.tools.unit_handler import generate_relative_value_2d


class vector_drawer:
    font = pygame.font.SysFont("arial.ttf", 30)

    def __init__(self, rect):
        self.shape = rect
        self.screen = pygame.display.get_surface()

    def draw(self, xyspeed, overall_speed, max_speed, accel, accel_xy ,heading, distance_to_target, desired_pose, runner, index, max_index):
        # Velocity label
        velocity_label = self.font.render(
            f"X-Y Speed : {array(numpy.around(xyspeed, 3))} Speed: {round(overall_speed, 3)}",
            True,
            (255, 255, 255),
        )
        velocity_label_rect = numpy.add(self.shape.center, [-velocity_label.get_width() / 2, 50])

        # Distance label
        distance_label = self.font.render(
            f"Distance : {round(distance_to_target, 3)} ", True, (255, 255, 255)
        )
        distance_label_rect = numpy.add(self.shape.center, [-distance_label.get_width() / 2, 70])

        # Acceleration label
        accel_label = self.font.render(
            f"Acceleration : {array(numpy.around(accel, 2))} ", True, (255, 255, 255)
        )
        accel_label_rect = numpy.add(self.shape.center, [-accel_label.get_width() / 2, 90])
        # ID label
        id_label = self.font.render(
            f"{runner.id} ", True, (255, 255, 255)
        )
        id_label_rect = numpy.add(self.shape.center, [40, 30])

        # Index label

        index_label = self.font.render(
            f"{index} / {max_index} ", True, (255, 255, 255)
        )
        index_label_rect = numpy.add(self.shape.center, [55, 10])


        # Desired pose marker
        pygame.draw.circle(
            self.screen, [0, 255, 0], tuple(generate_relative_value_2d(desired_pose)), 10
        )
        pygame.draw.line(
            self.screen,
            [0, 255, 0],
            tuple(generate_relative_value_2d(desired_pose)),
            self.shape.center,
        )

        accel_heading = math.atan2(-accel_xy[0], accel_xy[1])
        print(accel_heading)

        # Main circle
        pygame.draw.circle(self.screen, (255, 255, 255), self.shape.center, 50, 5)

        # Heading and speed line
        heading_line_start = self.shape.center
        heading_line_end = numpy.add(
                self.shape.center, [-math.sin(accel_heading) * 50, math.cos(accel_heading) * 50]

        )

        # Convert to tuple for Pygame
        pygame.draw.line(
            self.screen,
            (255, 255, 255),
            tuple(heading_line_start),
            tuple(heading_line_end),
            3,
        )

        # Draw labels
        self.screen.blit(velocity_label, tuple(velocity_label_rect))
        self.screen.blit(distance_label, tuple(distance_label_rect))
        self.screen.blit(accel_label, tuple(accel_label_rect))
        self.screen.blit(id_label, tuple(id_label_rect))
        self.screen.blit(index_label, tuple(index_label_rect))
