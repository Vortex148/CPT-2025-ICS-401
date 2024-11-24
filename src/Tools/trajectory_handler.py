import numpy
import math


from src.tools.time_handler import Timer
from src.tools.dev_tools import vector_drawer


class trajectory_handler:
    tolerance = 0.1

    def __init__(self, max_speed, accel, position, rect, runner):
        self.max_speed = max_speed

        self.accel = accel
        self.position = position
        self.trajectory_index = 0
        self.last_speed = [0, 0]
        self.rect = rect
        self.initial_pose = None
        self.dev_tools = vector_drawer(self.rect)
        self.path_iteration = 0
        self.runner = runner

    def update_max_speed(self, value):
        self.max_speed = value

    def update_acceleration(self, value):
        self.accel = value

    def follow_trajectory(self, trajectory, current_position):
        if self.last_speed[0] == 0:  # Start of current_trajectory
            self.initial_pose = current_position.copy()

        if self.trajectory_index < len(trajectory):  # Check if current_trajectory is complete

            current_node = trajectory[self.trajectory_index]
            previous_node = trajectory[self.trajectory_index - 1] if self.trajectory_index > 0 else self.initial_pose
            self.current_trajectory = trajectory

            # Calculate updated position
            delta_position_over_time = numpy.add(
                self.__go_to_node(
                    previous_node,
                    current_node,
                    current_position,
                ),
                current_position,
            )
            distance_to_node = numpy.subtract(current_position, current_node)

            # Check if the node is reached
            if (
                math.isclose(distance_to_node[0], 0, abs_tol=self.tolerance)
                and math.isclose(distance_to_node[1], 0, abs_tol=self.tolerance)
            ):
                self.trajectory_index += 1
                print(f"Reached Node {self.trajectory_index}")
                self.path_iteration = 0
                if self.trajectory_index == len(trajectory):
                    self.trajectory_index = 0
                    self.last_speed = [0, 0]

            return delta_position_over_time

    #TODO: Check time logic. Im pretty sure its wrong but it works
    def __go_to_node(self, start_position, end_position, current_position):
        delta_y = end_position[1] - current_position[1]
        delta_x = end_position[0] - current_position[0]

        dist_to_node = math.sqrt(delta_x**2 + delta_y**2)
        # Converts acceleration from units/sec to units/frame time. Need to validate
        acceleration = self.accel / (1 / Timer.delta)

        # Calculate initial motion parameters
        if self.path_iteration == 0:
            self.time_to_decelerate = self.max_speed / self.accel
            self.dist_to_decelerate = (1 / 2) * self.accel * (self.time_to_decelerate**2)
            self.dist_at_max_speed = max(0, dist_to_node - 2 * self.dist_to_decelerate)
            self.time_at_max_speed = (
                self.dist_at_max_speed / self.max_speed if self.dist_at_max_speed > 0 else 0
            )
            self.estimated_path_length = (
                self.time_to_decelerate * 2 + self.time_at_max_speed
            )

        heading = math.atan2(delta_y, delta_x)

        # Acceleration and deceleration logic
        if dist_to_node <= self.dist_to_decelerate:
            # To prevent from decelerating to fast and missing node, causes slight overshoot on occasion
            acceleration = -acceleration * 0.90
        else:
            acceleration = acceleration#


        acceleration *= Timer.delta  # Scale by time delta (frame time)

        # Update speed with clamping
        acceleration_x = math.cos(heading) * acceleration
        acceleration_y = math.sin(heading) * acceleration
        x_speed = self.last_speed[0] + acceleration_x
        y_speed = self.last_speed[1] + acceleration_y
        speed_magnitude = math.sqrt(x_speed**2 + y_speed**2)

        if speed_magnitude * 1 / Timer.delta > self.max_speed:  # Limit speed to max
            scale = self.max_speed * Timer.delta / speed_magnitude
            x_speed *= scale
            y_speed *= scale

        self.last_speed = [x_speed, y_speed]

        # Compute new position delta
        delta_position = numpy.array([x_speed, y_speed])
        x_speed = x_speed * 1 / Timer.delta
        y_speed = y_speed * 1 / Timer.delta

        # Comment out to disable overlay
        self.dev_tools.draw(
            [x_speed, -y_speed],
            math.sqrt(x_speed**2 + y_speed**2),
            acceleration,
            [acceleration_x, acceleration_y],
            dist_to_node,
            end_position,
            self.runner,
            self.trajectory_index,
            len(self.current_trajectory)
        )
        self.path_iteration += 1

        return delta_position
