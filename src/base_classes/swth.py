import pygame


import numpy
from pygame.display import update


# % -> Screen Dimensions
def generate_relative_value_2d(value_2d):
   value = numpy.divide(value_2d, (100, 100))
   value = numpy.multiply(value, pygame.display.get_surface().get_size())
   return value


# % -> Modifier
def generate_relative_value(value, modifier):
   value = value / 100
   value = value * modifier
   return value


# Screen Dimensions -> %
def generate_screen_to_relative(screen_pos):
   value = numpy.divide(screen_pos, pygame.display.get_surface().get_size())
   value = numpy.multiply(value, [100, 100])
   return value


enable_hitbox = False
# SWTH is a custom unit that is measured as screen_width/100. This enables for various screen sizes to be supported easily
class swth_sprite(pygame.sprite.Sprite):
   def __init__(self, image, position = [0,0], size = [5,7]):
       super().__init__()
       self.super = super()
       self.position = position
       self.image = image
       self.size = size
       self.image = pygame.transform.smoothscale(image, generate_relative_value_2d(self.size))

       self.rect = self.image.get_rect()








   def generate_relative_coords(self):
       position = numpy.divide(self.position, (100,100))
       position = numpy.multiply(position, pygame.display.get_surface().get_size())
       self.rect.topleft = position
       # print(self.rect.center)
       return position






   def update_position(self, position):


       self.generate_relative_coords()
       self.position = position


   def update_rect_center(self, position):
       self.rect.center = position
       update()




   def update_position_abs(self, position):
       self.position = generate_screen_to_relative(position)
       print(self.position)


   def get_position(self):
       return self.position


   # def get_relative_position(self):
   #     return self.generate_relative_coords()


   def get_image(self):
       return self.image


   def get_rect(self):
       return self.rect


   def get_size(self):
       return self.size


   def draw(self):
       screen = pygame.display.get_surface()
       # screen.blit(self.image,(1180,100))
       if enable_hitbox:
           pygame.draw.rect(screen, pygame.Color('blue'), self.rect)
       screen.blit(self.image, self.generate_relative_coords())

   def update(self):
       self.rect.center = self.generate_relative_coords()

# Blueprint for screen relative objects
class swth_object(pygame.sprite.Sprite):
   def __init__(self, image_path, position = [0,0], size = [100,100], rotation = 0.0, frame_count = 1, opacity =  255):
       super().__init__()
       self.super = super()
       self.position = position
       self.frames = []
       self.size = size
       self.frame_index = 0
       self.opacity = opacity

       self.image = pygame.image.load(image_path).convert_alpha()
       self.image = pygame.transform.smoothscale(self.image, generate_relative_value_2d(self.size))
       self.image = pygame.transform.rotate(self.image, rotation)

       self.rect = self.image.get_rect()

       # for i in range(frame_count):
       #     try:
       #         image = pygame.image.load(image_path + "_" + str(i) + ".png").convert_alpha()
       #         image = pygame.transform.smoothscale(image, generate_relative_value_2d(self.size))
       #         image = pygame.transform.rotate(image, rotation)
       #
       #
       #         self.frames.append(image)
       #     except:
       #         raise(ValueError("Invalid frame count"))

   # Generating screen relative coordinates from regular pixel position values
   def generate_relative_coords(self):
       position = numpy.divide(self.position, (100,100))
       position = numpy.multiply(position, pygame.display.get_surface().get_size())
       self.rect.topleft = position
       return position


   def update_position(self, position):

       self.generate_relative_coords()
       self.position = position


   def update_rect_center(self, position):
       self.rect.center = position
       update()

   def update_position_abs(self, position):
       self.position = generate_screen_to_relative(position)
       print(self.position)

   def get_position(self):
       return self.position

   def get_size(self):
       return self.size

   def get_image(self):
       return self.image

   def get_rect(self):
       return self.rect

   def get_frame_index(self):
       return self.frame_index

   def draw(self, position=[0,0]):
       if position != [0,0]:
           self.update_position(position)
       screen = pygame.display.get_surface()
       if enable_hitbox:
           pygame.draw.rect(screen, pygame.Color('green'), self.rect)
       screen.blit(self.image, self.generate_relative_coords())

   def set_frame_index(self, frame_index):
       self.frame_index = frame_index

   def set_opacity(self, opacity):
       self.opacity = opacity

   def fade(self, fade_in):


       if fade_in and self.opacity != 255:
           self.opacity += 255 / 10
       elif self.opacity != 0 and not fade_in:
           self.opacity -= 255 / 10

       for i in self.frames:
           i.set_alpha(self.opacity)


   def update(self):
       self.rect.center = self.generate_relative_coords()