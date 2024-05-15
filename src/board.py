import pygame as pg
from src import ui
from src import state

CELL_WIDTH = 64
CELL_HEIGHT = 64
COLOR_PIN_WIDTH = 32
COLOR_PIN_HEIGHT = 32
RESPONSE_PIN_WIDTH = 16
RESPONSE_PIN_HEIGHT = 16
HOLE_WIDTH = 8
HOLE_HEIGHT = 8
BOARD_COLOR = (252, 178, 50)
# HOVER_COLORS_VECTOR = (10, 10, 10)
LINE_COLOR = (158, 121, 0)
BACKLIGHT_COLOR = (250, 211, 142)
COLOR_PINS_COLORS = [(0, 0, 0), (255, 23, 23), (246, 250, 42), (22, 245, 33), (10, 216, 252),
                     (255, 0, 255)]
RESPONSE_PINS_COLORS = [(0, 0, 0), (255, 255, 255), (0, 0, 0)]


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
        self.backlight_color = BACKLIGHT_COLOR
        self.color_pin_colors = COLOR_PINS_COLORS
        self.response_pin_colors = RESPONSE_PINS_COLORS
        # self.hover_colors_vector = HOVER_COLORS_VECTOR
        self.board = pg.Rect(x, y, CELL_WIDTH * cols * 2 + 10, CELL_HEIGHT * rows)
        self.line = pg.Rect(x + cols * CELL_WIDTH + 3, y + 2, 4, CELL_HEIGHT * rows - 4)
        self.secret = pg.Rect(x, y + rows * CELL_HEIGHT, CELL_WIDTH * cols, CELL_HEIGHT)
        self.active_row_backlight = pg.Rect(x + 2, y + 2, CELL_WIDTH * cols - 4, CELL_HEIGHT - 4)
        self.state = state.Game(rows, cols, [0 for i in range(0, cols)])
        init_pos_x = x + (CELL_WIDTH - HOLE_WIDTH) / 2
        init_pos_y = y + (CELL_HEIGHT - HOLE_HEIGHT) / 2
        self.color_pins = [
            [ui.Button(init_pos_x + i * CELL_WIDTH, init_pos_y + j * CELL_HEIGHT, HOLE_WIDTH, HOLE_HEIGHT,
                       self.color_pin_colors, (255, 255, 255)) for i in
             range(0, cols)] for j in range(0, rows)]
        self.response_pins = [
            [ui.Button(init_pos_x + (i + cols) * CELL_WIDTH + 10, init_pos_y + j * CELL_HEIGHT, HOLE_WIDTH, HOLE_HEIGHT,
                       self.response_pin_colors, (255, 255, 255))
             for i in range(0, cols)] for j in range(0, rows)]
        self.secret_line = [
            ui.Button(init_pos_x + i * CELL_WIDTH, init_pos_y + rows * CELL_HEIGHT, HOLE_WIDTH, HOLE_HEIGHT,
                      self.color_pin_colors, (255, 255, 255)) for i in
            range(0, cols)]

    def update_state_after_click(self, mouse_state: [bool, (int, int)]) -> None:

        self.active_row_backlight = pg.Rect(self.x + 2, self.y + CELL_HEIGHT * self.state.get_active_row_no() + 2,
                                            CELL_WIDTH * self.cols - 4, CELL_HEIGHT - 4)

        modified_row = self.state.get_active_row_no()
        for i in range(0, self.cols):

            pos = mouse_state[1]
            is_mouse_over = self.color_pins[modified_row][i].is_mouse_over(pos)
            self.color_pins[modified_row][i].set_hover(is_mouse_over)

            if is_mouse_over:
                clicked = mouse_state[0]
                if clicked:
                    self.color_pins[modified_row][i].next_click()

                if self.color_pins[modified_row][i].click_count == 1:
                    pos_x = self.x + CELL_WIDTH / 2 + i * CELL_WIDTH - self.color_pin_width / 2
                    pos_y = self.y + CELL_HEIGHT / 2 + modified_row * CELL_HEIGHT - self.color_pin_height / 2
                    self.color_pins[modified_row][i].rect = pg.Rect(pos_x, pos_y, self.color_pin_width, self.color_pin_height)

                if self.color_pins[modified_row][i].click_count == len(self.color_pin_colors):
                    self.color_pins[modified_row][i].click_count = 0
                    pos_x = self.x + (CELL_WIDTH - HOLE_WIDTH) / 2 + i * CELL_WIDTH
                    pos_y = self.y + (CELL_HEIGHT - HOLE_HEIGHT) / 2 + modified_row * CELL_HEIGHT
                    self.color_pins[modified_row][i].rect = pg.Rect(pos_x, pos_y, HOLE_WIDTH, HOLE_HEIGHT)

            is_mouse_over = self.response_pins[modified_row][i].is_mouse_over(pos)
            self.response_pins[modified_row][i].set_hover(is_mouse_over)

            self.state.place_color_pin(self.color_pins[modified_row][i].click_count, i)

        new_combination = []
        for i in range(0, self.cols):
            pos = mouse_state[1]
            is_mouse_over = self.secret_line[i].is_mouse_over(pos)
            self.secret_line[i].set_hover(is_mouse_over)

            if is_mouse_over:
                clicked = mouse_state[0]
                if clicked:
                    self.secret_line[i].next_click()

                if self.secret_line[i].click_count == 1:
                    pos_x = self.x + CELL_WIDTH / 2 + i * CELL_WIDTH - self.color_pin_width / 2
                    pos_y = self.y + CELL_HEIGHT / 2 + self.rows * CELL_HEIGHT - self.color_pin_height / 2
                    self.secret_line[i].rect = pg.Rect(pos_x, pos_y, self.color_pin_width, self.color_pin_height)

                if self.secret_line[i].click_count == len(self.color_pin_colors):
                    self.secret_line[i].click_count = 0
                    pos_x = self.x + (CELL_WIDTH - HOLE_WIDTH) / 2 + i * CELL_WIDTH
                    pos_y = self.y + (CELL_HEIGHT - HOLE_HEIGHT) / 2 + self.rows * CELL_HEIGHT
                    self.secret_line[i].rect = pg.Rect(pos_x, pos_y, HOLE_WIDTH, HOLE_HEIGHT)

            new_combination.append(self.secret_line[i].click_count)

        self.state.set_combination(new_combination)

    def update_state_after_evaluation(self) -> None:

        self.active_row_backlight = pg.Rect(self.x + 2, self.y + CELL_HEIGHT * self.state.get_active_row_no() + 2,
                                            CELL_WIDTH * self.cols - 4, CELL_HEIGHT - 4)

        active_row_storage = self.state.get_active_row_no()  # temporary
        for i in range(0, self.rows):
            self.state.set_active_row(i)
            for j in range(0, self.cols):

                self.response_pins[i][j].click_count = self.state.get_response_pin_color(i, j)

                if self.response_pins[i][j].click_count > 0:
                    pos_x = self.x + CELL_WIDTH / 2 + (
                            j + self.cols) * CELL_WIDTH + 10 - self.response_pin_width / 2
                    pos_y = self.y + CELL_HEIGHT / 2 + i * CELL_HEIGHT - self.response_pin_height / 2
                    self.response_pins[i][j].rect = pg.Rect(pos_x, pos_y, self.response_pin_width,
                                                            self.response_pin_height)
                else:
                    pos_x = self.x + (CELL_WIDTH - HOLE_WIDTH) / 2 + (j + self.cols) * CELL_WIDTH + 10
                    pos_y = self.y + (CELL_HEIGHT - HOLE_HEIGHT) / 2 + i * CELL_HEIGHT
                    self.response_pins[i][j].rect = pg.Rect(pos_x, pos_y, HOLE_WIDTH, HOLE_HEIGHT)

            self.state.place_color_pin(self.color_pins[i][j].click_count, j)
            self.state.place_response_pin(self.response_pins[i][j].click_count, j)

        self.state.set_active_row(active_row_storage)  # temporary

    def draw(self, screen: pg.Surface, mouse_state: [bool, (int, int)]) -> None:
        self.update_state_after_click(mouse_state)

        pg.draw.rect(screen, self.board_color, self.board)
        pg.draw.rect(screen, self.line_color, self.line)
        pg.draw.rect(screen, self.board_color, self.secret)
        pg.draw.rect(screen, self.backlight_color, self.active_row_backlight)

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.color_pins[i][j].draw(screen)
                self.response_pins[i][j].draw(screen)

        for i in range(0, self.cols):
            self.secret_line[i].draw(screen)
