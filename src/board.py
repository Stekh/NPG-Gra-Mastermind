import pygame as pg
from src import ui
from src import state

CELL_SIZE = 64
COLOR_PIN_SIZE = 32
RESPONSE_PIN_SIZE = 16
HOLE_SIZE = 8
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
        # Size of the game
        self.rows: int = rows
        self.cols: int = cols

        # Position of the board
        self.x: float = x
        self.y: float = y

        # Pin's parameters
        self.color_pin_size: float = COLOR_PIN_SIZE
        self.response_pin_size: float = RESPONSE_PIN_SIZE
        self.color_pin_colors: list[(int, int, int)] = COLOR_PINS_COLORS
        self.response_pin_colors: list[(int, int, int)] = RESPONSE_PINS_COLORS
        self.hover_colors_vector: (int, int, int) = HOVER_COLORS_VECTOR

        # Parts of board
        self.board: pg.Rect = pg.Rect(x, y, CELL_SIZE * cols * 2 + 10, CELL_SIZE * rows)
        self.line: pg.Rect = pg.Rect(x + cols * CELL_SIZE + 3, y + 2, 4, CELL_SIZE * rows - 4)
        self.secret: pg.Rect = pg.Rect(x, y + rows * CELL_SIZE, CELL_SIZE * cols, CELL_SIZE)
        self.active_row_backlight: pg.Rect = pg.Rect(x + 2, y + 2, CELL_SIZE * cols - 4, CELL_SIZE - 4)

        # Parts of board parameters
        self.board_color: pg.Color = pg.Color(BOARD_COLOR)
        self.line_color: pg.Color = pg.Color(LINE_COLOR)
        self.backlight_color: pg.Color = pg.Color(BACKLIGHT_COLOR)

        # State of the game
        self.state: state.Game = state.Game(rows, cols, [0 for _i in range(0, cols)])
        self.secret_visible: bool = True

        # All pins on the board
        init_pos_x: float = x + (CELL_SIZE - HOLE_SIZE) / 2
        init_pos_y: float = y + (CELL_SIZE - HOLE_SIZE) / 2
        self.color_pins: list[list[ui.Pin]] = [
            [ui.Pin(init_pos_x + i * CELL_SIZE, init_pos_y + j * CELL_SIZE, HOLE_SIZE, HOLE_SIZE) for i in
             range(0, cols)] for j in range(0, rows)]
        self.response_pins: list[list[ui.Pin]] = [
            [ui.Pin(init_pos_x + (i + cols) * CELL_SIZE + 10, init_pos_y + j * CELL_SIZE, HOLE_SIZE, HOLE_SIZE)
             for i in range(0, cols)] for j in range(0, rows)]
        self.secret_line: list[ui.Pin] = [
            ui.Pin(init_pos_x + i * CELL_SIZE, init_pos_y + rows * CELL_SIZE, HOLE_SIZE, HOLE_SIZE) for i in
            range(0, cols)]

    def update_state(self, mouse_state: [bool, (int, int)]) -> None:
        """Game state updater.
        :param mouse_state: including mouse button state and cursor position
        :return: None
        """

        modified_row: int = self.state.get_active_row_no()
        for i in range(0, self.cols):
            # Check if the cursor is over the button
            pos: (int, int) = mouse_state[1]
            is_mouse_over: bool = self.color_pins[modified_row][i].is_mouse_over(pos)
            self.color_pins[modified_row][i].set_hover(is_mouse_over)

            if is_mouse_over:
                # Check if the mouse button is down
                clicked: bool = mouse_state[0]
                if clicked:
                    # Change color of the button and the game state
                    self.state.place_color_pin((self.state.get_color_pin_color(modified_row, i) + 1) % 6, i)

                # Change the size and position of the button from hole size to pin size
                if self.state.get_color_pin_color(modified_row, i) == 1:
                    pos_x: float = self.x + CELL_SIZE / 2 + i * CELL_SIZE - self.color_pin_size / 2
                    pos_y: float = self.y + CELL_SIZE / 2 + modified_row * CELL_SIZE - self.color_pin_size / 2
                    self.color_pins[modified_row][i].rect = pg.Rect(pos_x, pos_y, self.color_pin_size,
                                                                    self.color_pin_size)

                # Change the size and position of the button from pin size to hole size
                if self.state.get_color_pin_color(modified_row, i) == 0:
                    pos_x: float = self.x + (CELL_SIZE - HOLE_SIZE) / 2 + i * CELL_SIZE
                    pos_y: float = self.y + (CELL_SIZE - HOLE_SIZE) / 2 + modified_row * CELL_SIZE
                    self.color_pins[modified_row][i].rect = pg.Rect(pos_x, pos_y, HOLE_SIZE, HOLE_SIZE)

        """Variable used to create the new combination of secret line - after clicking or hovering a button.
        Everything just like in the loop above, but for secret line"""
        if self.secret_visible:
            current_combination: list[int] = self.state.get_combination()
            new_combination: list[int] = []
            for i in range(0, self.cols):
                pos: (int, int) = mouse_state[1]
                is_mouse_over: bool = self.secret_line[i].is_mouse_over(pos)
                self.secret_line[i].set_hover(is_mouse_over)

                if is_mouse_over:
                    clicked: bool = mouse_state[0]
                    if clicked:
                        new_combination.append((current_combination[i] + 1) % 6)
                    else:
                        new_combination.append(current_combination[i])

                    if new_combination[i] == 1:
                        pos_x: float = self.x + CELL_SIZE / 2 + i * CELL_SIZE - self.color_pin_size / 2
                        pos_y: float = self.y + CELL_SIZE / 2 + self.rows * CELL_SIZE - self.color_pin_size / 2
                        self.secret_line[i].rect = pg.Rect(pos_x, pos_y, self.color_pin_size, self.color_pin_size)

                    if new_combination[i] == 0:
                        pos_x: float = self.x + (CELL_SIZE - HOLE_SIZE) / 2 + i * CELL_SIZE
                        pos_y: float = self.y + (CELL_SIZE - HOLE_SIZE) / 2 + self.rows * CELL_SIZE
                        self.secret_line[i].rect = pg.Rect(pos_x, pos_y, HOLE_SIZE, HOLE_SIZE)
                else:
                    new_combination.append(current_combination[i])

            # Combination update
            self.state.set_combination(new_combination)

    def update_state_before_row_advance(self) -> None:
        """Game state updater to use before row advancement.
        :return: None
        """

        # Backlight position change
        if self.state.get_active_row_no() < self.rows - 1:
            self.active_row_backlight = pg.Rect(self.x + 2,
                                                self.y + CELL_SIZE * (self.state.get_active_row_no() + 1) + 2,
                                                CELL_SIZE * self.cols - 4, CELL_SIZE - 4)

        modified_row: int = self.state.get_active_row_no()
        for i in range(0, self.cols):

            # Updating response pins size from hole size to pin size
            if self.state.get_response_pin_color(modified_row, i) > 0:
                pos_x: float = self.x + CELL_SIZE / 2 + (i + self.cols) * CELL_SIZE + 10 - self.response_pin_size / 2
                pos_y: float = self.y + CELL_SIZE / 2 + modified_row * CELL_SIZE - self.response_pin_size / 2
                self.response_pins[modified_row][i].rect = pg.Rect(pos_x, pos_y, self.response_pin_size,
                                                                   self.response_pin_size)
            else:
                # Updating response pins size from pin size to hole size
                pos_x: float = self.x + (CELL_SIZE - HOLE_SIZE) / 2 + (i + self.cols) * CELL_SIZE + 10
                pos_y: float = self.y + (CELL_SIZE - HOLE_SIZE) / 2 + modified_row * CELL_SIZE
                self.response_pins[modified_row][i].rect = pg.Rect(pos_x, pos_y, HOLE_SIZE, HOLE_SIZE)

    def pick_color_for_pin(self, board_part: str, i: int, j: int = -1) -> pg.Color:
        """Function picking color for the Pin before drawing, depending on the game state
        and Pin's hover value.
        :param board_part: describe the part of the board, when the analyzing Pin is located
        :param i: Pin's row number
        :param j: Pin's column number
        :return: color of the Pin for the drawing
        """

        color: list[int] = [0, 0, 0]
        add_vector: bool = False

        if board_part == "color_pin":
            color = [self.color_pin_colors[self.state.get_color_pin_color(i, j)][k] for k in range(3)]
            if self.color_pins[i][j].hover:
                add_vector = True
        if board_part == "response_pin":
            color = [self.response_pin_colors[self.state.get_response_pin_color(i, j)][k] for k in range(3)]
            if self.response_pins[i][j].hover:
                add_vector = True
        if board_part == "secret_pin":
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

        return pg.Color(color)

    def draw(self, screen: pg.Surface, mouse_state: [bool, (int, int)]) -> None:
        """Draws board on the screen.
        :param screen: where board will be drawn
        :param mouse_state: including mouse button state and cursor position
        :return: None
        """

        # Updating game state
        self.update_state(mouse_state)

        # Draw board core
        pg.draw.rect(screen, self.board_color, self.board)
        pg.draw.rect(screen, self.line_color, self.line)
        if self.secret_visible:
            pg.draw.rect(screen, self.board_color, self.secret)
        pg.draw.rect(screen, self.backlight_color, self.active_row_backlight)

        # Draw color and response pins
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.color_pins[i][j].draw(screen, self.pick_color_for_pin("color_pin", i, j))
                self.response_pins[i][j].draw(screen, self.pick_color_for_pin("response_pin", i, j))

        # Draw secret line
        if self.secret_visible:
            for i in range(0, self.cols):
                self.secret_line[i].draw(screen, self.pick_color_for_pin("secret_pin", i))

    def set_random_secret(self) -> None:
        """sets the secret to a random combination, and makes the draw function display said combination as pins,
        rather than colorful holes"""
        self.state.set_random_combination()
        init_pos_x: float = self.secret.centerx - self.color_pin_size * 3.5
        init_pos_y: float = self.secret.centery - self.color_pin_size / 2
        self.secret_line: list[ui.Pin] = [
            ui.Pin(init_pos_x + i * CELL_SIZE, init_pos_y, self.color_pin_size, self.color_pin_size) for i in
            range(0, self.cols)]
