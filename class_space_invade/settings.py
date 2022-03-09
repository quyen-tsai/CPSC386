from vector import Vector

class Settings:
    def __init__(self):
        self.screen_width = 1250
        self.screen_height = 780
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

        self.bullet_width = 8
        self.bullet_height = 24
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.bullet_speed_factor = 5


