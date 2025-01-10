# Flipping the visibility of each sprite in the desired group
# Function creates an instance of the defined class.
# Used to create instances of each item --> allows

from src.common_variables import *

# Getting the path to any file. Quickens refactoring
def get_path(file_name, directory, extension):
    file = f"{file_name}."+f"{extension}"
    return os.path.join(directory, file)

# Creates an instance of the given class
def create_instance(class_type, *args):
    return class_type(*args)

# Changes the visibility attribute of each item in a group
def toggle_group_visibility(group, state, upgrades_group=None):
    for sprite in group:
        sprite.visible = state

        # Ensuring buttons can't be clicked if they are invisible.
        # Because the upgrade sprites are defined differently than
        # ships or weapons, they must also be referenced as such.
        if upgrades_group:
            sprite.set_actionable(state)
        else:
            sprite.item_sprite.set_actionable(state)

# Drawing function for generic yes/no buttons.
def draw_choice_buttons(button_yes, button_no):
    button_yes.draw()
    button_no.draw()

# Drawing a menu with yes and no choices.
def draw_choice_screen(button_yes,
        button_no, background_surface):

    background_surface.draw()

    # Checking for clicks on the yes and no buttons
    button_yes.check_click()
    button_no.check_click()

    # Function parameter executed, usually for drawing the group
    # of objects associated with the particular yes/no screen.
    draw_choice_buttons(button_yes, button_no)
