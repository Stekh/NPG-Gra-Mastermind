import pygame as pg

from src import board
from src import heuristics as hr
from src import ui

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# (screen, buttons) = ui.construct_display()
screen = ui.construct_display()

main_board: board.Board = board.Board(8, 4, 10, 10)
main_board.set_random_secret()

adv_button: ui.UniversalButton = ui.UniversalButton(700, 50, 80, 40, pg.Color(252, 178, 50), pg.Color(200, 178, 50), )
# evaluate_board = board.Board(4, 10, 10, 280, (252, 178, 50), board.SMALL_PIN_WIDTH, board.SMALL_PIN_HEIGHT,
#                             board.RESPONSE_PINS_LIST)

# list of used fonts:
font_endscreen: pg.font.Font = pg.font.Font(None, 80)
font: pg.font.Font = pg.font.Font(None, 40)

points: int = -1

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

    adv_button.update([clicked, pg.mouse.get_pos()])
    if adv_button.clicked:
        points: int = hr.advance_row(main_board)

    # ui.ui(screen, (clicked, pg.mouse.get_pos()), buttons)
    main_board.draw(screen, (clicked, pg.mouse.get_pos()))
    adv_button.draw(screen)

    # text for "next turn" button
    text = font.render("next turn", True, "white", None, 1000)
    text_block = text.get_rect()
    text_block.center = (720, 32)
    screen.blit(text, text_block)

    # endscreen text printing
    if points == 0:
        ui.draw_endscreen(screen, font_endscreen, "You win!")
    elif points == 2:
        ui.draw_endscreen(screen, font_endscreen, "You lose!")
    # evaluate_board.draw(screen, (clicked, pg.mouse.get_pos()))

    pg.display.flip()

pg.quit()
