import enum
import random
import sys

from src.Tools.Misc_Tools.button_classes import basic_button
from src.BaseClasses.Entities.player import *

from src.Tools.Misc_Tools.time_handler import *
from src.Tools.Misc_Tools.unit_handler import swth_object, generate_relative_value_2d, generate_relative_value
from src.Tools.Misc_Tools.drawing_tools import draw_resource_overlay
from src.Tools.EnemyScripts.parse_engine.tools import parse_engine



screen = pygame.display.get_surface()

difficulty_data = json.load(open("src/JSON_Files/difficulty_data.json"))
ship_data = json.load(open("src/JSON_Files/ships.json"))
weapon_data = json.load(open("src/JSON_Files/weapons.json"))
game_data = json.load(open("src/JSON_Files/game_data.json"))

player_count = 0

# Class for the equipment menu
class equipment_menu:
    def __init__(self, position, player: player):
        self.player = player
        self.position = position
        self.current_ship = swth_object(player.get_ship_path()[0:len(player.get_ship_path())-6], numpy.add(position, [7, -3]), [12, 16])
        self.equipment_menu = swth_object("Images/Objects/Intermediate/equipment_menu",numpy.add(position, [0, 16]), [26, 34], opacity=0.0)


        self.weapons_button = basic_button("Images/Objects/Intermediate/weapons_button", numpy.add(position, [0,29]), [12,9], execute_click= lambda :self.draw_weapon_select())
        self.ships_button = basic_button("Images/Objects/Intermediate/ships_button", numpy.add(position, [14,29]), [12,9], execute_click= lambda : self.draw_ship_select())

        self.ship_buttons = []
        self.weapon_buttons = []

        self.ships = game_data["unlocked_items"]["ships"].copy()
        self.weapons = game_data["unlocked_items"]["weapons"].copy()

        # Generates ship buttons based off unlocked ships
        for i in range(len(game_data["unlocked_items"]["ships"])):
            path = ship_data[game_data["unlocked_items"]["ships"][i]]["Sprite_P"+ str(player.player_number)]
            offset = numpy.add(self.position, [2, 18])
            ship_val = game_data["unlocked_items"]["ships"][i]
            ship = basic_button(path[0:len(path) - 6], numpy.add(offset,[8 * (i % 3), 12 if i > 2 else 0]), [5.5, 8], execute_click=lambda ship_val=ship_val: self.player.set_ship(ship_val) )
            ship.disable()
            self.ship_buttons.append(ship)

        # Generates weapons buttons based off unlocked weapons
        for i in range(len(game_data["unlocked_items"]["weapons"])):
            path = weapon_data[game_data["unlocked_items"]["weapons"][i]]["Sprite"]
            offset = numpy.add(self.position, [2, 18])
            weapon_val = game_data["unlocked_items"]["weapons"][i]
            weapon = basic_button(path[0:len(path) - 6], numpy.add(offset,[8 * (i % 3), 12 if i > 2 else 0]), [5.5, 8], execute_click=lambda weapon_val=weapon_val: self.player.set_weapon(weapon_val))
            weapon.disable()
            self.weapon_buttons.append(weapon)



    def draw(self):
        self.current_ship.draw()
        self.equipment_menu.draw()
        self.weapons_button.draw()
        self.ships_button.draw()
        for i in self.ship_buttons:
            i.check_click()
            i.draw()
        for i in self.weapon_buttons:
            i.check_click()
            i.draw()

    def update(self):
        self.weapons_button.check_click()
        self.ships_button.check_click()
        self.current_ship.set_frames(self.player.get_ship_path()[0:len(self.player.get_ship_path())-6])
        self.current_ship.update()
        self.draw()


    def draw_ship_select(self):
        # Disables weapon buttons
        for i in self.weapon_buttons:
            i.disable()

        # Draws ship buttons
        self.equipment_menu.set_opacity(255)
        self.weapons_button.set_position(numpy.add(self.position, [0,52]))
        self.ships_button.set_position(numpy.add(self.position, [14,52]))
        for i in self.ship_buttons:
            i.enable()

    def draw_weapon_select(self):
        # Disables ship buttons
        for i in self.ship_buttons:
            i.disable()

        # Draws weapon buttons
        self.equipment_menu.set_opacity(255)
        self.weapons_button.set_position(numpy.add(self.position, [0,52]))
        self.ships_button.set_position(numpy.add(self.position, [14,52]))
        for i in self.weapon_buttons:
            i.enable()

class health_bar:
    def __init__(self, image_path, position, player: player):
        self.player_data = player
        self.size = [20, 4]
        self.offset = [self.size[0]/20, self.size[1]/20]
        self.image = swth_object(image_path, position=position, size=self.size)
        self.bar_max_width = self.size[0] - self.offset[0] * 1.95
        self.bar = pygame.Rect(generate_relative_value_2d(numpy.add(position, self.offset)), generate_relative_value_2d(numpy.subtract(self.size, numpy.multiply(self.offset, [1.95 , 1.95]) )))
        self.visible = True
    def update(self):
        pass

    def draw(self):
        if self.visible:
            self.bar.width = generate_relative_value(self.player_data.health / self.player_data.max_health * self.bar_max_width, screen.get_width())
            pygame.draw.rect(screen, [255,0,0],rect=self.bar)
            self.image.draw()



