import pygame
from src.common_variables import *

# Todo: Needs to be refactored
class Clickability(pygame.sprite.Sprite):
    # The "execute_click" parameter takes a function as a parameter and runs it in the
    # "check_click" method. "execute_click" argument functions must be passed in "lamda" (used in all instance of this class).
   def __init__(self, sprite_image, x, y, execute_click=None, hover_text=None, hover_surface=None):
       super().__init__()
       self.image = sprite_image
       self.rect = self.image.get_rect()
       self.rect.center = (x, y)
       self.execute_click = execute_click
       self.visible = True
       self.hovering = False
       self.hover_text = hover_text
       self.hover_surface = hover_surface

       self.font = pygame.font.SysFont("Courier New", 16, True, False)

    # Checking if the sprite was clicked
   def check_click(self, events):
       # Looping through each event in pygame and triggering the desired function when the mouse button is released.
       for event in events:
           if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
               # Allowing self.execute to be none by only running the function when it has a value.
               if self.execute_click:
                   self.execute_click()

   # Checking if the mouse shares coordinates with
   # the sprite and setting self.hover to true if so.
   def check_hover(self):
      mouse_position = pygame.mouse.get_pos()
      self.hovering = self.rect.collidepoint(mouse_position)

   # Drawing the sprite if it is set to visible
   def draw(self, screen):
       if self.visible:
           screen.blit(self.image, self.rect.topleft)

           # Drawing a rectangle over the hovered sprite (used in the
           # game shop to display info about the item)
           if self.hovering:
               hover_rect = self.rect.copy()
               hover_rect.x += 30
               hover_rect.width = 200
               hover_rect.height = 150

               pygame.draw.rect(screen, GRAY, hover_rect)

               # If there is text to be displayed when hovering, it is blit to the hover rect.
               if self.hover_text:
                   lines = self.hover_text.split("\n")
                   line_height = self.font.get_linesize()
                   y_offset = hover_rect.y + 10

                   for line in lines:
                       text = self.font.render(line, True, WHITE)
                       text_rect = text.get_rect(topleft=(hover_rect.x, y_offset))
                       text_rect.x = 0
                       text_rect.y = 0
                       if self.hover_surface:
                           self.hover_surface.blit(text, text_rect)
                       else:
                           screen.blit(text, text_rect)
                       y_offset += line_height

# Blueprint for basic buttons
class basic_button(pygame.sprite.Sprite):
   # Parameters for position, text, click function, size etc... make button highly customizable.
   def __init__(self, x, y, text, execute_click, screen, width=160, height=80, color=YELLOW):
       super().__init__()
       self.screen = screen
       self.x = x
       self.y = y
       self.text = text
       self.color = None
       self.visible = True
       self.width = width
       self.height = height
       self.execute_click = execute_click
       self.font = pygame.font.SysFont('Courier New', 15, True, False)
       self.text_box = self.font.render(self.text, True, BLACK)
       self.button = pygame.Surface((self.width, self.height))
       self.button.fill(color)

       # Positioning the text in the center of the button --> Todo: needs reworking
       self.text_rect = self.text_box.get_rect()
       self.text_width = self.text_rect.width
       self.text_height = self.text_rect.height
       self.text_x = (self.text_width - self.width)/2
       self.text_y = (self.text_height - self.height)/2
       self.button.blit(self.text_box, (self.text_x, self.text_y))
       self.button_sprite = Clickability(self.button, x, y, execute_click)

   # Checking for clicks
   def update(self, events):
       if self.visible:
            self.button_sprite.check_click(events)

   # Drawing the button
   def draw(self):
       if self.visible:
            self.button_sprite.draw(self.screen)