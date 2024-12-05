import pygame
from src.common_variables import *
from src.base_classes.menu import Clickability


item_counter = 0


# Creating the visibility function globally so it can be accessed in each class. It is like a switch.
def visibility(target1):
   target1.visible = not target1.visible

def place_holder_item_click(screen):
    pygame.draw.rect(screen, BLUE, [100, 100, 500, 500])
    purchase_button_yes = "p"
    purchase_button_no = "p"

class open_and_background:
   def __init__(self, screen):
       self.screen = screen
       open_button = pygame.image.load("images/buttons_and_menus/shopping_cart.png")
       open_button = pygame.transform.scale(open_button, (menu_button_width, menu_button_height))


       self.open_button_sprite = Clickability(
           open_button,
           700,
           100,
           lambda: visibility(self.background_sprite)
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


       self.close_button_sprite = Clickability(
           close_button_image,
           550,
           70,
           lambda: visibility(self.background_sprite)
       ) #add code for whole item shop


   def update(self, events):
       self.open_button_sprite.check_click(events)

       if self.background_sprite.visible:
           self.close_button_sprite.check_click(events)


   def draw(self):
       self.open_button_sprite.draw(self.screen)

       if self.background_sprite.visible:
           self.background_sprite.draw(self.screen)
           self.close_button_sprite.draw(self.screen)

class item_category_button(pygame.sprite.Sprite):
   def __init__(self, x, y, text, execute_click, screen):
       super().__init__()
       self.screen = screen
       self.x = x
       self.y = y
       self.visible = True
       self.execute_click = execute_click
       self.font = pygame.font.SysFont('Courier New', 10, True, False)
       self.text_box = self.font.render(text, True, BLACK)
       self.category_button = pygame.Surface((60, 20))
       self.category_button.fill(GOLD)
       self.category_button.blit(self.text_box, (12, 5))
       self.category_button_sprite = Clickability(self.category_button, x, y, execute_click)


   def update(self, events):
       if self.visible:
           self.category_button_sprite.check_click(events)

   def draw(self):
       self.category_button_sprite.draw(self.screen)

class shop_items(pygame.sprite.Sprite):
   item_number = 0
   def __init__(self, screen, name, path, price, item_info):
       super().__init__()
       shop_items.item_number += 1
       self.item_number = shop_items.item_number
       self.screen = screen
       self.name = name
       self.price = price
       self.item_info = item_info


       item_image = pygame.image.load(path)
       item_image = pygame.transform.scale(item_image, (item_width, item_height))
       self.visible = False

       pos_x = 330
       pos_y = 180

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

       hover_text = f"Name: {self.name}\nPrice: ${self.price}\n"+\
                    "\n".join(f"{key.title()}: {value}" for key, value in item_info.items())

       self.item_sprite = Clickability(
           item_image,
           pos_x,
           pos_y,
           lambda: place_holder_item_click(screen), # to be replaced with purchase function
           hover_text
       )

   def update(self, events):
       if self.visible:
           self.item_sprite.check_click(events)
           self.item_sprite.check_hover()

   def draw(self):
       if self.visible:
           self.item_sprite.draw(self.screen)

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
       self.health_increase = item_info.get("Health Increase", 0)
       self.velocity_increase = item_info.get("Velocity Increase", 0)
       self.cooldown_decrease = item_info.get("Cooldown Decrease", 0)