class store_menu:
    def __init__(self, position):
        self.position = position
        self.background = swth_object("Images/Objects/Intermediate/equipment_menu", numpy.subtract(self.position, [31, 34]), [62, 68])
        self.exit_button = basic_button("Images/Objects/Mid_Game/exit_button", position=numpy.subtract(self.position, [-20,33]), width_height=[10, 5], execute_click=lambda :self.set_visibility(False))
        self.visible = False

        self.ship_buttons = []
        self.weapon_buttons = []

    def draw(self):
        self.background.draw()

    def update(self):
        if self.visible:
            self.draw()
            self.exit_button.draw()
            self.exit_button.check_click()


    def set_visibility(self, state):
        self.visible = state



class Difficulties(enum.Enum):
    Easy = "Easy"
    Medium = "Medium"
    Hard = "Hard"


class script_generator:

    def __init__(self, difficulty: Difficulties):
        self.levels = []
        level_data = difficulty_data[difficulty.value].copy()
        for i in range(20):
            self.levels.append(random.choice(level_data))

        print(self.levels)
        self.index = 0
        self.script = parse_engine.engine.read_script(self.levels[self.index]["path"])
        self.delay = timed_delay(2)
        self.overlay_on = False

    def update_script(self):

        script_done = self.script.update()

        if self.overlay_on:
            self.delay.did_delay_elapse()
            self.delay.update()
            self.overlay_on = not self.delay.did_delay_elapse()
            draw_resource_overlay([70,80])

        if script_done:
            player_file = open("src/JSON_Files/game_data.json")
            player_data = json.load(player_file)
            self.index += 1
            for i in range(len(player_data["resources"])):
                player_data["resources"][list(player_data["resources"].keys())[i]] = player_data["resources"][list(player_data["resources"].keys())[i]] + self.levels[self.index]["rewards"][i]
                file = open("src/JSON_Files/game_data.json", "w")
                json.dump(player_data, file)
                file.close()
                player_file.close()
                self.read_script()
                self.overlay_on = True

        else:
            for i in player_sprite_group:
                for y in i.projectile_group:
                    if self.script.current_operation.type == "WAIT":
                        self.script.check_collision(y)
            if self.script.current_operation.type != "END":
                if self.script.get_projectile_sprite_group():
                    for i in player_sprite_group:
                        for x in self.script.get_projectile_sprite_group():
                            for y in x:
                                i.check_collision(y)

    def read_script(self):
        self.script = parse_engine.engine.read_script(self.levels[self.index]["path"])

class settings_menu:
    def __init__(self):
        self.x = 100
        self.tgt = 100
        self.menu = swth_object("Images/Objects/Menu/Settings Menu/setting_menu", [self.x, 0], size=[100, 100])

    def set_position(self, position):
        self.tgt = position

    def draw(self):

        if self.tgt != self.x:
            if self.tgt == 0:
                self.x -= 2
            else:
                self.x += 2
        self.menu.draw([self.x, 0])

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x


def load_game_init():
    sys.setrecursionlimit(1_000_000)
    settings_menu_opened = False

    player_1 = swth_object("Images/Objects/Menu/Ships/ship_1", [10, 10], size=[7, 10])
    player_2 = swth_object("Images/Objects/Menu/Ships/ship_2", [20, 10], size=[7, 10])
    stars = swth_object("Images/Objects/Menu/Stars/background_stars", [0, -100], size=[100, 250])
    setting_word = swth_object("Images/Objects/Menu/Settings Menu/settings_word", [85, 1], size=[9, 4])
    global screen
    global player_count

    settings = settings_menu()

    one_player_button = basic_button("Images/Objects/Menu/Player Select/player_1", [15, 80], [15, 10],
                                     execute_hover=lambda: player_1.draw([19, 68]))
    two_player_button = basic_button("Images/Objects/Menu/Player Select/player_2", [70, 80], [15, 10],
                                     execute_hover=lambda: (player_1.draw([68, 68]), player_2.draw([80, 68])))
    settings_button = basic_button("Images/Objects/Menu/Settings Menu/settings_gear", [95, 0.725], [3.5, 5],
                                   click_delay=0.0)
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
            player_count = 1
            break
        elif two_player_button.check_click():
            initialize_sprites(2)
            player_count = 2
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
    store = store_menu([50,50])

    depart_and_explore_button = basic_button("Images/Objects/Intermediate/depart_and_explore_button", [38, 20],
                                             [16 * 1.5, 9 * 1.5], progress_bar_dimensions=[4.5, 8.89, 14.6, 0.5],
                                             execute_click=lambda: load_difficulty_selection())
    store_button = basic_button("Images/Objects/Intermediate/store_button", [38, 70],
                                            [16 * 1.5, 9 * 1.5],
                                            execute_click=lambda: store.set_visibility(True))

    player_menu = equipment_menu([5, 30], list(player_sprite_group)[0])
    if len(list(player_sprite_group)) > 1:
        player_2_menu = equipment_menu([69, 30], list(player_sprite_group)[1])
    while True:

        pygame.display.set_caption(f"Space Defenders -- {1 / Timer.get_last_frame_time_s()}")
        events = pygame.event.get()
        screen.fill((0, 0, 0))

        depart_and_explore_button.update_progress_bar(depart_and_explore_button.check_hover())

        depart_and_explore_button.check_click_conditional()
        store_button.check_click()

        depart_and_explore_button.draw()
        store_button.draw()

        player_menu.update()
        if len(list(player_sprite_group)) > 1:
            player_2_menu.update()

        store.update()

        pygame.display.flip()
        Timer.update()


