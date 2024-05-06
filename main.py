import pygame as pg

from src import ui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

(screen, buttons) = ui.construct_display(SCREEN_WIDTH, SCREEN_HEIGHT)

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
