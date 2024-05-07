import pygame as pg

from src import ui
from src import board

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

(screen, buttons) = ui.construct_display()

main_board = board.Board(4, 10, 10, 10, (252, 178, 50))
evaluate_board = board.Board(4, 10, 10, 280, (252, 178, 50), board.SMALL_PIN_WIDTH, board.SMALL_PIN_HEIGHT)

run = True
while run:
    clicked = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            clicked = True
            pos = event.pos
            mouse_button = event.button
            if mouse_button == 1:  # left click
                # put here actions associated with specific mouse position e.g. clicking a specific box on the screen
                continue
            elif mouse_button == 3:  # right click
                # same as above
                continue
        elif event.type == pg.MOUSEMOTION:
            pos = event.pos
            rel = event.rel
            event_buttons = event.buttons
        elif event.type == pg.MOUSEBUTTONUP:
            pos = event.pos
            mouse_button = event.button
        elif event.type == pg.KEYDOWN:
            unicode = event.unicode
            key = event.key
            mod = event.mod
            # event handling for specific key
        elif event.type == pg.KEYUP:
            key = event.key
            mod = key.mod
            # event handling for specific key

    # ui.ui(screen, (clicked, pg.mouse.get_pos()), buttons)
    main_board.draw(screen, (clicked, pg.mouse.get_pos()))
    evaluate_board.draw(screen, (clicked, pg.mouse.get_pos()))

pg.quit()
