import pygame as pg

WSIZE = (720, 480)
TSIDE = 30
MSIZE = WSIZE[0] // TSIDE, WSIZE[1] // TSIDE

COLOR_BG = "black"
COLOR_SNAKE = "green"
COLOR_APPLE = "red"
COLOR_SCORE = "yellow"
COLOR_TEXT = "white"

FPS_START = 5

pg.font.init()
FONT_SCORE = pg.font.SysFont("Arial", 25)
FONT_GAMEOVER = pg.font.SysFont("Arial", 45)
FONT_SPACE = pg.font.SysFont("Arial", 18)
