import pygame as pg
import sys
import game_functions as gf
from vector import Vector
from pygame.sprite import Sprite
from pygame.sprite import Group
from time import sleep

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_display = True
        self.cursor_rect = pg.Rect(0, 0, 20, 20)
        self.offset = -100


        #self.image = pygame.image.load('Menu3.jpg').convert()
        #self.image = pygame.transform.scale(self.image, (self.game.DISPLAY_W, self.game.DISPLAY_H))

    def create_text(self, text):
        text = text
        return text

    """def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)"""

    def blit_screen(self):
        self.game.screen.blit(self.game.image, (0, 0))
        self.game.reset_keys()

    def renderText(self, text, width, height, color, size):
        font = pg.font.Font('AmericanCaptain.ttf', size)

        textsurface = font.render(text, False, color)
        textrect = textsurface.get_rect()
        textrect.centerx = width / 2
        textrect.centery = height / 2
        self.game.screen.blit(textsurface, textrect)

    def renderHeader(self, text, width, color, size):
        font = pg.font.Font('Franchise.ttf', size)
        textsurface = font.render(text, False, color)
        textrect = textsurface.get_rect()
        textrect.centerx = width / 2
        textrect.centery = 70
        self.game.screen.blit(textsurface, textrect)

    def renderAlienPoints(self,image, imagerect, text,widtht, widthm,text_h, img_h, color, size):
        font = pg.font.Font('Franchise.ttf', size)
        textsurface = font.render(text, False, color)
        textrect = textsurface.get_rect()
        imgrect = imagerect
        textrect.centerx = widtht
        textrect.centery = text_h
        imgrect.centerx = widthm
        imgrect.centery = img_h
        self.game.screen.blit(image, imgrect)
        self.game.screen.blit(textsurface, textrect)







class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()

    def display_menu(self):
        print("Menu is running")
        self.run_display = True
        header = self.create_text("SPACE INVADERS")
        text1 = self.create_text("Start Game")
        text2 = self.create_text("High Score")
        score1 = self.create_text("100")
        score2 = self.create_text("200")
        score3 = self.create_text("300")
        score4 = self.create_text("???")

        self.alien1 = pg.image.load('images/alien.png')
        self.alien1.convert()
        alien1_rect = self.alien1.get_rect()
        self.alien1 = pg.transform.scale(self.alien1, (68, 58))


        self.alien2 = pg.image.load('images/alien2.png')
        self.alien2.convert()
        alien2_rect = self.alien2.get_rect()
        self.alien2 = pg.transform.scale(self.alien2, (80, 70))

        self.alien3 = pg.image.load('images/alien3.png')
        self.alien3.convert()
        alien3_rect = self.alien3.get_rect()
        self.alien3 = pg.transform.scale(self.alien3, (100, 90))

        self.alien4 = pg.image.load('images/alien4.png')
        self.alien4.convert()
        alien4_rect = self.alien4.get_rect()
        self.alien4 = pg.transform.scale(self.alien4, (200, 190))

        # self.draw_cursor()
        self.renderHeader(header, self.game.settings.screen_width, self.game.WHITE, 150)
        self.renderText(text1, self.game.settings.screen_width, self.game.settings.screen_height, self.game.WHITE, 50)
        self.renderText(text2, self.game.settings.screen_width, self.game.settings.screen_height + 100, self.game.WHITE, 50)
        self.renderAlienPoints(self.alien1, alien1_rect, score1,
                               self.game.settings.screen_width - 1000,
                               self.game.settings.screen_width - 854,
                               self.game.settings.screen_height - 500 ,
                               self.game.settings.screen_height - 450,
                               self.game.WHITE, 50)

        self.renderAlienPoints(self.alien2, alien2_rect, score2, self.game.settings.screen_width/2,
                               self.game.settings.screen_width/2 + 133, self.game.settings.screen_height - 500,
                               self.game.settings.screen_height - 430, self.game.WHITE, 50)
        self.renderAlienPoints(self.alien3, alien3_rect, score3, self.game.settings.screen_width - 195,
                               self.game.settings.screen_width - 6, self.game.settings.screen_height - 500,
                               self.game.settings.screen_height - 400, self.game.WHITE, 50)
        self.renderAlienPoints(self.alien4, alien4_rect, score4, self.game.settings.screen_width/2,
                               self.game.settings.screen_width + 115, self.game.settings.screen_height-100,
                               self.game.settings.screen_height + 340, self.game.WHITE, 50)
        self.game.mouse = pg.mouse.get_pos()
        pg.display.flip()


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (150, 150, 150)
        self.laser_speed_factor = 1
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = 60, 60, 60
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 50
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.ship_limit = 3


