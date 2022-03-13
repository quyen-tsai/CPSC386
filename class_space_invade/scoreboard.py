import pygame as pg
from pygame.sprite import Group
from ship import Ship


WHITE = (255, 255, 255)

class SbElement:
    def __init__(self, screen, bg_color, ul, font, get_score, highscore, round=True):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bg_color = bg_color
        self.ul = ul
        self.font = font
        self.round = round
        self.text_color = WHITE
        self.image, self.rect = None, None
        self.get_score = get_score
        self.high_score = highscore
        self.update()



    def update(self): 
        score = self.get_score()
        if self.high_score:
            score_str = f'HIGH SCORE: {score}'
        else:
            score_str = str(score)
        self.score_image = self.font.render(score_str, True, 
                                            self.text_color, self.bg_color)
        self.score_rect = self.score_image.get_rect()
        r = self.score_rect 
        if self.ul[0] + r.width > self.screen_rect.right:
            self.score_rect.right = self.screen_rect.right - 20
        else: self.score_rect.left = self.ul[0]
        self.score_rect.top = self.ul[1]

    def draw(self): 
        self.screen.blit(self.score_image, self.score_rect)


class Scoreboard():
    def __init__(self, game):
        self.game = game
        self.stats = game.stats
        screen = game.screen
        sr = screen.get_rect()
        self.bg_color = game.bg_color
        font = pg.font.SysFont(None, 48)

        self.score = SbElement(screen=screen, bg_color=game.bg_color,
                               ul=(sr.right - 40, 20), font=font, 
                               get_score=self.stats.get_score, highscore=False)
        self.highscore = SbElement(screen=screen, bg_color=game.bg_color,
                                   ul=(sr.centerx - 60, 20), font=font,
                                   get_score=self.stats.get_highscore,highscore=True)
        self.level = SbElement(screen=screen, bg_color=game.bg_color,
                                   ul=(sr.right - 40, 50), font=font, 
                                   get_score=self.stats.get_level, round=False,highscore=False)

        self.ships = Group()
        self.update()

    def update_ships(self):
        self.ships = Group()
        for n in range(self.stats.get_ships_left()):
            ship = Ship(game=self.game)
            ship.rect.x = 10 + n * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    
    def update(self): 
        self.score.update()
        self.highscore.update()
        self.level.update()
        self.update_ships()

    def draw_ships(self):
        for ship in self.ships:
            ship.draw()

    def draw(self): 
        self.score.draw()
        self.highscore.draw()
        self.level.draw()
        self.draw_ships()
