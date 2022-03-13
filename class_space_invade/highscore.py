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


class HighScorePage:
    # alien_one_imgs = [pg.image.load(f'images/tie{n}.png') for n in range(5)]
    # alien_two_imgs = [pg.image.load(f'images/alienOne{n}.png') for n in range(2)]
    # alien_three_imgs = [pg.image.load(f'images/green_alien{n}.png') for n in range(2)]
    # ufo_imgs = [pg.image.load(f'images/alien2_{n}.bmp') for n in range(4)]

    def __init__(self, game):
        self.screen = game.screen
        self.game = game
        headingFont = pg.font.Font('AmericanCaptain.ttf', 130)
        subheadingFont = pg.font.Font('Franchise.ttf', 70)
        font = pg.font.Font('Franchise.ttf', 48)
        strings = [('SPACE INVADERS', WHITE, headingFont), ('', WHITE, headingFont)]
        self.texts = [self.get_text(msg=s[0], color=s[1], font=s[2]) for s in strings]
        self.high_score_text = self.get_text(msg=f'CURRENT HIGHSCORE: {game.stats.highscore}', color=WHITE, font=subheadingFont)
        n = len(self.texts)
        centerx = self.screen.get_rect().centerx
        centery = self.screen.get_rect().centery
        self.posns = [150, 230]
        self.rects = [self.get_text_rect(text=self.texts[i], centerx=centerx, centery=self.posns[i]) for i in range(n)]
        self.high_rect = self.get_text_rect(text=self.high_score_text, centerx=centerx, centery=centery)
        self.play_button = Button(self.screen, "HOME", ul=(centerx - 150, 650))

        self.hover_mouse = False
        self.hover_high = False

    def get_text(self, font, msg, color):
        return font.render(msg, True, color, BLACK)

    def get_text_rect(self, text, centerx, centery):
        rect = text.get_rect()
        rect.centerx = centerx
        rect.centery = centery
        return rect

    def mouse_on_play_button(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        return self.play_button.rect.collidepoint(mouse_x, mouse_y)

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            if e.type == pg.KEYUP and e.key == pg.K_p:  # pretend PLAY BUTTON pressed
                self.game.HIGH = False
            elif e.type == pg.MOUSEBUTTONDOWN:
                if self.mouse_on_play_button():
                    self.game.HIGH = False
                    self.game.MENU = True
            elif e.type == pg.MOUSEMOTION:
                if self.mouse_on_play_button() and not self.hover_mouse:
                    self.play_button.toggle_colors()
                    self.hover_mouse = True
                elif not self.mouse_on_play_button() and self.hover_mouse:
                    self.play_button.toggle_colors()
                    self.hover_mouse = False



    def show(self):
        while self.game.HIGH:
            self.draw()
            self.check_events()  # exits game if QUIT pressed

    def draw_text(self):
        n = len(self.texts)
        self.screen.blit(self.high_score_text, self.high_rect)
        for i in range(n):
            self.screen.blit(self.texts[i], self.rects[i])

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_text()
        self.play_button.draw()
        # self.alien_fleet.draw()   # TODO draw my aliens
        # self.lasers.draw()        # TODO dray my button and handle mouse events
        pg.display.flip()
