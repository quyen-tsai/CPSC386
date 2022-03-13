import pygame as pg
from pygame.sprite import Sprite, Group
from landing_page import LandingPage
from sys import exit
import game_functions as gf
from time import sleep
from stats import Stats
from scoreboard import Scoreboard
from laser import Lasers
from laser import Enemy_Bullet
from ship import Ship
from alien import AlienFleet
from settings import Settings
from sound import Sound
from mystery import Mystery
from pygame import time
from obstacle import Blockers
from highscore import HighScorePage
class Game:
    RED = (255, 0, 0)


    def __init__(self):

        pg.init()
        self.timer = time.get_ticks()
        self.settings = Settings()
        self.stats = Stats(game=self)
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        self.sound = Sound()
        self.sb = Scoreboard(game=self)
        pg.display.set_caption("Alien Invasion")
        self.ship = Ship(game=self)
        self.alien_fleet = AlienFleet(game=self)
        self.lasers = Lasers(game=self)
        self.ship.set_alien_fleet(self.alien_fleet)
        self.ship.set_lasers(self.lasers)
        self.Mys = Group()
        self.Mys.add(Mystery(game=self))
        self.blocker = Blockers(game=self)
        self.blocker.create_blockers()
        self.landing_page = LandingPage(game=self)
        self.hc = HighScorePage(game = self)
        self.MENU, self.HIGH, self.PLAY = True, False, False

    def restart(self):
        if self.stats.ships_left == 0: 
          self.game_over()
        print("restarting game")
        while self.sound.busy():
            pass
        self.lasers.empty()
        self.alien_fleet.empty()
        self.alien_fleet.create_fleet()
        self.ship.center_bottom()
        self.ship.reset_timer()
        self.alien_fleet.enemy_bullets.empty()
        self.blocker.kill()
        self.blocker.create_blockers()
        self.update()
        self.draw()
        sleep(0.5)

    def update(self):
        self.ship.update()
        self.alien_fleet.update()
        self.lasers.update()
        self.sb.update()
        self.blocker.check_collide()



    def draw(self):
        self.screen.fill(self.bg_color)
        self.ship.draw()
        self.alien_fleet.draw()
        self.lasers.draw()
        for mystery in self.Mys:
            mystery.update()
        self.sb.draw()
        self.blocker.update()
        pg.display.flip()

    def play(self):
        self.finished = False
        self.sound.play_bg()
        while not self.finished:
            if self.MENU:
                self.landing_page.show()
            if self.HIGH:
                self.hc.show()
            if self.PLAY:
                self.update()
                self.draw()
                gf.check_events(game=self)   # exits game if QUIT pressed
        self.game_over()



    def game_over(self):
      self.sound.play_game_over()
      print('\nGAME OVER!\n\n')  
      exit()    # can ask to replay here instead of exiting the game

def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
