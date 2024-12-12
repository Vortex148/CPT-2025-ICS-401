import pygame
from src.common_variables import *
from src.BaseClasses.button_classes import Clickability, basic_button

pygame.init()

# Creating the visibility function globally so it can be accessed in each class. It is like a switch.
def visibility(target):
   target.visible = not target.visible

# Defining a class for "clickability" to assign click detection to all instances of it
class Menu:
   def __init__(self, screen):
       self.screen = screen


       # Loading and sizing the image for the menu button
       menu_image = pygame.image.load("images/buttons_and_menus/Menu.png")
       menu_image = pygame.transform.scale(menu_image, (menu_button_width, menu_button_height))


       # Giving the menu button "clickability" attributes. The "execute" parameter runs the
       # visibility function. Using lambda allows us to use specific values from this class
       # in the clickability class by making the function "anonymous".
       self.menu_sprite = Clickability(
           menu_image,
           screen_width - (0.0225 * screen_width),
           screen_height/7.2,
           lambda: visibility(self.rules_sprite)
       )

       # Loading the rules menu and sizing it.
       rules_image = pygame.image.load("images/buttons_and_menus/Rules.png")
       rules_image = pygame.transform.scale(rules_image, (rules_width, rules_height))
       self.rules_sprite = Clickability(
           rules_image,
           screen_width/2,
           screen_height/2,
           None
       )

       # Starting with the rules menu invisible.
       self.rules_sprite.visible = False

       # Loading, sizing and giving clickability to the close button
       close_button_image = pygame.image.load("images/buttons_and_menus/Close.png")
       close_button_image = pygame.transform.scale(close_button_image, (close_button_width, close_button_height))


       self.close_button_sprite = Clickability(
           close_button_image,
           screen_width / 2 + (rules_width / 2) - (close_button_width / 2),
           (screen_height - rules_height) / 2 + (close_button_height / 2),
           lambda: visibility(self.rules_sprite))


   # Checking if either of the buttons have been clicked in each frame.
   def update(self, events):
       self.menu_sprite.check_click(events)

       if self.rules_sprite.visible:
           self.close_button_sprite.check_click(events)


   # The menu button is always drawn. If the rules are visible they are drawn as well
   # as the close button. The loop resets and checks for clicks on the close button.
   def draw(self):
       self.menu_sprite.draw()
       if self.rules_sprite.visible:
           self.rules_sprite.draw()
           self.close_button_sprite.draw()

# Creating the class for buttons that represents one player or two player game modes.
class player_mode_choice(basic_button):
    def __init__(self, x, y, text, screen, width=10, height=5, color=YELLOW):
        super().__init__(x, y, text, screen=screen, width=width, height=height, color=color)


    def get_clicked(self, events):
        return super().return_bool_val(events)
