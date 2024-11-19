import pygame

class Timer:
    last_tick = None
    clock = pygame.time.Clock()
    fps_cap = None

    def __init__(self, fps_cap):
        Timer.fps_cap = fps_cap
        Timer.clock.tick(fps_cap)
        Timer.last_tick = Timer.clock.get_time()


    @staticmethod
    def get_last_frame_time():
        if Timer.last_tick is None:
            raise Exception("Clock was never updated")
        if Timer.clock.get_time() - Timer.last_tick > 1000:
            raise Exception("Clock was likely not updated in time")

        return Timer.clock.get_time() * 0.001

    @staticmethod
    def update():
        Timer.last_tick = Timer.clock.tick(Timer.fps_cap)
