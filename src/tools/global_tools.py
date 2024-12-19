def toggle_group_visibility(group, state):
    for sprite in group:
        sprite.visible = state

def draw_choice_screen(class_name, attribute_name, button_yes,
        button_no, background_surface, events, screen, execute_drawing):

    setattr(class_name, attribute_name, True)
    screen.blit(background_surface, (100, 100))

    button_yes.update(events)
    button_no.update(events)

    execute_drawing()