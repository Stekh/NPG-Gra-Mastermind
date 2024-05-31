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
rd_ctr: int = 0
wins: int = 0
losses: int = 0

if "--rows" in sys.argv:
    rows = int(sys.argv[sys.argv.index("--rows") + 1])
if "--cols" in sys.argv:
    cols = int(sys.argv[sys.argv.index("--cols") + 1])

main_board: board.Board = board.Board(rows, cols, 10, 10)
adv_button: ui.UniversalButton = ui.UniversalButton(700, 50, 80, 40, False, pg.Color(252, 178, 50),
                                                    pg.Color(200, 178, 50), )
# evaluate_board = board.Board(4, 10, 10, 280, (252, 178, 50), board.SMALL_PIN_WIDTH, board.SMALL_PIN_HEIGHT,
#                             board.RESPONSE_PINS_LIST)

# list of used fonts:
font_endscreen: pg.font.Font = pg.font.Font(None, 80)
font: pg.font.Font = pg.font.Font(None, 40)

menu: ui.Menu = ui.Menu(screen, font)
menu2: ui.Menu2 = ui.Menu2(screen, font, no_rds, max_rds)
scoreboard: ui.Scoreboard = ui.Scoreboard(screen, font)

game_over_text: pg.Surface = font.render("Game over!", False, "white", None)
game_over_block: pg.Rect = game_over_text.get_rect()
game_over_block.center = (200, 200)

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
                rows = 8
                cols = 3
                stage = "Menu2"
            if menu.Medium.clicked:
                diff = 1
                rows = 7
                cols = 4
                stage = "Menu2"
            if menu.Hard.clicked:
                diff = 2
                rows = 6
                cols = 5
                stage = "Menu2"
            if menu.Exit.clicked:
                run = False
        case "Menu2":
            menu2.update([clicked, pg.mouse.get_pos()])
            no_rds = menu2.no_rounds
            menu2.draw()
            if menu2.Start.clicked:
                del main_board
                main_board: board.Board = board.Board(rows, cols, 10, 10)
                main_board.set_random_secret()
                stage = "Game"
            if menu2.Exit.clicked:
                run = False
        case "Game":
            scoreboard.draw(wins, losses)
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
            if rd_ctr == no_rds:
                stage = "End"
            else:
                if points == 0:
                    points = -1
                    del main_board
                    main_board: board.Board = board.Board(rows, cols, 10, 10)
                    main_board.set_random_secret()
                    rd_ctr += 1
                    wins += 1
                    stage = "Game"

                elif points == 2:
                    points = -1
                    del main_board
                    main_board: board.Board = board.Board(rows, cols, 10, 10)
                    main_board.set_random_secret()
                    losses += 1
                    rd_ctr += 1
                    stage = "Game"
            # evaluate_board.draw(screen, (clicked, pg.mouse.get_pos()))
        case "End":
            scoreboard.draw(wins, losses)
            screen.blit(game_over_text, game_over_block)
            if clicked:
                no_rds: int = 5
                rd_ctr = 0
                wins = 0
                losses = 0
                stage = "Menu"
        case _:
            stage = "Menu"

    pg.display.flip()

pg.quit()
