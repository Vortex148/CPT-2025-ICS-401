import pygame

from src.base_classes.revised_buttons import BASIC_BUTTON
from src.base_classes.swth import swth_object
from src.common_variables import *
from src.base_classes.button_classes import Clickability, basic_button

pygame.init()

# Creating the visibility function globally so it can be accessed in each class. It is like a switch.
def visibility(target):
   target.visible = not target.visible

# Defining a class for "clickability" to assign click detection to all instances of it
class Menu:
   def __init__(self):
       # Menu Button
       menu_image_path = "images/buttons_and_menus/Menu.png"
       self.menu_sprite = BASIC_BUTTON(
           menu_image_path,
           (80, 25),
           (10, 10),
           execute_click=lambda: visibility(self.rules_sprite)
       )

       # Rules Button
       rules_image_path = "images/buttons_and_menus/Rules.png"
       self.rules_sprite = swth_object(
           rules_image_path,
           (21, 15),
           (58, 70)
       )

       # Starting with the rules menu invisible.
       self.rules_sprite.visible = False

   # Checking for button clicks
   def update(self):
       self.menu_sprite.check_click()

   # The open button is always drawn. The rules and close are only drawn if the button is clicked.
   def draw(self):
       self.menu_sprite.draw()

       if self.rules_sprite.visible:
           self.rules_sprite.draw()



