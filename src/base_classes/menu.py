import pygame

# Defining a class for "clickability" to assign click detection to all instances of it
class Clickability(pygame.sprite.Sprite):
     # By giving this function image, x and y parameters, we are able to easily use the
     # attributes of other classes in this one.The "execute" parameter similarly, allows
     # us to import functions from those other classes and run them when the mouse
     # click is in rectangle bounding the image.
    def __init__(self, image, x, y, execute):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.execute = execute

    def check_click(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
                self.execute()

class Menu:
    def __init__(self, screen):
        self.screen = screen

        # Making the rules invisible until otherwise declared,
        # preventing the draw function from drawing them.
        self.visible = False

        # Loading and sizing the image for the menu button
        menu_image = pygame.image.load("images/Menu.png")
        menu_image = pygame.transform.scale(menu_image, (70, 70))

        # Giving the menu button "clickability" attributes
        self.menu_sprite = Clickability(menu_image, 1200, 100, self.show)

        # Loading and sizing the rules menu
        rules_image = pygame.image.load("images/Rules.png")
        rules_image = pygame.transform.scale(rules_image, (600, 600))
        self.rules_sprite = pygame.sprite.Sprite()
        self.rules_sprite.image = rules_image
        self.rules_sprite.rect = self.rules_sprite.image.get_rect()
        self.rules_sprite.rect.center = (640, 360)

        self.sprites = pygame.sprite.Group(self.menu_sprite)

    # Making the rules visible
    def show(self):
        self.visible = True

    def update(self, events):
        if not self.visible:
            for sprite in self.sprites:
                sprite.check_click(events)

    # Drawing the rules menu if the "button" has been clicked
    def draw(self):
        if not self.visible:
            self.sprites.draw(self.screen)
        else:
            self.screen.blit(self.rules_sprite.image, self.rules_sprite.rect)

