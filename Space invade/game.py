import pygame as pg
import sys
import game_functions as gf
from vector import Vector
from pygame.sprite import Sprite
from pygame.sprite import Group

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (150, 150, 150)
        self.laser_speed_factor = 1
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = 60, 60, 60

class Alien(Sprite):
    def __init__(self,game):
        super(Alien, self).__init__()
        self.game = game
        self.screen = game.screen
        self.setting = game.settings
        self.image = pg.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self): pass
    
    def draw(self):
        self.screen.blit(self.image, self.rect)


class Laser(Sprite):
    def __init__(self, game):
        super(Laser, self).__init__()
        self.game = game
        self.screen = game.screen
        self.setting = game.settings
        self.rect = pg.Rect(0, 0, self.setting.laser_width, self.setting.laser_height)
        self.rect.centerx = game.ship.rect.centerx
        self.rect.top = game.ship.rect.top
        self.y = float(self.rect.y)
        self.color = self.setting.laser_color
        self.speed_factor = self.setting.laser_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)


class Ship:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.image = pg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.v = Vector()

    def moving(self, vector): self.v = vector
    def update(self):
        if self.rect.right == self.screen_rect.right:
            self.rect.centerx -= 1
        elif self.rect.left == self.screen_rect.left:
            self.rect.centerx += 1
        else:
            self.rect.centerx += self.v.x

        if self.rect.top == self.screen_rect.top:
            self.rect.centery += 1
        if self.rect.bottom == self.screen_rect.bottom:
            self.rect.centery -= 1
        else:
            self.rect.centery += self.v.y

    def draw(self): self.screen.blit(self.image, self.rect)


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        pg.display.set_caption("Alien Invasion")
        self.ship = Ship(game=self)
        self.lasers = Group()

    def update(self):
        self.ship.update()
        self.lasers.update()

    def draw(self):
        self.screen.fill(self.bg_color)
        for laser in self.lasers.sprites():
            laser.draw()
        self.ship.draw()
        pg.display.flip()

    def play(self):
        finished = False
        while not finished:
            gf.check_events(game=self)  # exits game if QUIT pressed
            self.draw()
            self.update()


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
