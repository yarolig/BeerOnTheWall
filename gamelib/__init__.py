#!/usr/bin/env python
# coding: utf-8


# Reinvent UI


class Style:
    fgcolor = 0xFFffFF
    inactive_fgcolor = 0x888888


class Gui:
    def __init__(self):
        self.active_menu = None

    def draw_text(self, x, y, text, color=Style.fgcolor):
        pass

    def on_click(self, x, y):
        pass


class MenuItem:
    name = ''
    text = ''
    type = 'button'
    inactive = False
    x = 0
    y = 0
    xx = 0
    yy = 0


class Menu:
    def __init__(self, gui):
        self._gui = gui
        self.items = []

    def add_item(self, text):
        pass

    def draw(self):
        pass

'''
-----------------
Continue
New Game
Options
About
Exit
----------------
'''






import pgzrun

def draw():
    screen.clear()
    screen.draw.circle((400, 300), 30, 'white')
pgzrun.go()









def run():
    pass