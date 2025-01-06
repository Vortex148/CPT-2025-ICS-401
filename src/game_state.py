from src.BaseClasses.button_classes import basic_button
from src.BaseClasses.Entities.player import *

from src.Tools.Misc_Tools.time_handler import *
from src.Tools.Misc_Tools.unit_handler import swth_object
from src.common_variables import *
from src.Tools.Misc_Tools.drawing_tools import draw_resource_overlay

screen = pygame.display.get_surface()



class settings_menu:
    def __init__(self):
        self.x = 100
        self.tgt = 100
        self.menu = swth_object("Images/Objects/Menu/Settings Menu/setting_menu", [self.x, 0], size=[100,100])

    def set_position(self, position):
        self.tgt = position

    def draw(self):

        if self.tgt != self.x:
            if self.tgt == 0:
                self.x -= 2
            else:
                self.x += 2

        self.menu.draw([self.x , 0])

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x




def load_game_init():
    settings_menu_opened = False
    player_1 = swth_object("Images/Objects/Menu/Ships/ship_1", [10,10], size=[7,10])
    player_2 = swth_object("Images/Objects/Menu/Ships/ship_2", [20,10], size=[7,10])
    stars = swth_object("Images/Objects/Menu/Stars/background_stars", [0,-100], size=[100,250])
    setting_word = swth_object("Images/Objects/Menu/Settings Menu/settings_word", [85, 1], size=[9, 4])
    global screen
    screen = pygame.display.get_surface()
    settings = settings_menu()

    one_player_button = basic_button("Images/Objects/Menu/Player Select/player_1",[15,80], [15,10], execute_hover= lambda : player_1.draw([19,68]))
    two_player_button = basic_button("Images/Objects/Menu/Player Select/player_2", [70,80], [15, 10], execute_hover= lambda : (player_1.draw([68,68]),player_2.draw([80,68])))
    settings_button = basic_button("Images/Objects/Menu/Settings Menu/settings_gear", [95,0.725], [3.5, 5])
    bg = swth_object("Images/Objects/Menu/Background/Space Defenders Main Screen", frame_count=1)
    bg.draw()
    while True:
        pygame.display.set_caption(f"Space Defenders -- {1 / Timer.get_last_frame_time_s()}")

        # Draws settings menu
        if settings_menu_opened:
            settings_menu()

        # Draws stars
        if stars.get_position()[1] != 0:
            stars.update_position(numpy.add(stars.get_position(), [0, 0.125]))
        else:
            stars.update_position([0, -125])

        stars.draw()
        events = pygame.event.get()

        if one_player_button.check_click():
            initialize_sprites(1)
            break
        elif two_player_button.check_click():
            initialize_sprites(2)
            break


        setting_word.fade(settings_button.check_hover())
        setting_word.draw()


        if settings_button.check_click() and settings.get_x() > 50:
            settings.set_position(0)
            one_player_button.set_actionable(False)
            two_player_button.set_actionable(False)

        elif settings_button.check_click() and settings.get_x() < 50:
            settings.set_position(100)
            one_player_button.set_actionable(True)
            two_player_button.set_actionable(True)




        # Draws player buttons
        one_player_button.draw()
        two_player_button.draw()


        settings.draw()
        settings_button.draw()
        pygame.display.flip()

        Timer.update()

        # Draws background image
        bg.draw()




def load_intermediate():
    depart_and_explore_button = basic_button("Images/Objects/Intermediate/depart_and_explore_button", [38, 20],
                                             [16 * 1.5, 9 * 1.5], progress_bar_dimensions=[4.5,8.89,14.6,0.5])
    research_new_tech_button = basic_button("Images/Objects/Intermediate/research_new_tech_button", [38, 70], [16 * 1.5, 9 * 1.5], progress_bar_dimensions=[4.5,8.87,14.6,0.5], execute_click= lambda : load_research_intermediate())

    while True:
        pygame.display.set_caption(f"Space Defenders -- {1 / Timer.get_last_frame_time_s()}")
        events = pygame.event.get()
        screen.fill((0, 0, 0))

        depart_and_explore_button.update_progress_bar(depart_and_explore_button.check_hover())
        research_new_tech_button.update_progress_bar(research_new_tech_button.check_hover())

        if depart_and_explore_button.check_click_conditional():
            break
        research_new_tech_button.check_click_conditional()

        depart_and_explore_button.draw()
        research_new_tech_button.draw()

        pygame.display.flip()
        Timer.update()

def adjust_page(index, increase=True):
    if increase:
        index[0] = index[0] + 1
    else:
        index[0] = index[0] - 1


def load_research_intermediate():
    index = [0]
    left_select = basic_button("Images/Objects/Intermediate/selector_arrow", [30, 70], [5, 5], 180, execute_click= lambda: adjust_page(index, False), click_delay=0.25)
    right_select = basic_button("Images/Objects/Intermediate/selector_arrow", [70, 70], [5, 5], 0, execute_click= lambda: adjust_page(index), click_delay=0.25)
    background = swth_object("Images/Objects/Intermediate/tech_tree_bg", size=[300, 100], position=[0,0])

    while True:
        background.update_position([0 + (index[0] * -100),0 ])
        background.draw()
        pygame.display.set_caption(f"Space Defenders -- {1 / Timer.get_last_frame_time_s()}")
        events = pygame.event.get()

        if index[0] == 0:
            left_select.disable()

        elif index[0] == research_tree_max:
            right_select.disable()

        else:
            left_select.enable()
            right_select.enable()



        left_select.draw()
        right_select.draw()

        left_select.check_hover()
        right_select.check_hover()

        left_select.check_click()
        right_select.check_click()

        draw_resource_overlay([70, 90])
        pygame.display.flip()
        Timer.update()