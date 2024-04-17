import pygame as pg

pg.init()

screen = pg.display.set_mode((100, 100))

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


pg.quit()
