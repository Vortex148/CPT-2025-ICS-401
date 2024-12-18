# from src.Tools.global_tools import draw_default_group
from src.Tools.global_tools import toggle_group_visibility
from src.base_classes.button_classes import Clickability, basic_button
from src.Tools.purchase_functions import *

# The game engine must be initialized to define font styles
pygame.init()

def visibility(class_name, *args):
    for attribute in args:
        target = getattr(class_name, attribute)
        desired_toggle = not target
        setattr(class_name, attribute, desired_toggle)

# Class for the item shop structure
class open_and_background:
   def __init__(self, screen, ships_group, weapons_group, upgrades_group, buttons_group):
       self.item_shop_visible = False
       self.screen = screen
       self.ships_group = ships_group
       self.weapons_group = weapons_group
       self.upgrades_group = upgrades_group
       self.buttons_group = buttons_group
       open_button = pygame.image.load("images/buttons_and_menus/shopping_cart.png")
       open_button = pygame.transform.scale(open_button, (menu_button_width, menu_button_height))

       # Creating a clickable open button tht draws the item shop when opened.
       self.open_button_sprite = Clickability(
           open_button,
           700,
           100,
           lambda: self.open_shop()
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
           lambda: self.close_shop()
       )

   def open_shop(self):
      self.background_sprite.visible = True
      self.close_button_sprite.visible = True
      toggle_group_visibility(self.buttons_group, True)
      toggle_group_visibility(self.ships_group, True)

   def close_shop(self):
       self.background_sprite.visible = False
       self.close_button_sprite.visible = False

       toggle_group_visibility(self.ships_group, False)
       toggle_group_visibility(self.upgrades_group, False)
       toggle_group_visibility(self.weapons_group, False)
       toggle_group_visibility(self.buttons_group, False)
   def update_item_shop_visibility_state(self):
       return self.item_shop_visible

   # Checking if the buttons were clicked each frame.
   def update(self, events):
       if self.open_button_sprite.visible:
           self.open_button_sprite.check_click(events)

       if self.background_sprite.visible:
           self.close_button_sprite.check_click(events)
           self.item_shop_visible = True

       self.item_shop_visible = self.update_item_shop_visibility_state()

   # Drawing the close button if the background is visible.
   def draw(self):
       self.open_button_sprite.draw(self.screen)

       if self.background_sprite.visible:
           self.background_sprite.draw(self.screen)
           self.close_button_sprite.draw(self.screen)

class item_category_button(basic_button):
   def __init__(self, x, y, text, execute_click, screen, width=160, height=80, color=YELLOW):
       super().__init__(x, y, text, execute_click, screen, 60, 20, color)

class shop_items(pygame.sprite.Sprite):
   item_number = 0
   purchase_background_visibility = False
   equipping_visibility = False
   current_item = None
   purchase_button_yes = None
   purchase_button_no = None
   equip_confirm = None
   equip_deny = None

   def __init__(self, screen, name, path, price, item_info):
       super().__init__()
       shop_items.item_number += 1
       self.item_purchased = False
       self.equipped = False
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
           lambda: self.item_click() if not self.item_purchased
           else self.equip(),
           hover_text,
           self.purchase_background_surface # surface to blit text onto
       )

       self.selected_item = self.item_sprite

   def equip(self):
       x = (self.purchase_rect_x + self.purchase_rect_width / 2)
       y = self.purchase_rect_y
       shop_items.purchase_background_visibility = True
       shop_items.equip_confirm = basic_button(x, y, "Yes", lambda: equip(),
                                                     self.screen, 60, 30)

       shop_items.equip_deny = basic_button(x, y + 50, "No", lambda: close(shop_items), self.screen, 60, 30)

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
                                self.purchase_background_surface, players_list,
                                self.path, self.selected_item, shop_items, self),
                                self.screen, 60, 30)

       shop_items.purchase_button_no = basic_button(x, y + 50, "No", lambda: no(shop_items), self.screen, 60, 30)

       # Telling the program it can draw the purchase screen
       shop_items.purchase_background_visibility = True

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
