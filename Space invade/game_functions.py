import sys
import pygame as pg
from vector import Vector
from game import Laser

# def check_events(game):
#     ship = game.ship
#     RIGHT = Vector(1,0)
#     LEFT = Vector(-1,0)
#     UP = Vector(0,-1)
#     DOWN = Vector(0,1)
#     """Respond to key presses and mouse events."""
#     for e in pg.event.get():
#         if e.type == pg.QUIT:
#             sys.exit()
#         elif e.type == pg.KEYDOWN:
#             key = e.key
#             if key == pg.K_RIGHT:
#                 ship.moving(RIGHT)
#             elif key == pg.K_LEFT:
#                 ship.moving(LEFT)
#             elif key == pg.K_UP:
#                 ship.moving(UP)
#             elif key == pg.K_DOWN:
#                 ship.moving(DOWN)
#             if key == pg.K_SPACE:
#                 newlaser = Laser(game)
#                 game.lasers.add(newlaser)

def check_events(game):
    ship = game.ship
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            check_keydown_events(event, ship)
        if event.type == pg.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship):
    if event.key == pg.K_LEFT:
        ship.moving_left = True
    if event.key == pg.K_RIGHT:
        ship.moving_right = True
    if event.key == pg.K_UP:
        ship.moving_up = True
    if event.key == pg.K_DOWN:
        ship.moving_down = True
    if event.key == pg.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pg.K_LEFT:
        ship.moving_left = False
    if event.key == pg.K_RIGHT:
        ship.moving_right = False
    if event.key == pg.K_UP:
        ship.moving_up = False
    if event.key == pg.K_DOWN:
        ship.moving_down = False
