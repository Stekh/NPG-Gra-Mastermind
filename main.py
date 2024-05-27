import sys
import pygame as pg

from src import board
from src import heuristics as hr
from src import ui

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# (screen, buttons) = ui.construct_display()
screen = ui.construct_display()

rows: int = 8
cols: int = 4
no_rds: int = 5
max_rds: int = 10
start_as_guessing: bool = True

if "--rows" in sys.argv:
    rows = int(sys.argv[sys.argv.index("--rows") + 1])
if "--cols" in sys.argv:
    cols = int(sys.argv[sys.argv.index("--cols") + 1])

main_board: board.Board = board.Board(rows, cols, 10, 10)
main_board.set_random_secret()

adv_button: ui.UniversalButton = ui.UniversalButton(700, 50, 80, 40, False, pg.Color(252, 178, 50),
                                                    pg.Color(200, 178, 50), )
# evaluate_board = board.Board(4, 10, 10, 280, (252, 178, 50), board.SMALL_PIN_WIDTH, board.SMALL_PIN_HEIGHT,
#                             board.RESPONSE_PINS_LIST)

# list of used fonts:
font_endscreen: pg.font.Font = pg.font.Font(None, 80)
font: pg.font.Font = pg.font.Font(None, 40)

menu: ui.Menu = ui.Menu(screen, font)
menu2: ui.Menu2 = ui.Menu2(screen, font, no_rds, max_rds)
stage: str = "Menu"
diff: int = 0
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

    # background:
    pg.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))

    # main program loop:
    match stage:
        case "Menu":
            menu.update([clicked, pg.mouse.get_pos()])
            menu.draw()
            if menu.Easy.clicked:
                diff = 0
                stage = "Menu2"
            if menu.Medium.clicked:
                diff = 1
                stage = "Menu2"
            if menu.Hard.clicked:
                diff = 2
                stage = "Menu2"
            if menu.Exit.clicked:
                run = False
        case "Menu2":
            menu2.update([clicked, pg.mouse.get_pos()])
            no_rds = menu2.no_rounds
            start_as_guessing = menu2.guessing_status
            menu2.draw()
            if menu2.Start.clicked:
                stage = "Game"
            if menu2.Exit.clicked:
                run = False
        case "Game":
            # ui.ui(screen, (clicked, pg.mouse.get_pos()), buttons)
            main_board.draw(screen, (clicked, pg.mouse.get_pos()))
            adv_button.draw(screen)

            # text for "next turn" button
            text = font.render("next turn", True, "white", None, 1000)
            text_block = text.get_rect()
            text_block.center = (720, 32)
            screen.blit(text, text_block)

            # turn advance button:
            adv_button.update([clicked, pg.mouse.get_pos()])
            if adv_button.clicked:
                points: int = hr.advance_row(main_board)

            # endscreen text printing
            if points == 0:
                ui.draw_endscreen(screen, font_endscreen, "You win!")
            elif points == 2:
                ui.draw_endscreen(screen, font_endscreen, "You lose!")
            # evaluate_board.draw(screen, (clicked, pg.mouse.get_pos()))
        case _:
            stage = "Menu"

    pg.display.flip()

pg.quit()
