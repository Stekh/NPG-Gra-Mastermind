import pygame as pg
from src import ui

CELL_WIDTH = 32
CELL_HEIGHT = 32
HOLE_WIDTH = 8
HOLE_HEIGHT = 8
class Board:
    """Board is made out of board"""

    def __init__(self, rows: int, cols: int, x: float, y: float, board_color: pg.color, pin_color: pg.color):
        self.rows = rows
        self.cols = cols
        self.x = x
        self.y = y
        self.board_color = board_color
        self.pin_color = pin_color
        self.rect = pg.Rect(x, y, width, height)
