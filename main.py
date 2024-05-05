import pygame as pg

from src import ui

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Mastermind")

buttons = ui.construct_buttons()

run = True
while run:
    clicked = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            clicked = True
    ui.ui(screen, (clicked, pg.mouse.get_pos()), buttons)

pg.quit()
