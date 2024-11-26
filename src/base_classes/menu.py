import pygame
from common_variables import *

# Creating the visibility function globally so it can be accessed in each class. It is like a switch.
def visibility(target):
    target.visible = not target.visible

# Defining a class for "clickability" to assign click detection to all instances of it
class Clickability(pygame.sprite.Sprite):
     # The "execute" parameter allows the import of functions from other classes and
     # runs them when the mouse click is in rectangle bounding the image.
    def __init__(self, sprite_image, x, y, execute_click = None, hover_image = None, execute_hover = None):
        super().__init__()
        self.sprite_image = sprite_image
        self.hover_image = hover_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.execute_click = execute_click
        self.execute_hover = execute_hover
        self.hovering = False
        self.visible = True

    # Checking if the sprite was clicked
    def check_click(self, events):
        # Loping through each event in pygame and triggering the desired function when the mouse button is released.
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
                # Allowing self.execute to be none by only running the function when it has a value.
                if self.execute_click:
                    self.execute_click()

    def check_hover(self, events):
        for event in events:
            if self.rect.collidepoint(event.pos):
                self.hovering = True

                # Allowing self.execute_hover to be none by only running the function when it has a value.
                if self.execute_hover:
                    self.execute_hover()
            else:
                self.hovering = False

    # Drawing the  sprite if it is set to visible
    def draw(self, screen):
        if self.visible:
            screen.blit(self.sprite_image, self.rect.topleft)

        if self.hovering:
            screen.blit(self.hover_image, self.rect.topleft)

class Menu:
    def __init__(self, screen):
        self.screen = screen

        # Loading and sizing the image for the menu button
        menu_image = pygame.image.load("images/buttons_and_menus/Menu.png")
        menu_image = pygame.transform.scale(menu_image, (menu_button_width, menu_button_height))

        # Giving the menu button "clickability" attributes. The "execute" parameter runs the
        # visibility function. Using lambda allows us to use specific values from this class
        # in the clickability class by making the function "anonymous".
        self.menu_sprite = Clickability(
            menu_image,
            screen_width - (0.0225 * screen_width),
            screen_height/7.2,
            lambda: visibility(self.rules_sprite)
        )

        # Loading the rules menu and sizing it.
        rules_image = pygame.image.load("images/buttons_and_menus/Rules.png")
        rules_image = pygame.transform.scale(rules_image, (rules_width, rules_height))
        self.rules_sprite = Clickability(
            rules_image,
            screen_width/2,
            screen_height/2,
            None
        )

        # Starting with the rules menu invisible.
        self.rules_sprite.visible = False

        # Loading, sizing and giving clickability to teh close button
        close_button_image = pygame.image.load("images/buttons_and_menus/Close.png")
        close_button_image = pygame.transform.scale(close_button_image, (close_button_width, close_button_height))

        self.close_button_sprite = Clickability(
            close_button_image,
            screen_width / 2 + (rules_width / 2) - (close_button_width / 2),
            (screen_height - rules_height) / 2 + (close_button_height / 2),
            lambda: visibility(self.rules_sprite))

    # Checking if any of the buttons have been clicked in each frame.
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

# Creating the class for buttons that represents one player or two player game modes.
class player_mode_choice():
    def __init__(self, x, y, text, execute_click, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.visible = True
        self.execute_click = execute_click
        self.font = pygame.font.SysFont('Courier New', 15, True, False)
        self.text_box = self.font.render(text, True, BLACK)
        self.player_button = pygame.Surface((160, 80))
        self.player_button.fill(GOLD)
        self.player_button.blit(self.text_box, (30, 30))
        self.player_button_sprite = Clickability(self.player_button, x, y, execute_click)

    def update(self, events):
        if self.visible:
            self.player_button_sprite.check_click(events)

    def draw(self):
        if self.visible:
            self.player_button_sprite.draw(self.screen)

# Add code for item shop and other clickable objects below




