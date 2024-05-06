import pygame as pg
from src import ui

CELL_WIDTH = 64
CELL_HEIGHT = 64
PIN_WIDTH = 32
PIN_HEIGHT = 32
HOLE_WIDTH = 8
HOLE_HEIGHT = 8


class Board:
    """Board is made out of board"""
    def __init__(self, rows: int, cols: int, x: float, y: float, board_color: pg.color):
        self.rows = rows
        self.cols = cols
        self.x = x
        self.y = y
        self.board_color = board_color
        self.rect = pg.Rect(x, y, CELL_WIDTH*cols, CELL_HEIGHT*rows)
        init_pos_x: float
        init_pos_y: float
        init_pos_x = x + (CELL_WIDTH - HOLE_WIDTH)/2
        init_pos_y = y + (CELL_HEIGHT - HOLE_HEIGHT)/2
        self.pins: list[ui.Button]
        self.pins = [[ui.Button(init_pos_x + i*CELL_WIDTH, init_pos_y + j*CELL_HEIGHT, HOLE_WIDTH, HOLE_HEIGHT, [(0,0,0), (255, 23, 23), (246, 250, 42), (22, 245, 33), (10, 216, 252),
                    (255, 0, 255)], (219, 217, 217)) for i in range(0, cols)] for j in range(0, rows)]

    def draw(self, screen: pg.Surface, mouse_state: [bool, (int, int)]) -> None:
        pg.draw.rect(screen, self.board_color, self.rect)
        for i in range(0,self.rows):
            for j in range(0,self.cols):

                pos = mouse_state[1]
                is_mouse_over = self.pins[i][j].is_mouse_over(pos)
                self.pins[i][j].set_hover(is_mouse_over)

                if is_mouse_over:
                    clicked = mouse_state[0]
                    if clicked:
                        self.pins[i][j].next_click()

                    if self.pins[i][j].click_count == 1:
                        init_pos_x: float
                        init_pos_y: float
                        init_pos_x = self.x + (CELL_WIDTH - HOLE_WIDTH) / 2
                        init_pos_y = self.y + (CELL_HEIGHT - HOLE_HEIGHT) / 2
                        self.pins[i][j].rect = pg.Rect(init_pos_x + j*CELL_WIDTH + HOLE_WIDTH/2 - PIN_WIDTH/2, init_pos_y + i*CELL_HEIGHT + HOLE_HEIGHT/2 - PIN_HEIGHT/2, PIN_WIDTH, PIN_HEIGHT)

                    if self.pins[i][j].click_count == 6:
                        self.pins[i][j].click_count = 0
                        init_pos_x: float
                        init_pos_y: float
                        init_pos_x = self.x + (CELL_WIDTH - HOLE_WIDTH) / 2
                        init_pos_y = self.y + (CELL_HEIGHT - HOLE_HEIGHT) / 2
                        self.pins[i][j].rect = pg.Rect(init_pos_x + j*CELL_WIDTH, init_pos_y + i*CELL_HEIGHT, HOLE_WIDTH, HOLE_HEIGHT)


                self.pins[i][j].draw(screen)
        pg.display.flip()