import pygame as pg

from src import ui
from src import board

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

(screen, buttons) = ui.construct_display()

main_board: board.Board = board.Board(8, 4, 10, 10)
# evaluate_board = board.Board(4, 10, 10, 280, (252, 178, 50), board.SMALL_PIN_WIDTH, board.SMALL_PIN_HEIGHT,
#                             board.RESPONSE_PINS_LIST)

run: bool = True
while run:
    clicked: bool = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            clicked = True
            pos: (int, int) = event.pos
            mouse_button: int = event.button
            if mouse_button == 1:  # left click
                # put here actions associated with specific mouse position e.g. clicking a specific box on the screen
                continue
            elif mouse_button == 3:  # right click
                # same as above
                continue
        elif event.type == pg.MOUSEMOTION:
            pos: (int, int) = event.pos
            rel: (int, int) = event.rel
            event_buttons: list[int] = event.buttons
        elif event.type == pg.MOUSEBUTTONUP:
            pos: (int, int) = event.pos
            mouse_button: int = event.button
        elif event.type == pg.KEYDOWN:
            unicode: str = event.unicode
            key: int = event.key
            mod: int = event.mod
            # event handling for specific key
        elif event.type == pg.KEYUP:
            key: int = event.key
            mod: int = event.mod
            # event handling for specific key

    pg.display.flip()
    # ui.ui(screen, (clicked, pg.mouse.get_pos()), buttons)
    main_board.draw(screen, (clicked, pg.mouse.get_pos()))
    # evaluate_board.draw(screen, (clicked, pg.mouse.get_pos()))

pg.quit()
