from vector import Vector

class Settings:
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = 0, 0, 0

        self.ship_speed_factor = 3
        self.ship_limit = 3

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = Vector(1, 0)

        self.laser_speed_factor = 3
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = 255, 0, 0


