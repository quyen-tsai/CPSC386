import pygame as pg
from vector import Vector
from pygame.sprite import Sprite, Group
from copy import copy
from random import randint
# from alien import Alien
# from stats import Stats
from spritesheet import SpriteSheet
from timer import Timer
from mystery import Mystery

class Lasers:
    def __init__(self, game):
        self.game = game
        self.stats = game.stats
        self.alien_fleet = game.alien_fleet
        self.lasers = Group()
        self.sound = game.sound

    def add(self, laser): self.lasers.add(laser)
    def empty(self): self.lasers.empty()
    def fire(self): 
      new_laser = Laser(self.game)
      self.lasers.add(new_laser)
      snd = self.sound
      snd.play_fire_phaser()

    def update(self):
        for laser in self.lasers.copy():
            if laser.rect.bottom <= 0: self.lasers.remove(laser)

        collisions = pg.sprite.groupcollide(self.alien_fleet.fleet, self.lasers, False, True)
        for alien in collisions: 
          if not alien.dying: alien.hit()


        for mystery in pg.sprite.groupcollide(self.game.Mys, self.lasers, False, True):
            mystery.mysteryEntered.stop()
            mystery.hit()
            self.game.Mys.add(Mystery(game=self.game))


        if self.alien_fleet.length() == 0:  
            self.stats.level_up()
            self.game.restart()
            
        for laser in self.lasers:
            laser.update()

    def draw(self):
        for laser in self.lasers:
            laser.draw()


class Laser(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.w, self.h = self.settings.laser_width, self.settings.laser_height
        self.ship = game.ship
        self.rect = pg.Rect(0, 0, self.w, self.h)
        self.center = copy(self.ship.center)
        # print(f'center is at {self.center}')
        # self.color = self.settings.laser_color
        tu = 50, 255
        self.color = randint(*tu), randint(*tu), randint(*tu)
        self.v = Vector(0, -1) * self.settings.laser_speed_factor

    def update(self):
        self.center += self.v
        self.rect.x, self.rect.y = self.center.x, self.center.y

    def draw(self): pg.draw.rect(self.screen, color=self.color, rect=self.rect)


class Enemy_Bullet(Sprite):
    def __init__(self, ai_settings, screen, alien,game):
        super(Enemy_Bullet, self).__init__()
        self.game = game
        self.screen = screen
        self.sprite = SpriteSheet('images/enemy_laser.png', 2)
        self.index = 0
        self.type = 0
        self.timer = 0
        self.image = self.sprite.image_get((8 * self.index, 24 * self.type, 8, 24))
        self.rect = pg.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom
        self.sound = game.sound
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update_enemy_bullet(self):
        self.y += self.speed_factor
        self.rect.y = self.y

        if self.timer < 10:
            self.timer += 1
        else:
            self.index += 1
            if self.index >= 4:
                self.index = 0
            self.image = self.sprite.image_get((8 * self.index, 24 * self.type, 8, 24))
            self.timer = 0


    def show_enemy_bullet(self):
        self.screen.blit(self.image, self.rect)