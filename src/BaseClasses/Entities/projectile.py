import json
import numpy

from src.Tools.Misc_Tools.time_handler import *
from src.Tools.Misc_Tools.unit_handler import generate_relative_value_2d, swth_sprite



weapon_data = json.load(open("src/JSON_Files/weapons.json"))

class Projectile(swth_sprite):
    FADE_OUT_SPEED = 10

    def __init__(self, sprite, weapon, starting_position, size = [1.5,2], rotation = 0, velocity_offset = [1,-1]):
        super().__init__(sprite, size=size, rotation=rotation)
        self.rect = self.image.get_rect()
        self.position = starting_position.copy()
        super().update_position(self.position)
        self.velocity = numpy.multiply(weapon_data[weapon]["Velocity"].copy(), velocity_offset)
        self.damage = weapon_data[weapon]["Damage"]
        self.opacity = 255


    def __del__(self):
        super().kill()

    def update(self, *args, **kwargs):
        # If the top of the projectile is at the edge of the screen, begin fadeout.
        if self.rect.top < 0:
            self.fade_out()
        elif super().get_position()[1] > 100 - super().get_size()[1] / 2:
            self.fade_out()
        else:
            # Animating the projectile to move by its velocity from its starting position each frame.
            super().update_position((numpy.array(self.velocity) * Timer.get_last_frame_time_s())+ numpy.array(super().get_position()))




    # Decreasing the opacity of the sprite gradually when it hits the top of the screen
    def fade_out(self):
        self.opacity -= self.FADE_OUT_SPEED

        # Deleting the sprite when it is completely transparent.
        if self.opacity < 0:
            self.__del__()

        self.image.set_alpha(self.opacity)



