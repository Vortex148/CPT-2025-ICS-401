import pygame
from src.Tools.Constants.ScreenConstants import *
from src.Tools.Constants.ColourConstants import *



def visibility(target):
    target.visible = not target.visible

# Defining a class for "clickability" to assign click detection to all instances of it
class Clickability(pygame.sprite.Sprite):
     # The "execute" parameter allows the import functions from other classes and
     # running them when the mouse click is in rectangle bounding the image.
    def __init__(self, image, x, y, execute):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.execute = execute
        self.visible = True

        # Checking if the sprite was clicked
    def check_click(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
                if self.execute:
                    self.execute()

        # Drawing the clickable sprite if it is set to visible
    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect.topleft)

class Menu:
    def __init__(self, screen):
        self.screen = screen

        # Loading and sizing the image for the menu button
        menu_image = pygame.image.load("Images/Menu.png")
        menu_image = pygame.transform.scale(menu_image, (menu_button_width, menu_button_height))

        # Giving the menu button "clickability" attributes. The "execute" parameter runs the
        # visibility function. Using lambda allows us to use specific values from this class
        # by making the function "anonymous"
        self.menu_sprite = Clickability(
            menu_image,
            screen_width - (0.0225 * screen_width),
            screen_height/7.2,
            lambda: visibility(self.rules_sprite)
        )

        # Loading and sizing the rules menu
        rules_image = pygame.image.load("Images/Rules.png")
        rules_image = pygame.transform.scale(rules_image, (rules_width, rules_height))
        self.rules_sprite = Clickability(
            rules_image,
            screen_width/2,
            screen_height/2,
            None
        )

        # Starting with the rules menu invisible.
        self.rules_sprite.visible = False

        close_button_image = pygame.image.load("Images/Close.png")
        close_button_image = pygame.transform.scale(close_button_image, (close_button_width, close_button_height))

        # Giving the menu button "clickability" attributes
        self.close_button_sprite = Clickability(
            close_button_image,
            screen_width / 2 + (rules_width / 2) - (close_button_width / 2),
            (screen_height - rules_height) / 2 + (close_button_height / 2),
            lambda: visibility(self.rules_sprite))

        self.sprites = pygame.sprite.Group(self.menu_sprite, self.rules_sprite, self.close_button_sprite)

    def update(self, events):
        self.menu_sprite.check_click(events)

        if self.rules_sprite.visible:
            self.close_button_sprite.check_click(events)

        # The menu button is always draw. If the rules are visible they are drawn as well
        # as the close button. The loop resets and checks for clicks on the close button.
    def draw(self):
        self.menu_sprite.draw(self.screen)
        if self.rules_sprite.visible:
            self.rules_sprite.draw(self.screen)
            self.close_button_sprite.draw(self.screen)

class player_mode_choice():
    def __init__(self, x, y, text, execute, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.visible = True
        self.execute = execute
        self.font = pygame.font.SysFont('Courier New', 15, True, False)
        self.text_box = self.font.render(text, True, BLACK)
        self.player_button = pygame.Surface((160, 80))
        self.player_button.fill(GOLD)
        self.player_button.blit(self.text_box, (30, 30))
        self.player_button_sprite = Clickability(self.player_button, x, y, execute)

    def update(self, events):
        if self.visible:
            self.player_button_sprite.check_click(events)

    def draw(self):
        if self.visible:
            self.player_button_sprite.draw(self.screen)

# Add code for item shop and other clickable objects below