class GameStats:
    def __init__(self, game):
        """Initialize statistics."""
        self.game = game
        self.settings = self.game.settings
        self.game_active = True
        self.reset_stats()


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit

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

    def update(self):
        self.x += (self.setting.alien_speed_factor * self.setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def get_number_aliens_x(self, alien_width):
        """Determine the number of aliens that fit in a row."""
        available_space_x = self.setting.screen_width - 2 * alien_width
        number_aliens_x = int(available_space_x / (2 * alien_width))
        return number_aliens_x

    def get_number_rows(self, alien_height, ship_height):
        """Determine the number of rows of aliens that fit on the screen."""
        available_space_y = (self.setting.screen_height - (3 * alien_height) - ship_height)
        number_rows = int(available_space_y / (2 * alien_height))
        return number_rows

    def create_alien(self,alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self.game)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.game.aliens.add(alien)

    def create_fleet(self):
        """Create a full fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        alien = Alien(self.game)
        alien_width = alien.rect.width
        number_aliens_x = self.get_number_aliens_x(alien_width)
        number_rows = self.get_number_rows(self.game.ship.rect.height, alien.rect.height) - 2
        # Create the first row of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number,row_number)

    def check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.game.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.game.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

    def check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.game.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self.game.ship.ship_hit()
                break

    def update_aliens(self):
        if pg.sprite.spritecollideany(self.game.ship, self.game.aliens):
            print("Ship hit!!!")
            self.game.ship.ship_hit()
        self.check_fleet_edges()
        self.game.aliens.update()
        self.game.alien.check_aliens_bottom()

    def draw(self):
        self.screen.blit(self.image, self.rect)
"""
ID
FAST for 6 hours 
Insurance card 
referal letter
vacine card
8.30 am, arrive 15 mins before to check it. 
Feb 22
208 N Garfield Ave, Monterey Park. 
"""

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

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def ship_hit(self):
        # Decrement ships_left.
        if self.game.stats.ships_left > 1:
            print(self.game.stats.ships_left)
            self.game.stats.ships_left -= 1
            sleep(0.5)
        else:
            print("Game Is over")
            self.game.stats.game_active = False
        # Empty the list of aliens and bullets.
        self.game.aliens.empty()
        self.game.lasers.empty()
        # Create a new fleet and center the ship.
        self.game.alien.create_fleet()
        self.game.ship.center_ship()
        # Pause.


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
        self.DISPLAY_W, self.DISPLAY_H = 1920, 1080
        self.BLACK, self.WHITE, self.DARK = (0, 0, 0), (255, 255, 255), (245, 245, 245)
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        pg.display.set_caption("Alien Invasion")
        self.ship = Ship(game=self)
        self.lasers = Group()
        self.aliens = Group()
        self.alien = Alien(game=self)
        self.create_fleet = self.alien.create_fleet()
        self.stats = GameStats(game=self)
        self.menu = MainMenu(game=self)
        self.menu_running = True

    def update_bullets(self):
        collisions = pg.sprite.groupcollide(self.lasers, self.aliens, True, True)

    def update(self):
        self.ship.update()
        self.lasers.update()
        self.alien.update_aliens()
        self.update_bullets()
    def draw(self):
        self.screen.fill(self.bg_color)
        for laser in self.lasers.sprites():
            laser.draw()
        self.ship.draw()
        self.aliens.draw(self.screen)
        pg.display.flip()

    def play(self):
        finished = False
        while not finished:
            gf.check_events(game=self)  # exits game if QUIT pressed
            if self.stats.game_active and not self.menu_running:
                self.update()
                self.draw()
            else:
                self.menu.display_menu()




def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
