#!/usr/bin/env python
from builtins import classmethod

import pgzero
from pgzero.screen import Screen
from pgzero.loaders import ImageLoader, SoundLoader
from pgzero.keyboard import Keyboard
from pgzero.constants import mouse
from pgzero.clock import clock
from pgzero.actor import Actor
from pgzero.rect import Rect, ZRect

import pygame
import pygame.time

from pgzero.ptext import getfont
#from pgzero.animation import Animation

from pgzero.game import PGZeroGame
from pgzero import clock, music, tone

pgzero.ptext.DEFAULT_FONT_NAME = 'tomorrow-regular'


print("Strar")
WIDTH = 800
HEIGHT = 600
GAP = 10

import pgzrun
'''
if pgzrun.__name__ == 'qwe':
    pgzero = module()
    clock = module()
    music = module()
    tone = module()
    Actor = type()
    keyboard = Keyboard()
    animate = function()
    Rect = type()
    ZRect = type()
    images = ImageLoader()
    sounds = SoundLoader()
    mouse = EnumMeta()
    keys = EnumMeta()
    keymods = EnumMeta()
    exit = function()
    pgzrun = module()
    #draw = function()
    screen = Screen()
'''

class Scene:
    MAX_TIME = 3.0
    bottles = []
    time_left = MAX_TIME
    def tick(self, dt):
        self.time_left -= dt


class GameSession:
    scene = Scene()
    def tick(self, dt):
        self.scene.tick(dt)
        if self.scene.time_left < 0:
            self.scene = Scene()

GS = GameSession()

def update(dt):
    GS.tick(dt)

MX = 0
MY = 0
def on_mouse_move(pos, rel, buttons):
    global MX, MY
    MX, MY = pos

def draw():
    #screen = pgzero.game.screen
    global screen
    assert isinstance(screen, Screen)
    font = getfont(fontname="tomorrow-regular", fontsize=32)
    screen.clear()
    screen.draw.text("Hello World", pos=(100, 100), fontname="tomorrow-regular", fontsize=32)

    screen.draw.text("DEFAULT_FONT_NAME", pos=(300, 100))

    screen.draw.text(str(GS.scene.time_left), pos=(30, 10))
    screen.draw.circle((400, 300), 30, 'white')


    # draw background
    # draw bottles
    bottles=[
        (100, 100), (200, 100),(300, 100),
        (100, 200), (200, 200),(300, 200),
        (100, 300), (200, 300),(300, 300),
    ]

    bottle_width=60
    bottle_height=90
    for x, y in bottles:
        screen.draw.rect(Rect(x, y, bottle_width, bottle_height), 'brown')

        # draw bullets/stones/lasso/tomahawks/effects
    # draw smoke
    # draw timer
    bar_width = 100
    tl = bar_width / GS.scene.MAX_TIME * GS.scene.time_left

    screen.draw.filled_rect(Rect(WIDTH - bar_width - GAP, HEIGHT - 20 - GAP,
                                 tl, 20), 'red')
    # draw crosshair
    screen.draw.circle((MX, MY), 20, 'white')
    # draw FPS

    # ???



    #i=0
    #for i in globals():
    #    print (i, '=', type(globals()[i]).__name__, '()')



'''

#import gamelib

if False:
    class Mod:
        @staticmethod
        def draw():
            global draw
            draw()
    DISPLAY_FLAGS = 0
    m=Mod()
    pgzero.loaders.set_root('.')
    PGZeroGame.show_default_icon()
    pygame.display.set_mode((100, 100), DISPLAY_FLAGS)
    from pgzero.builtins import *
    from pgzero.game import screen
    #m.__dict__.update(builtins.__dict__)
    PGZeroGame(m).run()

if __name__ == '__main__':
    #gamelib.run()
    pass
'''


pgzrun.go()