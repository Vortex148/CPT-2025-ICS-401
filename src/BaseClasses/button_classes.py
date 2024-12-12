from stat import FILE_ATTRIBUTE_ARCHIVE

import pygame

from src.Tools.unit_handler import *
from src.common_variables import *

class Clickability(swth_sprite):
    # The "execute" parameter allows the import of functions from other classes and
    # runs them when the mouse click is in rectangle bounding the image.

    def __init__(self, sprite_image, x, y, execute_click=None, hover_text=None, hover_surface=None):
       super().__init__(sprite_image)
       self.image = sprite_image
       self.rect = self.image.get_rect()
       self.rect.center = (x, y)

       self.execute_click = execute_click
       self.visible = True
       self.hovering = False
       self.hover_text = hover_text
       self.hover_surface = hover_surface

       super().update_position([x, y])

       self.font = pygame.font.SysFont("Courier New", 16, True, False)


    # Checking if the sprite was clicked
    def check_click(self, events):
       # Looping through each event in pygame and triggering the desired function when the mouse button is released.
       for event in events:
           if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
               # Allowing self.execute to be none by only running the function when it has a value.
               if self.execute_click:
                   self.execute_click()


    def return_bool_val(self, events):
       print(self.rect)
       # Looping through each event in pygame and triggering the desired function when the mouse button is released.
       for event in events:
           if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
                # Allowing self.execute to be none by only running the function when it has a value.
                    return True
       return False

    def check_hover(self):
        mouse_position = pygame.mouse.get_pos()
        self.hovering = super().rect.collidepoint(mouse_position)
    # Drawing the sprite if it is set to visible
    def draw(self):
        super().draw()
           # screen.blit(self.image, self.rect.topleft)


           # if self.hovering:
           #     hover_rect = self.rect.copy()
           #     hover_rect.x += 30
           #     hover_rect.width = generate_relative_value_2d(10)
           #     hover_rect.height = generate_relative_value_2d(10)
           #
           #     pygame.draw.rect(screen, GRAY, hover_rect)
           #
           #     if self.hover_text:
           #         text = self.font.render(self.hover_text, True, WHITE)
           #         text_rect = text.get_rect()
           #         super().
           #         if self.hover_surface:
           #             self.hover_surface.blit(text, text_rect)
           #         else:
           #             screen.blit(text, text_rect)

class basic_button():
   def __init__(self, x, y, text, screen, execute_click = None, width=160, height=80, color=YELLOW):
       self.screen = screen
       self.x = x
       self.y = y
       self.text = text
       self.color = None
       self.visible = True
       self.width = generate_relative_value(width, screen.get_size()[0])
       self.height = generate_relative_value(height, screen.get_size()[0])
       self.execute_click = execute_click
       self.font = pygame.font.SysFont('Courier New', 15, True, False)
       self.text_box = self.font.render(self.text, True, BLACK)
       self.button = pygame.Surface((self.width, self.height))
       self.button.fill(color)

       # Positioning the text in the center of the button
       self.text_rect = self.text_box.get_rect()
       self.text_width = self.text_rect.width
       self.text_height = self.text_rect.height
       self.text_x = (self.text_width - self.width)/2  # (self length - total)/2
       self.text_y = (self.text_height - self.height)/2  # (self height - total)/2
       self.button.blit(self.text_box, (self.text_x, self.text_y))
       self.button_sprite = Clickability(self.button, x, y, execute_click)

   def update(self, events):
       if self.visible:
            self.button_sprite.check_click(events)

   def clicked(self, events):
       return self.button_sprite.check_click(events)

   def bool_val(self, events):

       return self.button_sprite.return_bool_val(events)

   def draw(self):
       if self.visible:
            self.button_sprite.draw()