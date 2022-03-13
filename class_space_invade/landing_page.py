from decimal import HAVE_CONTEXTVAR
import imghdr
import pygame as pg
import sys
from alien import Alien
from vector import Vector
from button import Button

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)


pg.transform.rotozoom

class LandingPage:
    # alien_one_imgs = [pg.image.load(f'images/tie{n}.png') for n in range(5)]
    # alien_two_imgs = [pg.image.load(f'images/alienOne{n}.png') for n in range(2)]
    # alien_three_imgs = [pg.image.load(f'images/green_alien{n}.png') for n in range(2)]
    # ufo_imgs = [pg.image.load(f'images/alien2_{n}.bmp') for n in range(4)]

    alien_one_imgs = [pg.image.load(f'images/alien2_{n}.png') for n in range(3)]
    alien_two_imgs = [pg.image.load(f'images/alien1_{n}.png') for n in range(3)]
    alien_three_imgs = [pg.image.load(f'images/green_alien{n}.png') for n in range(2)]
    ufo_imgs = [pg.image.load(f'images/alien4_{n}.png') for n in range(4)]
    ufo_imgs  = [pg.transform.scale(image, (57, 58)) for image in ufo_imgs]
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.landing_page_finished = False

        headingFont = pg.font.Font('AmericanCaptain.ttf', 130)
        subheadingFont = pg.font.Font('Franchise.ttf', 122)
        font = pg.font.Font('Franchise.ttf', 48)

        strings = [('SPACE INVADERS', WHITE, headingFont),('', WHITE, headingFont),
                ('= 100 PTS', GREY, font), ('= 200 PTS', GREY, font),
                            ('= 300 PTS', GREY, font), ('= ???', GREY, font),
               # ('PLAY GAME', GREEN, font), 
               #  ('HIGH SCORES', GREY, font)
                ]

        self.texts = [self.get_text(msg=s[0], color=s[1], font=s[2]) for s in strings]

        self.posns = [150, 230]
        alien = [60 * x + 400 for x in range(4)]
        # play_high = [x for x in range(650, 760, 80)]
        # play_high = 730
        self.posns.extend(alien)
        self.posns.append(730)

        centerx = self.screen.get_rect().centerx

        self.play_button = Button(self.screen, "PLAY GAME", ul=(centerx - 150, 650))
        self.high_score_button = Button(self.screen, "HIGH SCORE", ul=(centerx - 150, 700))

        n = len(self.texts)
        self.rects = [self.get_text_rect(text=self.texts[i], centerx=centerx, centery=self.posns[i]) for i in range(n)]
        self.alien_one = Alien(game=game, image_list=LandingPage.alien_one_imgs, 
                               v=Vector(), ul=(centerx - 140, 370))
        self.alien_two = Alien(game=game, image_list=LandingPage.alien_two_imgs, 
                               v=Vector(), ul=(centerx - 145, 430))
        self.alien_three = Alien(game=game, image_list=LandingPage.alien_three_imgs, 
                               v=Vector(), ul=(centerx - 140, 490))
        self.ufo = Alien(game=game, image_list=LandingPage.ufo_imgs, 
                               v=Vector(), ul=(centerx - 140, 565))

        self.hover_mouse = False
        self.hover_high = False

    def get_text(self, font, msg, color): return font.render(msg, True, color, BLACK)

    def get_text_rect(self, text, centerx, centery):
        rect = text.get_rect()
        rect.centerx = centerx
        rect.centery = centery
        return rect

    def mouse_on_play_button(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        return self.play_button.rect.collidepoint(mouse_x, mouse_y)

    def mouse_on_high_button(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        return self.high_score_button.rect.collidepoint(mouse_x, mouse_y)

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            if e.type == pg.KEYUP and e.key == pg.K_p:  # pretend PLAY BUTTON pressed
                self.game.MENU = False
                self.game.PLAY = True
            elif e.type == pg.MOUSEBUTTONDOWN:
                if self.mouse_on_play_button():
                    self.game.MENU = False
                    self.game.PLAY = True
                    self.game.HIGH = False
                if self.mouse_on_high_button():
                    self.game.MENU = False
                    self.game.HIGH = True
                    self.game.PLAY = False
            elif e.type == pg.MOUSEMOTION:
                if self.mouse_on_play_button() and not self.hover_mouse:
                    self.play_button.toggle_colors()
                    self.hover_mouse = True
                elif not self.mouse_on_play_button() and self.hover_mouse:
                    self.play_button.toggle_colors()
                    self.hover_mouse = False
                if self.mouse_on_high_button() and not self.hover_high:
                    self.high_score_button.toggle_colors()
                    self.hover_high = True
                elif not self.mouse_on_high_button() and self.hover_high:
                    self.high_score_button.toggle_colors()
                    self.hover_high = False


    def update(self):       # TODO make aliens move
        pass 

    def show(self):
        while self.game.MENU:
            self.update()
            self.draw()
            self.check_events()   # exits game if QUIT pressed

    def draw_text(self):
        n = len(self.texts)
        for i in range(n):
            self.screen.blit(self.texts[i], self.rects[i])

    def draw(self):
        self.screen.fill(BLACK)
        self.alien_one.draw()
        self.alien_two.draw()
        self.alien_three.draw()
        self.ufo.draw()
        self.draw_text()
        self.play_button.draw()
        self.high_score_button.draw()
        # self.alien_fleet.draw()   # TODO draw my aliens
        # self.lasers.draw()        # TODO dray my button and handle mouse events
        pg.display.flip()
