import pygame
import json
from src.common_variables import *
from src.base_classes.button_classes import Clickability, basic_button
from src.base_classes.game_state import game
from src.base_classes.player import player
from src.tools.json_handler import get_json_path, update_json, read_json
from src.tools.purchase_functions import *

# The game engine must be initialized to define font styles
pygame.init()

# When an item is purchased from the item shop, the players must be recreated
# to display the changes in real time.

# Class for the item shop structure
class open_and_background:
   def __init__(self, screen):
       self.item_shop_visible = False
       self.screen = screen
       open_button = pygame.image.load("images/buttons_and_menus/shopping_cart.png")
       open_button = pygame.transform.scale(open_button, (menu_button_width, menu_button_height))

       # Creating a clickable open button tht draws the item shop when opened.
       self.open_button_sprite = Clickability(
           open_button,
           700,
           100,
           lambda: self.visibility("background_sprite")
       )

       shop_background = pygame.image.load("images/buttons_and_menus/shop_background.png")
       shop_background = pygame.transform.scale(shop_background, (600, 600))
       self.background_sprite = Clickability(
           shop_background,
           400,
           screen_height/2,
           None
       )


       self.background_sprite.visible = False


       close_button_image = pygame.image.load("images/buttons_and_menus/Close.png")
       close_button_image = pygame.transform.scale(close_button_image, (close_button_width, close_button_height))

       # Close button for the item shop
       self.close_button_sprite = Clickability(
           close_button_image,
           550,
           70,
           lambda: self.visibility("background_sprite", "item_shop_visible")
       )

   # Toggles visibility
   def visibility(self, target_attr, target_state=None):
       target = getattr(self, target_attr)
       target.visible = not target.visible

       if target_state:
           target_2 = getattr(self, target_state)
           target_2 = not target_2
           print(target_2)

   # Checking if the buttons were clicked each frame.
   def update(self, events):
       self.open_button_sprite.check_click(events)

       if self.background_sprite.visible:
           self.close_button_sprite.check_click(events)
           self.item_shop_visible = True

   # Drawing the close button if the background is visible.
   def draw(self):
       self.open_button_sprite.draw(self.screen)

       if self.background_sprite.visible:
           self.background_sprite.draw(self.screen)
           self.close_button_sprite.draw(self.screen)

# Needs to be refactored with "basic button" parent class
class item_category_button(basic_button):
   def __init__(self, x, y, text, execute_click, screen, width=160, height=80, color=YELLOW):
       super().__init__(x, y, text, execute_click, screen, 60, 20, color)

class shop_items(pygame.sprite.Sprite):
   item_number = 0
   purchase_background_visibility = False
   current_item = None
   purchase_button_yes = None
   purchase_button_no = None

   def __init__(self, screen, name, path, price, item_info):
       super().__init__()
       shop_items.item_number += 1
       self.path = path
       self.item_number = shop_items.item_number
       self.screen = screen
       self.name = name
       self.price = price
       self.item_info = item_info
       self.purchase_background_surface = pygame.Surface((200, 200))
       self.purchase_background_surface.fill(BLUE)
       purchase_rect = self.purchase_background_surface.get_rect()
       self.purchase_rect_x = purchase_rect.x
       self.purchase_rect_y = purchase_rect.y
       self.purchase_rect_width = purchase_rect.width
       self.purchase_rect_height = purchase_rect.height

       item_image = pygame.image.load(path)
       item_image = pygame.transform.scale(item_image, (item_width, item_height))

       pos_x = 330
       pos_y = 180

       self.visible = False

       # Assigning each item a number and positioning it based on that.
       # The count is reset after 4 because position is tied to the count
       # by multiplication
       if shop_items.item_number > 4:
           shop_items.item_number = 1

       if self.item_number == 1:
           pos_x = 330
           pos_y = 180
       elif self.item_number == 2:
           pos_x = 510
           pos_y = 180
       elif self.item_number == 3:
           pos_x = 330
           pos_y = 420
       elif self.item_number == 4:
           pos_x = 510
           pos_y = 420

       # Details of the object stored in hover_text so it is displayed when the item is hovered over.
       hover_text = f"Name: {self.name}\nPrice: ${self.price}\n"+\
                    "\n".join(f"{key.title()}: {value}" for key, value in item_info.items())

       self.item_sprite = Clickability(
           item_image,
           pos_x,
           pos_y,
           lambda: self.item_click(),
           hover_text,
           self.purchase_background_surface # surface to blit text onto
       )

   def item_click(self):
       x = (self.purchase_rect_x + self.purchase_rect_width/2)
       y = self.purchase_rect_y

       # Getting the name of the child class for handling in the purchase function
       item_type = type(self).__name__
       shop_items.current_item = self

       # Importing the players now prevents stale attribute values.
       if game.player2 != None:
           players_list = [game.player1, game.player2]
       elif game.player2 == None:
           players_list = [game.player1]

       # Calling the "yes" function when the confirm button is clicked
       shop_items.purchase_button_yes = basic_button(x, y, "Yes", lambda: yes(self.price,
                                self.name, self.item_info, item_type,
                                self.purchase_background_surface, players_list, self.path),
                                self.screen, 60, 30)

       shop_items.purchase_button_no = basic_button(x, y + 50, "No", lambda: no(), self.screen, 60, 30)

       # Telling the program it can draw the purchase screen
       shop_items.purchase_background_visibility = True

       print(item_type)

   # Checking for clicks each frame
   def update(self, events):
       if self.visible:
           self.item_sprite.check_click(events)
           self.item_sprite.check_hover()

   def draw(self):
       if self.visible:
           self.item_sprite.draw(self.screen)

# Defining child classes of shop items for each category.
# Category specific attributes like damage and velocity are added.
class weapons(shop_items):
   def __init__(self, screen, path, price, item_info, name):
       super().__init__(screen, name, path, price, item_info)
       self.damage = item_info.get("Damage")
       self.velocity = item_info.get("Velocity")

class ships(shop_items):
   def __init__(self, screen, path, price, item_info, name):
       super().__init__(screen, name, path, price, item_info)
       self.health = item_info.get("Health")
       self.velocity = item_info.get("Velocity")

class upgrades(shop_items):
   def __init__(self, screen , path, price, item_info, name):
       super().__init__(screen, name, path, price, item_info)
       # Defaulting to 0 if no parameter is given. This avoids redundant definition.
       self.health_increase = item_info.get("Health Increase", 0)
       self.velocity_increase = item_info.get("Velocity Increase", 0)
       self.cooldown_decrease = item_info.get("Cooldown Decrease", 0)
