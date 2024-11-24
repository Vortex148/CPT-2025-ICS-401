
from pygame.time import Clock
import time


class Timer:
    last_tick = None
    clock = Clock()
    fps_cap = None
    max_frame_delay = 0.1
    last_time = time.time()
    last_time_ns = 0
    current_time = time.time()
    delta = 0.001

    def __init__(self, fps_cap):
        Timer.fps_cap = fps_cap
        Timer.clock.tick(fps_cap)
        Timer.last_tick = Timer.clock.get_time()

    @staticmethod
    def get_time_s():
        return Timer.current_time


    @staticmethod
    # Returns frame time in seconds (Time between frames)
    def get_last_frame_time_s():
        clock_tick = Timer.clock.get_time()
        if Timer.last_tick is None:
            raise Exception("Clock was never updated")
        if clock_tick / 1000 > Timer.max_frame_delay:
            print(f"Clock was not updated in time, sending fake frame with value of {Timer.last_tick / 1000}")
            return Timer.last_tick / 1000
        Timer.last_tick = clock_tick
        return Timer.clock.get_time() / 1000

    @staticmethod
    def update():
        clock_tick = Timer.clock.tick(Timer.fps_cap)

        # To try and mitigate stuttering
        if clock_tick / 1000 > Timer.max_frame_delay:
            print(f"Clock was not updated in time, sending fake frame with value of {Timer.last_tick / 1000}")
        else:
            Timer.last_tick = clock_tick
            Timer.current_time = time.time()
            Timer.delta = Timer.current_time - Timer.last_time  # Calculate delta
            Timer.last_time = Timer.current_time  # Update last_time for the next frame