def adjust_page(index, increase=True):
    if increase:
        index[0] = index[0] + 1
    else:
        index[0] = index[0] - 1


def load_difficulty_selection():
    easy_selection = basic_button("Images/Objects/Difficulty_Select/select_button", position=[10, 70],
                                  width_height=[20, 10], execute_click=lambda: load_game(Difficulties.Easy), execute_hover=lambda: easy_img.in_focus(True), execute_not_hover=lambda: easy_img.in_focus(False))
    medium_selection = basic_button("Images/Objects/Difficulty_Select/select_button", position=[40, 70],
                                    width_height=[20, 10], execute_click=lambda: load_game(Difficulties.Medium), execute_hover=lambda: medium_img.in_focus(True), execute_not_hover=lambda: medium_img.in_focus(False))
    hard_selection = basic_button("Images/Objects/Difficulty_Select/select_button", position=[70, 70],
                                  width_height=[20, 10], execute_click=lambda: load_game(Difficulties.Hard), execute_hover=lambda: hard_img.in_focus(True), execute_not_hover=lambda: hard_img.in_focus(False))

    easy_img = swth_object("Images/Objects/Difficulty_Select/easy_mode_sel", position=[10, 20], size=[20, 40])
    medium_img = swth_object("Images/Objects/Difficulty_Select/medium_mode_sel", position=[40, 20], size=[20, 40])
    hard_img = swth_object("Images/Objects/Difficulty_Select/hard_mode_sel", position=[70, 20], size=[20, 40])
    exit_button = basic_button("Images/Objects/Mid_Game/exit_button", position=[3,3], width_height=[10, 5])
    selection_made = [False, False, False]
    done = False

    while not done:
        if exit_button.check_click():
            break

        pygame.display.set_caption(f"Space Defenders -- {1 / Timer.get_last_frame_time_s()}")
        screen.fill((0, 0, 0))
        pygame.event.get()



        selection_made[0] = easy_selection.check_click()
        selection_made[1] = medium_selection.check_click()
        selection_made[2] = hard_selection.check_click()

        for i in selection_made:
            if i:
                done = True
                break

        easy_selection.draw()
        medium_selection.draw()
        hard_selection.draw()

        easy_img.draw()
        medium_img.draw()
        hard_img.draw()
        exit_button.draw()
        pygame.display.flip()
        Timer.update()


def load_game(difficulty: Difficulties):
    global player_count
    gen = script_generator(difficulty=difficulty)
    exit_button = basic_button("Images/Objects/Mid_Game/exit_button", position=[3,3], width_height=[10, 5])
    health_bar_p1 = health_bar("Images/Objects/Mid_Game/health_bar", [10,90], list(player_sprite_group)[0])
    health_bar_p2 = health_bar("Images/Objects/Mid_Game/health_bar", [70,90], list(player_sprite_group)[1] if len(player_sprite_group) > 1 else list(player_sprite_group)[0])
    death_tally = 0

    for i in player_sprite_group:
        i.set_alive(True)
        i.health = i.max_health

    done = False

    while not done:
        print("A")
        pygame.display.set_caption(f"Space Defenders -- {1 / Timer.get_last_frame_time_s()}")
        if exit_button.check_click():
            break
        screen.fill((0, 0, 0))

        # --- Main event loop
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                for sprite in player_sprite_group:
                    sprite.update_position(event)



        gen.update_script()

        for sprite in player_sprite_group:
            sprite.update()

        exit_button.draw()

        if len(player_sprite_group) > 1:
            health_bar_p2.draw()

        health_bar_p1.draw()

        for i in player_sprite_group:
            if i.health <= 0:
                i.alive = False
                i.set_alive(False)
                if i.player_number == 1 and health_bar_p1.visible:
                    health_bar_p1.visible = False
                    death_tally += 1
                elif i.player_number == 2 and health_bar_p2.visible:
                    health_bar_p2.visible = False
                    death_tally += 1


                if death_tally == len(player_sprite_group):

                    done = True
                    break

        print(len(player_sprite_group))


        pygame.display.flip()
        Timer.update()
