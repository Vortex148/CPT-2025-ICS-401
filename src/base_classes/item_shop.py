# from src.Tools.global_tools import draw_default_group
from src.Tools.global_tools import toggle_group_visibility
from src.base_classes.button_classes import Clickability, basic_button
from src.Tools.purchase_functions import *
from src.base_classes.revised_buttons import BASIC_BUTTON
from src.base_classes.swth import swth_sprite, swth_object

# The game engine must be initialized to access font styles and other pygame properties
pygame.init()

# Class for the item shop structure
class open_and_background():
   # Parameters written for each of the main item groups of the shop. In the main game loop, the instances
   # of each of these groups are accessible as arguments for this class. It is not possible to do so here
   # because the instances rely on the class, and the class the instances. For this reason, it is outsourced
   # to the main game loop to prevent circular import.
   def __init__(self, screen, ships_group, weapons_group, upgrades_group, buttons_group):
       self.item_shop_visible = False
       self.screen = screen

       self.ships_group = ships_group
       self.weapons_group = weapons_group
       self.upgrades_group = upgrades_group
       self.buttons_group = buttons_group

       open_button_path = "images/buttons_and_menus/shopping_cart.png"
       self.open_button_sprite = BASIC_BUTTON(
           open_button_path,
           (80, 10),
           (10, 10),
           execute_click=lambda: self.open_shop()
       )

       shop_background_path = "images/buttons_and_menus/shop_background.png"

       # Todo: background sprite should not be clickable. Works but could be far simpler as a basic sprite
       self.background_sprite = swth_object(
           shop_background_path,
           (10, 10),
           (80, 80),
       )

       # Defaulting the shop to be invisible so it is not drawn unless opened.
       self.background_sprite.visible = False

       close_button_path = "images/buttons_and_menus/Close.png"
       # See lambda function for description
       self.close_button_sprite = BASIC_BUTTON(
           close_button_path,
           (73, 20),
           (5, 7),
           execute_click=lambda: self.close_shop()
       )

   # Makes all game shop objects visible (triggers drawing in main game loop)
   def open_shop(self):
      self.background_sprite.visible = True
      self.close_button_sprite.visible = True
      toggle_group_visibility(self.buttons_group, True)
      toggle_group_visibility(self.ships_group, True)

   # Makes all game shop objects invisible
   def close_shop(self):
       self.background_sprite.visible = False
       self.close_button_sprite.visible = False
       toggle_group_visibility(self.ships_group, False)
       toggle_group_visibility(self.upgrades_group, False)
       toggle_group_visibility(self.weapons_group, False)
       toggle_group_visibility(self.buttons_group, False)

   # Checking if the buttons were clicked each frame.
   def update(self, events):
       if self.open_button_sprite.visible:
           self.open_button_sprite.check_click()

       if self.background_sprite.visible:
           self.close_button_sprite.check_click()
           self.item_shop_visible = True

   # Drawing the close button if the background is visible.The open button is always drawn.
   def draw(self):
       self.open_button_sprite.draw()

       if self.background_sprite.visible:
           self.background_sprite.draw()
           self.close_button_sprite.draw()

