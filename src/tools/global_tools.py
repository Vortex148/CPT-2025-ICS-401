# Flipping the visibility of each sprite in the desired group
# Function creates an instance of the defined class.
# Used to create instances of each item --> allows

from src.common_variables import *

def get_path(file_name, directory, extension):
    file = f"{file_name}."+f"{extension}"
    return os.path.join(directory, file)

def get_json_path(file_name):
    return os.path.join(json_directory, f"{file_name}.json")

def get_image_path(file_name):
    return os.path.join(images_directory, f"{file_name}.png")

def create_instance(class_type, *args):
    return class_type(*args)

def toggle_group_visibility(group, state, upgrades_group=None):
    for sprite in group:
        sprite.visible = state
        if upgrades_group:
            sprite.set_actionable(state)
        else:
            sprite.item_sprite.set_actionable(state)


# Drawing a menu with yes and no choices.
def draw_choice_screen(class_name, attribute_name, button_yes,
        button_no, background_surface, screen, execute_drawing):

    # Making the group visible (activates drawing within that class)
    setattr(class_name, attribute_name, True)
    screen.blit(background_surface, (100, 100))

    # Checking for clicks on the yes and no buttons
    button_yes.update()
    button_no.update()

    # Function parameter executed, usually for drawing the group
    # of objects associated with the particular yes/no screen.
    execute_drawing()
