import pygame as pg
from src import ui

CELL_WIDTH = 32
CELL_HEIGHT = 32
HOLE_WIDTH = 8
HOLE_HEIGHT = 8


class Board:
    """Board is made out of board"""
    def __init__(self, rows: int, cols: int, x: float, y: float, board_color: pg.color, hole_color: pg.color):
        self.rows = rows
        self.cols = cols
        self.x = x
        self.y = y
        self.board_color = board_color
        self.pin_color = hole_color
        self.rect = pg.Rect(x, y, CELL_WIDTH*cols, CELL_HEIGHT*rows)
        init_pos_x: float
        init_pos_y: float
        init_pos_x = x + (CELL_WIDTH - HOLE_WIDTH)/2
        init_pos_y = y + (CELL_HEIGHT - HOLE_HEIGHT)/2
        self.pins: list[ui.Button]
        self.pins = [[ui.Button(init_pos_x + i*CELL_WIDTH, init_pos_y + j*CELL_HEIGHT, HOLE_WIDTH, HOLE_HEIGHT, [(120, 120, 120)], (120, 0, 120)) for i in range(0, cols)] for j in range(0, rows)]

    def draw(self, screen: pg.Surface, mouse_state: [bool, (int, int)]) -> None:
        pg.draw.rect(screen, self.board_color, self.rect)
        for p_row in self.pins:
            for p in p_row:

                pos = mouse_state[1]
                is_mouse_over = p.is_mouse_over(pos)
                p.set_hover(is_mouse_over)

                if is_mouse_over:
                    clicked = mouse_state[0]
                    if clicked:
                        p.next_click()

                p.draw(screen)
        pg.display.flip()