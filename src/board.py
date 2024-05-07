import pygame as pg
from src import ui

CELL_WIDTH = 64
CELL_HEIGHT = 64
COLOR_PIN_WIDTH = 32
COLOR_PIN_HEIGHT = 32
RESPONSE_PIN_WIDTH = 16
RESPONSE_PIN_HEIGHT = 16
HOLE_WIDTH = 8
HOLE_HEIGHT = 8
BOARD_COLOR = (252, 178, 50)
LINE_COLOR = (158, 121, 0)
COLOR_PINS_LIST = [(0, 0, 0), (255, 23, 23), (246, 250, 42), (22, 245, 33), (10, 216, 252),
                   (255, 0, 255)]
RESPONSE_PINS_LIST = [(0, 0, 0), (255, 255, 255), (0, 0, 0)]


class Board:
    """Board is made out of board"""

    def __init__(self, rows: int, cols: int, x: float, y: float):
        self.rows = rows
        self.cols = cols
        self.x = x
        self.y = y
        self.color_pin_width = COLOR_PIN_WIDTH
        self.color_pin_height = COLOR_PIN_HEIGHT
        self.response_pin_width = RESPONSE_PIN_WIDTH
        self.response_pin_height = RESPONSE_PIN_HEIGHT
        self.board_color = BOARD_COLOR
        self.line_color = LINE_COLOR
        self.color_pin_colors = COLOR_PINS_LIST
        self.response_pin_colors = RESPONSE_PINS_LIST
        self.board = pg.Rect(x, y, CELL_WIDTH * cols, CELL_HEIGHT * rows * 2 + 10)
        self.line = pg.Rect(x + 2, y + rows * CELL_HEIGHT + 3, CELL_WIDTH * cols - 4, 4)
        self.secret = pg.Rect(x + cols * CELL_WIDTH, y, CELL_WIDTH, rows * CELL_HEIGHT)
        init_pos_x: float
        init_pos_y: float
        init_pos_x = x + (CELL_WIDTH - HOLE_WIDTH) / 2
        init_pos_y = y + (CELL_HEIGHT - HOLE_HEIGHT) / 2
        self.pins: list[ui.Button]
        self.color_pins = [
            [ui.Button(init_pos_x + i * CELL_WIDTH, init_pos_y + j * CELL_HEIGHT, HOLE_WIDTH, HOLE_HEIGHT,
                       self.color_pin_colors, (219, 217, 217)) for i in range(0, cols)] for j in range(0, rows)]
        self.response_pins = [
            [ui.Button(init_pos_x + i * CELL_WIDTH, init_pos_y + (j + rows) * CELL_HEIGHT + 10,
                       HOLE_WIDTH, HOLE_HEIGHT, self.response_pin_colors, (219, 217, 217)) for i in range(0, cols)] for
            j in range(0, rows)]
        self.secret_line = [
            ui.Button(init_pos_x + cols * CELL_WIDTH, init_pos_y + i * CELL_HEIGHT, HOLE_WIDTH, HOLE_HEIGHT,
                      self.color_pin_colors, (219, 217, 217)) for i in range(0, rows)]

    def draw(self, screen: pg.Surface, mouse_state: [bool, (int, int)]) -> None:
        pg.draw.rect(screen, self.board_color, self.board)
        pg.draw.rect(screen, self.line_color, self.line)
        pg.draw.rect(screen, self.board_color, self.secret)
        for i in range(0, self.rows):
            for j in range(0, self.cols):

                pos = mouse_state[1]
                is_mouse_over = self.color_pins[i][j].is_mouse_over(pos)
                self.color_pins[i][j].set_hover(is_mouse_over)

                if is_mouse_over:
                    clicked = mouse_state[0]
                    if clicked:
                        self.color_pins[i][j].next_click()

                    if self.color_pins[i][j].click_count == 1:
                        init_pos_x: float
                        init_pos_y: float
                        init_pos_x = self.x + CELL_WIDTH / 2
                        init_pos_y = self.y + CELL_HEIGHT / 2
                        self.color_pins[i][j].rect = pg.Rect(init_pos_x + j * CELL_WIDTH - self.color_pin_width / 2,
                                                             init_pos_y + i * CELL_HEIGHT - self.color_pin_height / 2,
                                                             self.color_pin_width, self.color_pin_height)

                    if self.color_pins[i][j].click_count == len(self.color_pin_colors):
                        self.color_pins[i][j].click_count = 0
                        init_pos_x: float
                        init_pos_y: float
                        init_pos_x = self.x + (CELL_WIDTH - HOLE_WIDTH) / 2
                        init_pos_y = self.y + (CELL_HEIGHT - HOLE_HEIGHT) / 2
                        self.color_pins[i][j].rect = pg.Rect(init_pos_x + j * CELL_WIDTH, init_pos_y + i * CELL_HEIGHT,
                                                             HOLE_WIDTH, HOLE_HEIGHT)

                is_mouse_over = self.response_pins[i][j].is_mouse_over(pos)
                self.response_pins[i][j].set_hover(is_mouse_over)

                if is_mouse_over:
                    clicked = mouse_state[0]
                    if clicked:
                        self.response_pins[i][j].next_click()

                    if self.response_pins[i][j].click_count == 1:
                        init_pos_x: float
                        init_pos_y: float
                        init_pos_x = self.x + CELL_WIDTH / 2
                        init_pos_y = self.y + CELL_HEIGHT / 2
                        self.response_pins[i][j].rect = pg.Rect(
                            init_pos_x + j * CELL_WIDTH - self.response_pin_width / 2,
                            init_pos_y + (i + self.rows) * CELL_HEIGHT + 10 - self.response_pin_height / 2,
                            self.response_pin_width, self.response_pin_height)

                    if self.response_pins[i][j].click_count == len(self.response_pin_colors):
                        self.response_pins[i][j].click_count = 0
                        init_pos_x: float
                        init_pos_y: float
                        init_pos_x = self.x + (CELL_WIDTH - HOLE_WIDTH) / 2
                        init_pos_y = self.y + (CELL_HEIGHT - HOLE_HEIGHT) / 2
                        self.response_pins[i][j].rect = pg.Rect(init_pos_x + j * CELL_WIDTH,
                                                                init_pos_y + (i + self.rows) * CELL_HEIGHT + 10,
                                                                HOLE_WIDTH, HOLE_HEIGHT)

                self.color_pins[i][j].draw(screen)
                self.response_pins[i][j].draw(screen)

            pos = mouse_state[1]
            is_mouse_over = self.secret_line[i].is_mouse_over(pos)
            self.secret_line[i].set_hover(is_mouse_over)

            if is_mouse_over:
                clicked = mouse_state[0]
                if clicked:
                    self.secret_line[i].next_click()

                if self.secret_line[i].click_count == 1:
                    init_pos_x: float
                    init_pos_y: float
                    init_pos_x = self.x + CELL_WIDTH / 2
                    init_pos_y = self.y + CELL_HEIGHT / 2
                    self.secret_line[i].rect = pg.Rect(init_pos_x + self.cols * CELL_WIDTH - self.color_pin_width / 2,
                                                       init_pos_y + i * CELL_HEIGHT - self.color_pin_height / 2,
                                                       self.color_pin_width, self.color_pin_height)

                if self.secret_line[i].click_count == len(self.color_pin_colors):
                    self.secret_line[i].click_count = 0
                    init_pos_x: float
                    init_pos_y: float
                    init_pos_x = self.x + (CELL_WIDTH - HOLE_WIDTH) / 2
                    init_pos_y = self.y + (CELL_HEIGHT - HOLE_HEIGHT) / 2
                    self.secret_line[i].rect = pg.Rect(init_pos_x + self.cols * CELL_WIDTH,
                                                         init_pos_y + i * CELL_HEIGHT,
                                                         HOLE_WIDTH, HOLE_HEIGHT)

            self.secret_line[i].draw(screen)

        pg.display.flip()
