# from src.Tools.global_tools import draw_default_group
from src.Tools.global_tools import get_path
from src.Tools.global_tools import toggle_group_visibility
from src.Tools.purchase_functions import *
from src.base_classes.revised_buttons import BASIC_BUTTON
from src.base_classes.swth import swth_object
from src.image_paths import *
# The game engine must be initialized to access font styles and other pygame properties
pygame.init()

black_background = swth_object(black_background_path, size=(35, 35), position=(50, 50))

# Class for the item shop structure
class open_and_background():
   # Parameters written for each of the main item groups of the shop. In the main game loop, the instances
   # of each of these groups are accessible as arguments for this class. It is not possible to do so here
   # because the instances rely on the class, and the class the instances. For this reason, it is outsourced
   # to the main game loop to prevent circular import.
   def __init__(self, ships_group, weapons_group, upgrades_group, buttons_group):
       self.item_shop_visible = False
       self.ships_group = ships_group
       self.weapons_group = weapons_group
       self.upgrades_group = upgrades_group
       self.buttons_group = buttons_group

       # Open button for shop
       self.open_button_sprite = BASIC_BUTTON(
           open_button_path,
           (80, 10),
           (10, 10),
           execute_click=lambda: self.open_shop()
       )

       # Item shop background
       self.background_sprite = swth_object(
           shop_background_path,
           (21, 15),
           (58, 70),
       )

       # Close button for shop
       self.close_button_sprite = BASIC_BUTTON(
           close_button_path,
           (73, 20),
           (5, 7),
           execute_click=lambda: self.close_shop()
       )

       # Defaulting the shop to be invisible so it is not drawn unless opened.
       self.background_sprite.visible = False

   # Makes all game shop objects visible (triggers drawing)
   def open_shop(self):
      self.background_sprite.visible = True
      self.close_button_sprite.visible = True
      toggle_group_visibility(self.ships_group, True)
      toggle_group_visibility(self.buttons_group, True, True)

   # Shop made invisible
   def close_shop(self):
       self.background_sprite.visible = False
       self.close_button_sprite.visible = False
       toggle_group_visibility(self.ships_group, False)
       toggle_group_visibility(self.upgrades_group, False)
       toggle_group_visibility(self.weapons_group, False)
       toggle_group_visibility(self.buttons_group, False, True)

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

