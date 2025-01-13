from src.Tools.Misc_Tools.unit_handler import *
from src.Tools.Misc_Tools.time_handler import *

screen = pygame.display.get_surface()


class basic_button(swth_object):


    def __init__(self, image, position = (0,0), width_height = (10,10), rotation=0,  execute_click=None, execute_hover=None, execute_not_hover=None, progress_bar_dimensions=None, click_delay = 0.25):
        self.screen = pygame.display.get_surface()
        self.position = position
        self.visible = True
        self.actionable = True
        self.image = image
        self.execute_click = execute_click
        self.execute_hover = execute_hover
        self.execute_not_hover = execute_not_hover
        self.condition_met = False
        self.progress_bar_dimensions = progress_bar_dimensions
        self.bar_progress = 0.0
        self.delay_timer = None
        super().__init__(self.image, self.position, width_height, rotation,2)
        if click_delay > 0:
            self.delay_timer = timed_delay(click_delay)

    def check_click(self):
        if self.visible and self.actionable:
            if self.check_hover():
                if pygame.mouse.get_pressed()[0] and self.delay_timer.did_delay_elapse() if self.delay_timer is not None else pygame.mouse.get_pressed()[0]:
                    self.execute_click() if self.execute_click else None
                    return True
            else:
                return False

    def check_click_conditional(self):
        if self.visible and self.actionable and self.condition_met:
            if self.check_hover():
                if pygame.mouse.get_pressed()[0]:
                    self.execute_click() if self.execute_click else None
                    return True
            else:
                return False

    def check_hover(self):
        # print(super().get_rect())
        if self.visible and self.actionable:
            if super().get_rect().collidepoint(pygame.mouse.get_pos()):
                super().set_frame_index(1)
                self.execute_hover() if self.execute_hover else None
                return True
            else:
                super().set_frame_index(0)
                self.execute_not_hover() if self.execute_not_hover else None
                return False

    def set_visible(self, visible):
        self.visible = visible

    def set_actionable(self, actionable):
        self.actionable = actionable

    def disable(self):
        self.visible = False
        self.actionable = False

    def enable(self):
        self.visible = True
        self.actionable = True

    def set_position(self, position):
        self.position = position

    def clicked(self):
        return super().get_rect().collidepoint(pygame.mouse.get_pos() and pygame.mouse.get_pressed()[0])

    def update_progress_bar(self, increase):
        tick = 0.05
        if increase and self.bar_progress <= 1.0 - tick:
            self.bar_progress += tick
        elif not increase and self.bar_progress >= 0.0 + tick:
            self.bar_progress -= tick
            self.condition_met = False
        elif self.bar_progress == 1.0:
            self.condition_met = True
        self.bar_progress = round(self.bar_progress, 2)


    def draw(self):
        self.delay_timer.update() if self.delay_timer else None
        if self.visible:
            super().draw()

            if self.progress_bar_dimensions:
                progress_bar_tl = generate_relative_value_2d(numpy.add(self.progress_bar_dimensions[0:2], self.position))
                progress_bar_wh = generate_relative_value_2d([self.progress_bar_dimensions[2] * self.bar_progress, self.progress_bar_dimensions[3]])
                pygame.draw.rect(screen, (40,200,40), [progress_bar_tl, progress_bar_wh])


