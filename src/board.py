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
HOVER_COLORS_VECTOR = (-50, -50, -50)
LINE_COLOR = (158, 121, 0)
BACKLIGHT_COLOR = (250, 211, 142)
COLOR_PINS_COLORS = [(0, 0, 0), (255, 23, 23), (246, 250, 42), (22, 245, 33), (10, 216, 252),
                     (255, 0, 255)]
RESPONSE_PINS_COLORS = [(0, 0, 0), (255, 255, 255), (0, 0, 0)]


class Board:
    """The class representing board for Mastermind game

    Holds:
        state -- Game class object, actual state of game
        color_pins -- matrix of Button class objects - color pins matrix visualization
        response_pins -- matrix of Button class objects - response pins matrix visualization
        secret_line -- list of Button class objects - combination visualization
        board,
        line,
        secret,
        active_row_backlight -- elements displaying on screen to draw a Mastermind board
        rows, cols, x, y -- size and position parameters for board
        color_pin_width, board_color, etc. -- bunch of additional parameters to customize the board
    Initialise with size of game and the position on the screen
    """

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
        self.hover_colors_vector = HOVER_COLORS_VECTOR
        self.board = pg.Rect(x, y, CELL_WIDTH * cols * 2 + 10, CELL_HEIGHT * rows)
        self.line = pg.Rect(x + cols * CELL_WIDTH + 3, y + 2, 4, CELL_HEIGHT * rows - 4)
        self.secret = pg.Rect(x, y + rows * CELL_HEIGHT, CELL_WIDTH * cols, CELL_HEIGHT)
        self.active_row_backlight = pg.Rect(x + 2, y + 2, CELL_WIDTH * cols - 4, CELL_HEIGHT - 4)
        self.state = state.Game(rows, cols, [0 for i in range(0, cols)])
        init_pos_x = x + (CELL_WIDTH - HOLE_WIDTH) / 2
        init_pos_y = y + (CELL_HEIGHT - HOLE_HEIGHT) / 2
        self.color_pins = [
            [ui.Pin(init_pos_x + i * CELL_WIDTH, init_pos_y + j * CELL_HEIGHT, HOLE_WIDTH, HOLE_HEIGHT) for i in
             range(0, cols)] for j in range(0, rows)]
        self.response_pins = [
            [ui.Pin(init_pos_x + (i + cols) * CELL_WIDTH + 10, init_pos_y + j * CELL_HEIGHT, HOLE_WIDTH, HOLE_HEIGHT)
             for i in range(0, cols)] for j in range(0, rows)]
        self.secret_line = [
            ui.Pin(init_pos_x + i * CELL_WIDTH, init_pos_y + rows * CELL_HEIGHT, HOLE_WIDTH, HOLE_HEIGHT) for i in
            range(0, cols)]

    def update_state(self, mouse_state: [bool, (int, int)]) -> None:
        """Game state updater.
        :param mouse_state: including mouse button state and cursor position
        :return: None
        """

        modified_row = self.state.get_active_row_no()
        for i in range(0, self.cols):
            """Check if the cursor is over the button"""
            pos = mouse_state[1]
            is_mouse_over = self.color_pins[modified_row][i].is_mouse_over(pos)
            self.color_pins[modified_row][i].set_hover(is_mouse_over)

            if is_mouse_over:
                """Check if the mouse button is down"""
                clicked = mouse_state[0]
                if clicked:
                    """Change color of the button"""
                    self.state.place_color_pin((self.state.get_color_pin_color(modified_row, i) + 1) % 6, i)

                """Change the size and position of the button from hole size to pin size"""
                if self.state.get_color_pin_color(modified_row, i) == 1:
                    pos_x = self.x + CELL_WIDTH / 2 + i * CELL_WIDTH - self.color_pin_width / 2
                    pos_y = self.y + CELL_HEIGHT / 2 + modified_row * CELL_HEIGHT - self.color_pin_height / 2
                    self.color_pins[modified_row][i].rect = pg.Rect(pos_x, pos_y, self.color_pin_width,
                                                                    self.color_pin_height)

                """Change the size and position of the button from pin size to hole size"""
                if self.state.get_color_pin_color(modified_row, i) == 0:
                    pos_x = self.x + (CELL_WIDTH - HOLE_WIDTH) / 2 + i * CELL_WIDTH
                    pos_y = self.y + (CELL_HEIGHT - HOLE_HEIGHT) / 2 + modified_row * CELL_HEIGHT
                    self.color_pins[modified_row][i].rect = pg.Rect(pos_x, pos_y, HOLE_WIDTH, HOLE_HEIGHT)

        """Variable used to create the new combination of secret line - after clicking or hovering a button"""
        """Everything just like in the loop above, but for secret line"""
        current_combination = self.state.get_combination()
        new_combination = []
        for i in range(0, self.cols):
            pos = mouse_state[1]
            is_mouse_over = self.secret_line[i].is_mouse_over(pos)
            self.secret_line[i].set_hover(is_mouse_over)

            if is_mouse_over:
                clicked = mouse_state[0]
                if clicked:
                    new_combination.append((current_combination[i] + 1) % 6)
                else:
                    new_combination.append(current_combination[i])

                if new_combination[i] == 1:
                    pos_x = self.x + CELL_WIDTH / 2 + i * CELL_WIDTH - self.color_pin_width / 2
                    pos_y = self.y + CELL_HEIGHT / 2 + self.rows * CELL_HEIGHT - self.color_pin_height / 2
                    self.secret_line[i].rect = pg.Rect(pos_x, pos_y, self.color_pin_width, self.color_pin_height)

                if new_combination[i] == 0:
                    pos_x = self.x + (CELL_WIDTH - HOLE_WIDTH) / 2 + i * CELL_WIDTH
                    pos_y = self.y + (CELL_HEIGHT - HOLE_HEIGHT) / 2 + self.rows * CELL_HEIGHT
                    self.secret_line[i].rect = pg.Rect(pos_x, pos_y, HOLE_WIDTH, HOLE_HEIGHT)
            else:
                new_combination.append(current_combination[i])

        """Combination update"""
        self.state.set_combination(new_combination)

    def update_state_before_evaluation(self) -> None:
        """Game state updater after row's evaluation.
        :return: None
        """

        """Backlight position change"""
        self.active_row_backlight = pg.Rect(self.x + 2, self.y + CELL_HEIGHT * (self.state.get_active_row_no() + 1) + 2,
                                            CELL_WIDTH * self.cols - 4, CELL_HEIGHT - 4)

        modified_row = self.state.get_active_row_no()
        for i in range(0, self.cols):

            """Updating response pins color size from hole size to pin size"""
            if self.state.get_response_pin_color(modified_row, i) > 0:
                pos_x = self.x + CELL_WIDTH / 2 + (
                        i + self.cols) * CELL_WIDTH + 10 - self.response_pin_width / 2
                pos_y = self.y + CELL_HEIGHT / 2 + modified_row * CELL_HEIGHT - self.response_pin_height / 2
                self.response_pins[modified_row][i].rect = pg.Rect(pos_x, pos_y, self.response_pin_width,
                                                                   self.response_pin_height)
            else:
                """Updating response pins color size from pin size to hole size"""
                pos_x = self.x + (CELL_WIDTH - HOLE_WIDTH) / 2 + (i + self.cols) * CELL_WIDTH + 10
                pos_y = self.y + (CELL_HEIGHT - HOLE_HEIGHT) / 2 + modified_row * CELL_HEIGHT
                self.response_pins[modified_row][i].rect = pg.Rect(pos_x, pos_y, HOLE_WIDTH, HOLE_HEIGHT)

    def pick_color_for_pin(self, id: int, i: int, j: int = -1) -> (int, int, int):

        color: list[int] = [0, 0, 0]
        add_vector: bool = False

        if id == 0:
            color = [self.color_pin_colors[self.state.get_color_pin_color(i, j)][k] for k in range(3)]
            if self.color_pins[i][j].hover:
                add_vector = True
        if id == 1:
            color = [self.response_pin_colors[self.state.get_response_pin_color(i, j)][k] for k in range(3)]
            if self.response_pins[i][j].hover:
                add_vector = True
        if id == 2:
            color = [self.color_pin_colors[self.state.get_combination()[i]][k] for k in range(3)]
            if self.secret_line[i].hover:
                add_vector = True
        if add_vector:
            for i in range(3):
                color[i] += self.hover_colors_vector[i]
                if color[i] > 255:
                    color[i] = 255
                if color[i] < 0:
                    color[i] = 0

        return color

    def draw(self, screen: pg.Surface, mouse_state: [bool, (int, int)]) -> None:
        """Draws board on the screen.
        :param screen: where board will be drawn
        :param mouse_state: including mouse button state and cursor position
        :return: None
        """

        """Updating game state"""
        self.update_state(mouse_state)

        """Draw board core"""
        pg.draw.rect(screen, self.board_color, self.board)
        pg.draw.rect(screen, self.line_color, self.line)
        pg.draw.rect(screen, self.board_color, self.secret)
        pg.draw.rect(screen, self.backlight_color, self.active_row_backlight)

        """Draw color and response pins"""
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.color_pins[i][j].draw(screen, self.pick_color_for_pin(0, i, j))
                self.response_pins[i][j].draw(screen, self.pick_color_for_pin(1, i, j))

        """Draw secret line"""
        for i in range(0, self.cols):
            self.secret_line[i].draw(screen, self.pick_color_for_pin(2, i))
