#!/usr/bin/env python3
"""author << Anonim_007 >>"""

from typing import Sequence

# Version
version: float = 0.1

# Type aliases
Resolution = tuple[int, int]
RGB = tuple[int, int, int]
PhrasesTuple = Sequence[str]
SurfFill = tuple[int, int, int, int]

# Screen settings
WIDTH_APP: int = 1000
HEIGHT_APP: int = 700
RES_APP: Resolution = (WIDTH_APP, HEIGHT_APP)

# Title window
TITLE: str = f"Слава Україні матриця v{version}"
# Surface fill
FILL: SurfFill = (0, 0, 0, 17)
# FPS app (speed depends on it)
FPS: int = 10

# Chance of falling matrix column
CHANCE = 97

# Font config
FONT_SIZE: int = 14
FONT_FAMILY: str = 'arial'
FONT_BOLD: bool = True

# Colors in RGB formats
GREEN: RGB = (52, 191, 61)
RED: RGB = (255, 0, 0)
YELLOW: RGB = (255, 239, 17)
BLUE: RGB = (17, 191, 255)

# Text matrix
PHRASES: PhrasesTuple = (
    "ПУТІН ХУЙЛО ",
    "ПУТІН ХУЙЛО ",
    "РОСІЙСЬКИЙ ВОЄННИЙ КОРАБЕЛЬ, ПІШОВ НАХУЙ ",
    "СМЕРТЬ РОСІЙСТКІЙ ФЕДЕРАЦІЇ "
)

PHRASES_2: PhrasesTuple = (
    "СЛАВА УКРАЇНІ ",
    "БАТЬКО НАШ БАНДЕРА ",
    "СЛАВА ЗСУ ",
    "ГЕРОЯМ СЛАВА "
)

# Tuple of phrases to drawing
USE_PHRASES: PhrasesTuple = PHRASES_2
