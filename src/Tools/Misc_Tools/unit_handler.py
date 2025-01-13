
import pygame
import numpy

from pygame.display import update



screen = pygame.display.get_surface()

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

# Scrn Dimensions -> %
def generate_screen_to_relative(screen_pos):
    value = numpy.divide(screen_pos, pygame.display.get_surface().get_size())
    value = numpy.multiply(value, [100, 100])
    return value

# SWTH is a custom unit that is measured in as screen_width/100. This enables for various screen sizes to be supported easily
class swth_sprite(pygame.sprite.Sprite):
    def __init__(self, image, position = [0,0], size = [5,7], rotation = 0, visible = True):
        super().__init__()
        self.super = super()
        self.position = position
        self.image = image
        self.size = size
        self.rotation = rotation
        self.image = pygame.transform.smoothscale(image, generate_relative_value_2d(self.size))
        self.image = pygame.transform.rotate(self.image, rotation)
        self.visible = visible
        self.rect = self.image.get_rect()




    def generate_relative_coords(self):
        position =  numpy.subtract(self.position, numpy.divide(self.size, [2,2]))
        position = numpy.divide(position, (100,100))
        position = numpy.multiply(position, pygame.display.get_surface().get_size())
        self.rect.topleft = position
        # print(self.rect.center)
        return position

    def set_visible(self, visible):
        self.visible = visible

    def set_image(self, image):
        self.image = image
        self.image = pygame.transform.smoothscale(image, generate_relative_value_2d(self.size))
        self.image = pygame.transform.rotate(self.image, self.rotation)

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
        if self.visible:
            screen.blit(self.image, self.generate_relative_coords())


    def update(self):
        self.rect.center = self.generate_relative_coords()




class swth_object(pygame.sprite.Sprite):
    def __init__(self, image_path, position = [0,0], size = [100,100], rotation = 0.0, frame_count = 1, opacity =  255):
        super().__init__()
        self.rect = None
        self.super = super()
        self.position = position.copy()
        self.frames = []
        self.size_init = size.copy()
        self.size = size
        self.frame_index = 0
        self.opacity = opacity
        self.zoom = 0
        self.image_path = image_path
        self.frame_count = frame_count
        self.init_position = position.copy()
        self.rotation = rotation
        self.set_frames(image_path)
        for i in self.frames:
            i.set_alpha(self.opacity)




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

    def update_size(self, size):
        self.size = size
        for i in range(len(self.frames)):
            self.frames[i] = pygame.image.load(self.image_path + "_" + str(i) + ".png")
            self.frames[i] = pygame.transform.scale(self.frames[i], generate_relative_value_2d(size))

    def update_position_abs(self, position):
        self.position = generate_screen_to_relative(position)
        print(self.position)

    def get_position(self):
        return self.position

    # def get_relative_position(self):
    #     return self.generate_relative_coords()

    def get_rect(self):
        return self.rect

    def get_frame_index(self):
        return self.frame_index
    
    def set_frames(self, image_path):
        self.frames.clear()
        for i in range(self.frame_count):
            try:
                image = pygame.image.load(image_path + "_" + str(i) + ".png").convert_alpha()
                image = pygame.transform.scale(image, generate_relative_value_2d(self.size))
                image = pygame.transform.rotate(image, self.rotation)

                self.frames.append(image)
            except:
                if i == 0:
                    raise(ValueError(f"Invalid image path of {image_path}"))

                raise(ValueError("Invalid frame count"))
        self.rect = self.frames[0].get_rect()

    def in_focus(self, focused, zoom_factor = 0.5, zoom_max = 10):

        ratio = self.size[1] / self.size[0]

        if focused and zoom_factor + self.zoom < zoom_max:
            self.zoom += zoom_factor
            # print(self.zoom)
            self.update_size(numpy.add(self.size, [zoom_factor / ratio, zoom_factor]))
            self.update_position(numpy.subtract(self.get_position(), [zoom_factor / (ratio * 2), zoom_factor / ratio * 0.5]))


        elif not focused and self.zoom > 0:

            self.zoom -= zoom_factor
            self.update_size(numpy.subtract(self.size, [zoom_factor / ratio, zoom_factor]))
            if self.zoom <= 0:
                self.zoom = 0

                self.update_size(self.size_init)
                self.update_position(self.init_position)
            else:
                self.update_position(numpy.add(self.get_position(), [zoom_factor / (ratio * 2), zoom_factor/ ratio * 0.5]))


        # print(self.get_position())



    def draw(self, position=[0,0]):
        if position != [0,0]:
            self.update_position(position)
        screen = pygame.display.get_surface()
        # screen.blit(self.image,(1180,100))
        screen.blit(self.frames[self.frame_index], self.generate_relative_coords())

    def set_frame_index(self, frame_index):
        self.frame_index = frame_index

    def set_opacity(self, opacity):
        self.opacity = opacity
        for i in self.frames:
            i.set_alpha(self.opacity)

    def fade(self, fade_in):

        if fade_in and self.opacity != 255:
            self.opacity += 255 / 10
        elif self.opacity != 0 and not fade_in:
            self.opacity -= 255 / 10


        for i in self.frames:
            i.set_alpha(self.opacity)

    def update(self):
        self.rect.center = self.generate_relative_coords()
