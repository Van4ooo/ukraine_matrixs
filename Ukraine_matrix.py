#!/usr/bin/env python3
"""
Слава Україні, Героям слава
Матриця для:
    Підняття морального духу
    Для кайфу і релаксу

Путін хуйло
developer: https://t.me/van4o_0
"""

import pygame as pg
import random

from config import *


class MatrixSymbol:
    """
    This class in the role Custom Iterators
    This working by __iter__() and the __next__() methods.

    The __iter__() method returns the iterator object itself.
    Initializes a variable self.index_columns,\
    with a value of 0 as the beginning of the iteration.

    The __next__() method must return the next symbol to drawing and index of column.
    """
    def __init__(self, col):
        self._phrases = USE_PHRASES
        self._columns = col

        self._len_phrases = self._phrases.__len__()

        self._drops = [1 for _ in range(self._columns)]
        self._phrases_point = [
            random.randint(0, self._len_phrases - 1)
            for _ in range(self._columns)
        ]
        self._pos_char = [
            random.randint(0, self._get_len_ph(i) - 1)
            for i in range(self._columns)
        ]

    def __iter__(self):
        self.index_columns = 0

        return self

    def __next__(self):
        if self.index_columns + 1 < self._columns:
            return (
                self._now_render_symbol(),
                self.index_columns
            )
        raise StopIteration

    def _now_render_symbol(self) -> str:
        phrases_i = self._phrases_point[self.index_columns]
        symbol_i = self._pos_char[self.index_columns]

        return self._phrases[phrases_i][symbol_i]

    def _new_phrases_point(self):
        if self._pos_char[self.index_columns] == self._get_len_ph():
            self._phrases_point[self.index_columns] = random.choice([
                x for x in range(self._len_phrases)
                if x != self._phrases_point[self.index_columns]
            ])
            self._pos_char[self.index_columns] = 0

    def _get_len_ph(self, i: int = None) -> int:
        i = self.index_columns if i is None else i

        return self._phrases[self._phrases_point[i]].__len__()

    def get_drop(self) -> int:
        return self._drops[self.index_columns]

    def add(self, new: bool):
        if new:
            self._drops[self.index_columns] = 0
        else:
            self._drops[self.index_columns] += 1
            self._pos_char[self.index_columns] += 1

        self._new_phrases_point()
        self.index_columns += 1


class MatrixSymbolDraw:
    """
    Drawing class, draw symbol of matrix

    Here the main parameters of the symbol are configured
    The configuration is taken from a file config.py

    Class method MatrixSymbolDraw.draw() drawing one symbol of\
    falling matrix column
    """

    def __init__(self, app):
        self.app = app
        self.phrases = PHRASES_2
        self.font_size = FONT_SIZE

        self.font = pg.font.SysFont(FONT_FAMILY, self.font_size, bold=FONT_BOLD)
        self.columns = app.RES[0] // self.font_size

        self.symbol = MatrixSymbol(col=self.columns)

    def draw(self):
        for char, i in self.symbol:
            self._render_symbol(char=char, i=i)
            self._new_columns_falling()

    def _render_symbol(self, char: str, i: int):
        char_render = self.font.render(char, False, self._color())

        pos = (i * self.font_size, (self.symbol.get_drop() - 1) * self.font_size)
        self.app.surface.blit(char_render, pos)

    def _new_columns_falling(self):
        lower_limit = self.symbol.get_drop() * self.font_size > self.app.RES[1]
        ch = random.randint(0, 100) > CHANCE

        self.symbol.add(new=(lower_limit and ch))

    def _color(self) -> RGB:
        status = (self.symbol.get_drop() - 1) * self.font_size >= self.app.RES[1] / 2

        return YELLOW if status else BLUE


class Matrix:
    """
    Main class, run and draw matrix

    Here the main parameters of the window are configured
    The configuration is taken from a file config.py

    Class method Matrix.run() starts the Infinite Loop to drawing of the matrix
    """

    def __init__(self):
        self.RES = RES_APP

        self.screen = pg.display.set_mode(self.RES)
        self.surface = pg.Surface(self.RES, pg.SRCALPHA)
        self.clock = pg.time.Clock()

        self.matrix_symbol_draw = MatrixSymbolDraw(self)

    def run(self):
        while True:
            self._filling_frame()
            self._check_exit()
            self._render_frame()

    def _filling_frame(self):
        self.surface.fill(FILL)
        self.matrix_symbol_draw.draw()
        self.screen.blit(self.surface, (FONT_SIZE // 2 + 3, 1))

    def _render_frame(self):
        pg.display.flip()
        self.clock.tick(FPS)

    @staticmethod
    def _check_exit():
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit(0)


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption(TITLE)

    Matrix().run()
