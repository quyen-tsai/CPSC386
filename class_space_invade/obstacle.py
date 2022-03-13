import pygame as pg
from pygame.sprite import Group, Sprite

GREEN = (78, 255, 87)
class Blocker(Sprite):
    def __init__(self, size, color, row, column, game):
        Sprite.__init__(self)
        self.game = game
        self.screen = game.screen
        self.height = size
        self.width = size
        self.color = color
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.column = column

    def update(self):
        self.game.screen.blit(self.image, self.rect)



class Blockers:
    def __init__(self,game):
        self.game = game


    def create_blockers(self):
        self.allBlockers = Group(self.make_blockers(0),
                                 self.make_blockers(1.5),
                                 self.make_blockers(3),
                                 self.make_blockers(5))

    def kill(self):
        self.allBlockers.empty()

    def make_blockers(self, number):
        blockerGroup = Group()
        for row in range(4):
            for column in range(12):
                blocker = Blocker(10, GREEN, row, column, game=self.game)
                blocker.rect.x = 50 + (200 * number) + (column * blocker.width)
                blocker.rect.y = 600 + (row * blocker.height)
                blockerGroup.add(blocker)
        return blockerGroup

    def check_collide(self):
        if len(self.allBlockers) > 0:
            pg.sprite.groupcollide(self.game.lasers.lasers, self.allBlockers, True, True)
            pg.sprite.groupcollide(self.game.alien_fleet.enemy_bullets, self.allBlockers, True, True)
            pg.sprite.groupcollide(self.game.alien_fleet.fleet, self.allBlockers, True, True)

    def update(self):
        self.allBlockers.update()