class shop_items(pygame.sprite.Sprite):
   item_number = 0
   purchase_background_visibility = False
   equipping_background_visibility = False
   current_item = None
   purchase_button_yes = None
   purchase_button_no = None
   equip_confirm = None
   equip_deny = None

   def __init__(self, screen, name, path, price, item_info):
       super().__init__()
       shop_items.item_number += 1 # Incrementing the item number for positioning

       # Default values for purchased and equipped state.
       self.item_purchased = False
       self.equipped = False

       # Defining instance variables from parameters
       self.item_type = type(self).__name__ # Returns the name of the child class to distinguish purchase functions in the purchase functions file.
       self.path = path
       self.item_number = shop_items.item_number
       self.screen = screen
       self.name = name
       self.price = price
       self.item_info = item_info

       # Defining the purchase menu for each item
       self.purchase_background_surface = pygame.Surface((200, 200))
       self.purchase_background_surface.fill(BLUE)
       purchase_rect = self.purchase_background_surface.get_rect()
       self.purchase_rect_x = purchase_rect.x
       self.purchase_rect_y = purchase_rect.y
       self.purchase_rect_width = purchase_rect.width
       self.purchase_rect_height = purchase_rect.height

       self.item_image_path = path

       self.visible = False

       # Assigning each item a number and positioning it based on that.
       # The count is reset after 4 because position is tied to the count
       # by multiplication
       if shop_items.item_number > 4:
           shop_items.item_number = 1

       if self.item_number == 1:
           self.pos_x = 24
           self.pos_y = 22
       elif self.item_number == 2:
           self.pos_x = 49
           self.pos_y = 22
       elif self.item_number == 3:
           self.pos_x = 24
           self.pos_y = 56
       elif self.item_number == 4:
           self.pos_x = 49
           self.pos_y = 56

       # Details of the object stored in hover_text so it is displayed when the item is hovered over.

       # hover_text = f"Name: {self.name}\nPrice: ${self.price}\n"+\
       #              "\n".join(f"{key.title()}: {value}" for key, value in item_info.items())

       #
       if self.item_type == "upgrades":
           self.item_sprite = BASIC_BUTTON(
               self.item_image_path,
               (self.pos_x, self.pos_y,),
               (22, 22),
               execute_click = lambda: self.equip(),
               execute_hover = None # self.purchase_background_surface.draw()
               # Calls basic item_click function if item has not been purchased.
               # Will call equipping code if a purchased item is selected again.
           )

       elif self.item_type == "ships" or "weapons":
           self.item_sprite = BASIC_BUTTON(
               self.item_image_path,
               (self.pos_x, self.pos_y),
               (22, 22),
               execute_click=lambda: self.item_click() if not self.item_purchased else self.equip(), # Calls basic item_click function if item has not been purchased. Will call equipping code if a purchased item is selected again.
               execute_hover= None # self.purchase_background_surface.draw()
           )

       self.selected_item = self.item_sprite

   # In progress
   def equip(self):
       shop_items.current_item = self
       x = (self.purchase_rect_x + self.purchase_rect_width / 2)
       y = self.purchase_rect_y

       if game.player2 != None:
           players_list = [game.player1, game.player2]
       elif game.player2 == None:
           players_list = [game.player1]

       shop_items.equipping_background_visibility = True
       # add new text for purchase background
       shop_items.equip_confirm = basic_button(x, y, "Yes", lambda: equip(self,
                lambda: close_yes_no(shop_items, "equipping_background_visibility"), self.item_type, self.item_info,
                                     self.path, self.name, players_list),
                self.screen, 60, 30, RED)

       shop_items.equip_deny = basic_button(x, y + 50, "No", lambda: close_yes_no(shop_items,
                            "equipping_background_visibility"),
                            self.screen, 60, 30, RED)

   # Defines what happens when an item is clicked
   def item_click(self):
       x = (self.purchase_rect_x + self.purchase_rect_width/2)
       y = self.purchase_rect_y

       # Getting the name of the child class for handling in the purchase function
       shop_items.current_item = self

       # Importing the players now prevents stale attribute values.

       if game.player2 != None:
           players_list = [game.player1, game.player2]
       elif game.player2 == None:
           players_list = [game.player1]

       # Calling the "yes" function when the confirm button is clicked
       shop_items.purchase_button_yes = basic_button(x, y, "Yes", lambda: purchase(self.price,
                                self.name, players_list, self,
                                self.purchase_background_surface, shop_items),
                                self.screen, 60, 30)

       shop_items.purchase_button_no = basic_button(x, y + 50, "No", lambda: no(shop_items), self.screen, 60, 30)

       # Telling the program it can draw the purchase screen
       shop_items.purchase_background_visibility = True

   # Following two methods in progress- for equipping/double purchase prevention code
   def draw_purchased(self):
       if self.item_purchased and not self.equipped:
           equipping_or_purchase(self.item_image, self.screen, "purchase", [self.pos_x, self.pos_y])

   def draw_equipped(self):
       if self.equipped:
           equipping_or_purchase(self.item_image, self.screen, "equipped", [self.pos_x, self.pos_y])

   # Checking for clicks each frame
   def update(self, events):
       if self.visible:
           self.item_sprite.check_click()
           self.item_sprite.check_hover()
           self.draw_equipped()
           self.draw_purchased()

   def draw(self):
       if self.visible:
           self.item_sprite.draw()

# Defining child classes of shop items for each category.
# Category specific attributes like damage and velocity are added
# In the class constructor.
class weapons(shop_items):
   def __init__(self, screen, name, path, price, item_info):
       super().__init__(screen, name, path, price, item_info)
       self.damage = item_info.get("Damage")
       self.velocity = item_info.get("Velocity")

# Blueprint for upgrades
class ships(shop_items):
    def __init__(self, screen, name, path, price, item_info):
       super().__init__(screen, name, path, price, item_info)
       self.health = item_info.get("Health")
       self.velocity = item_info.get("Velocity")

# Blueprint for upgrades
class upgrades(shop_items):
    def __init__(self, screen, name, path, price, item_info):
       super().__init__(screen, name, path, price, item_info)
       # Defaulting to 0 if no parameter is given. This avoids needing to
       # differentiate between the types of upgrades. All upgrades update all
       # attributes but only update the selected one in a meaningful way (i.e.
       # not with 0).
       self.health_increase = item_info.get("Health Increase", 0)
       self.velocity_increase = item_info.get("Velocity Increase", 0)
       self.cooldown_decrease = item_info.get("Cooldown Decrease", 0)
