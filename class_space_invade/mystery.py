import pygame as pg
from pygame.sprite import Sprite, Group
from pygame import time
from pygame import mixer
from timer import Timer
from pygame import font
from random import randint


WHITE = (255,255,255)
class Mystery(Sprite):

    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.screen = game.screen
        self.stats = game.stats
        self.setting = game.settings
        alien = [pg.image.load(f'images/alien4_{n}.png') for n in range(4)]
        alien = [pg.transform.scale(image, (57,58)) for image in alien]
        self.alien = pg.image.load(f'images/alien4_0.png')
        self.rect= self.alien.get_rect(topleft=(-100,45))
        self.row = 5
        self.screen = game.screen
        self.moveTime = 10000
        self.direction = 1
        self.mysteryEntered = mixer.Sound('sounds/mysteryentered.wav')
        self.mysteryEntered.set_volume(0.3)
        self.playSound = True


    def update(self):
        resetTimer = False
        self.timer = time.get_ticks()
        passed = self.timer - self.game.timer
        if passed > self.moveTime:
            if (self.rect.x < 0 or self.rect.x > 1250) and self.playSound:
                self.mysteryEntered.play()
                self.playSound = False
            if self.rect.x < 1300 and self.direction == 1:
                self.mysteryEntered.fadeout(4000)
                self.rect.x += 2
                self.screen.blit(self.alien, self.rect)
            if self.rect.x > -210 and self.direction == -1:
                self.mysteryEntered.fadeout(4000)
                self.rect.x -= 2
                self.screen.blit(self.alien, self.rect)
        if self.rect.x > 1290:
            self.playSound = True
            self.direction = -1
            resetTimer = True
        if self.rect.x < -200:
            self.playSound = True
            self.direction = 1
            resetTimer = True
        if passed > self.moveTime and resetTimer:
            self.timer = time.get_ticks()
            self.game.timer = time.get_ticks()
    def draw_mys(self):
        self.screen.blit(self.alien, self.rect)



    def renderText(self, text, x, y, color, size):

        self.text= font.render(text, False, color)
        self.textrect = self.text.get_rect(topleft = (x,y))

    def hit(self):
        self.score = randint(0, 1000)
        print(f"TOTAL SCORE BEFORE: {self.stats.score} points")
        print(f"UFO HIT! GAINED {self.score} points")
        self.stats.mystery_hit(mystery=self)
        print(f"TOTAL SCORE AFTER: {self.stats.score} points")
        self.timer = time.get_ticks()
        self.game.timer = time.get_ticks()
        self.kill()



    def ex_update(self, current_time, *args):
        passed = current_time - self.timer
        if passed <= 200 or 400 < passed <= 600:
            self.draw(self.screen)
        elif 600 < passed:
            self.kill()

class Text(object):
    def __init__(self, textFont, size, message, color, xpos, ypos):
        self.font = font.Font(textFont, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos, ypos))

    def draw(self, surface):
        surface.blit(self.surface, self.rect)
