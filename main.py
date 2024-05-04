import pygame as pg

pg.init()

screen = pg.display.set_mode((100, 100))

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = event.pos
            button = event.button
            if button == 1:  # left click
                # put here actions associated with specific mouse position e.g. clicking a specific box on the screen
                continue
            elif button == 3:  # right click
                # same as above
                continue
        elif event.type == pg.MOUSEMOTION:
            pos = event.pos
            rel = event.rel
            buttons = event.buttons
        elif event.type == pg.MOUSEBUTTONUP:
            pos = event.pos
            button = event.button
        elif event.type == pg.KEYDOWN:
            unicode = event.unicode
            key = event.key
            mod = event.mod
            # event handling for specific key
        elif event.type == pg.KEYUP:
            key = event.key
            mod = key.mod
            # event handling for specific key


pg.quit()