# Blueprint for shop items. Must inherit from sprite for grouping
class shop_items(pygame.sprite.Sprite):
   item_number = 0
   current_item = None
   purchase_background_visibility = False
   equipping_background_visibility = False

   def __init__(self, screen, name, path, price, item_info, hover_image=None):
       super().__init__()
       shop_items.item_number += 1 # Incrementing the item number for positioning

       # Default values for purchased and equipped state.
       self.item_purchased = False
       self.equipped = False
       self.hover_image = hover_image

       # Defining instance variables from parameters
       self.item_type = type(self).__name__ # Returns the name of the child class to distinguish purchase functions in the purchase functions file.
       self.path = path
       self.item_number = shop_items.item_number
       self.screen = screen
       self.name = name
       self.price = price
       self.item_info = item_info
       self.item_image_path = path
       self.visible = False
       self.pos_x = 24
       self.pos_y = 22

       # Positioning each item by its number
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

       if self.item_type == "upgrades":
           self.item_sprite = BASIC_BUTTON(
               self.item_image_path,
               (self.pos_x, self.pos_y,),
               (22, 22),
               execute_click = lambda: self.equip(),
               execute_hover = lambda: self.draw_hover_image()
           )

       # Calls basic item_click function if item has not been purchased.
       # Will call equipping code if a purchased item is selected again.
       elif self.item_type == "ships" or "weapons":
           self.item_sprite = BASIC_BUTTON(
               self.item_image_path,
               (self.pos_x, self.pos_y),
               (22, 22),
               execute_click = lambda: self.item_click() if not self.item_purchased else self.equip(), # Calls basic item_click function if item has not been purchased. Will call equipping code if a purchased item is selected again.
               execute_hover = lambda: self.draw_hover_image()
           )

   def draw_hover_image(self):
       global black_background
       black_background.draw()
       self.hover_image.draw()

   # In progress
   def equip(self):
       shop_items.current_item = self

       if game.player2 != None:
           players_list = [game.player1, game.player2]
       elif game.player2 == None:
           players_list = [game.player1]

       # add new text for purchase background
       self.equip_confirm = BASIC_BUTTON(equip_yes_path, (50, 50), (10, 10), execute_click = lambda: equip(self,
                lambda: close_yes_no(shop_items, "equipping_background_visibility"), self.item_type, self.item_info,
                                     self.path, self.name, players_list),
                                               )

       self.equip_deny = BASIC_BUTTON(equip_no_path, (50, 65), (10, 10), execute_click=lambda: close_yes_no(shop_items,
                            "equipping_background_visibility"))

       shop_items.equipping_background_visibility = True

   # Defines what happens when an item is clicked
   def item_click(self):
       # Getting the name of the child class for handling in the purchase function
       shop_items.current_item = self
       print("running item_click")

       # Importing the players now prevents stale attribute values.

       if game.player2 != None:
           players_list = [game.player1, game.player2]
       elif game.player2 == None:
           players_list = [game.player1]

       # TODo: note to self for tomorrow: buttons working but need to get them to update (likely needs class reference)
       # TOdo; shop items.purchase button yes etc..
       # Calling the "yes" function when the confirm button is clicked
       self.purchase_button_yes = BASIC_BUTTON(equip_yes_path, (50, 50),
                    (10, 10), execute_click=lambda: purchase(self.price,
                                self.name, players_list, self, shop_items)
                                )

       self.purchase_button_no = BASIC_BUTTON(equip_no_path, (50, 65),
                    (10, 10), execute_click=lambda: no(shop_items))


       self.purchase_background_surface = swth_object(purchase_background_path, (36, 40), (35, 35))
       self.equipping_background_surface = swth_object(equipping_background_path, (36, 40), (35, 35))

       # Telling the program it can draw the purchase screen
       shop_items.purchase_background_visibility = True

   # Following two methods in progress- for equipping/double purchase prevention code
   def draw_purchased(self):
       if self.item_purchased and not self.equipped:
           equipping_or_purchase(self.item_sprite, self.screen, "purchase", [self.pos_x, self.pos_y])

   def draw_equipped(self):
       if self.equipped:
           equipping_or_purchase(self.item_sprite, self.screen, "equipped", [self.pos_x, self.pos_y])

   # Checking for clicks each frame
   def update(self, events):
       if self.visible:
           self.item_sprite.check_click()
           self.item_sprite.check_hover()
           self.draw_equipped()
           self.draw_purchased()

       if shop_items.purchase_background_visibility or shop_items.equipping_background_visibility:
           self.item_sprite.set_actionable(False)
       else:
           self.item_sprite.set_actionable(True)

   def draw(self):
       if self.visible:
           self.item_sprite.draw()

# Defining child classes of shop items for each category.
# Category specific attributes like damage and velocity are added
# In the class constructor.
class weapons(shop_items):
   def __init__(self, screen, name, path, price, item_info, hover_image):
       super().__init__(screen, name, path, price, item_info, hover_image)
       self.damage = item_info.get("Damage")
       self.velocity = item_info.get("Velocity")

# Blueprint for upgrades
class ships(shop_items):
    def __init__(self, screen, name, path, price, item_info, hover_image):
       super().__init__(screen, name, path, price, item_info, hover_image)
       self.health = item_info.get("Health")
       self.velocity = item_info.get("Velocity")

# Blueprint for upgrades
class upgrades(shop_items):
    def __init__(self, screen, name, path, price, item_info, hover_image):
       super().__init__(screen, name, path, price, item_info, hover_image)
       # Defaulting to 0 if no parameter is given. This avoids needing to
       # differentiate between the types of upgrades. All upgrades update all
       # attributes but only update the selected one in a meaningful way (i.e.
       # not with 0).
       self.health_increase = item_info.get("Health Increase", 0)
       self.velocity_increase = item_info.get("Velocity Increase", 0)
       self.cooldown_decrease = item_info.get("Cooldown Decrease", 0)
