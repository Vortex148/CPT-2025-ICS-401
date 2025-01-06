# Flipping the visibility of each sprite in the desired group

# Function creates an instance of the defined class.
# Used to create instances of each item --> allows
def create_instance(class_type, *args):
    return class_type(*args)

def toggle_group_visibility(group, state):
    for sprite in group:
        sprite.visible = state

# Drawing a menu with yes and no choices.
def draw_choice_screen(class_name, attribute_name, button_yes,
        button_no, background_surface, events, screen, execute_drawing):

    # Making the group visible (activates drawing within that class)
    setattr(class_name, attribute_name, True)
    screen.blit(background_surface, (100, 100))

    # Checking for clicks on the yes and no buttons
    button_yes.update(events)
    button_no.update(events)

    # Function parameter executed, usually for drawing the group
    # of objects associated with the particular yes/no screen.
    execute_drawing()
