import pygame as pg
from src.ui import ui

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Mastermind")

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    ui(screen)


pg.quit()
