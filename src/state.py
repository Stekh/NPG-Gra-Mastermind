import random
from board import COLOR_PINS_COLORS


class Game:
    """The core game state class.

    Holds two 2D matrices of pins currently on the board:
        color_pin_matrix -- colored pins used for guessing
        response_pin_matrix -- black and white pins used for verifying guesses
    Also holds the current combination and the current active row.
    Initialise with the size of the game and the target combination.
    """

    def __init__(self, no_rows: int, no_cols: int, combination: list[int] = None):

        if combination is None:
            combination = [0 for _ in range(no_cols)]
        self.__active_row: int = 0
        self.__no_rows: int = no_rows  # Doubles as turn limit
        self.__no_cols: int = no_cols
        self.__combination: list[int] = combination
        self.__color_pin_matrix: list[list[int]] = [[0 for i in range(no_cols)] for j in range(no_rows)]
        self.__response_pin_matrix: list[list[int]] = [[0 for i in range(no_cols)] for j in range(no_rows)]
        self.end_row_reached: bool = False

    def get_color_pin_color(self, row: int, col: int) -> int:
        """Color pin getter.
        :param row: the pin's row
        :param col: the pin's column
        :return: the pin's color
        """
        return self.__color_pin_matrix[row][col]

    def get_active_color_row(self) -> list[int]:
        """Active row getter.
        :return: the active row's color pins"""
        return self.__color_pin_matrix[self.__active_row]

    def get_active_response_row(self) -> list[int]:
        """Active row getter.
        :return: the active row's black and white pins"""
        return self.__response_pin_matrix[self.__active_row]

    def get_response_pin_color(self, row: int, col: int) -> int:
        """Response pin getter.
        :param row: the pin's row
        :param col: the pin's column
        :return: the pin's color
        """
        return self.__response_pin_matrix[row][col]

    def get_active_row_no(self) -> int:
        """Active row position getter.
        :return: the active row's position
        """
        return self.__active_row

    def get_no_rows_turn_limit(self) -> int:
        """Getter for number of rows, which is also the turn limit.
        :return: number of rows, which doubles as the turn limit
        """
        return self.__no_rows

    def get_no_cols(self) -> int:
        """Getter for number of columns.
        :return: number of columns
        """
        return self.__no_cols

    def get_combination(self) -> list[int]:
        """Combination getter.
        :return: combination (as a list[int])
        """
        return self.__combination

    def set_combination(self, new_combination: list[int]) -> None:
        """temporary, for test
        """
        self.__combination = new_combination

    def set_random_combination(self) -> None:
        """Generates a random combination."""
        self.__combination = [random.randint(1, len(COLOR_PINS_COLORS) + 1) for _ in range(self.__no_cols)]

    def place_color_pin(self, color: int, pos: int) -> None:
        """Places a color pin in given position of active row.
        :param color: color of the pin
        :param pos: position in the active row
        """
        self.__color_pin_matrix[self.__active_row][pos] = color

    def place_response_pin(self, color: int, pos: int) -> None:
        """Places a response pin in given position of active row.
        :param color: color of the pin
        :param pos: position in the active row
        """
        self.__response_pin_matrix[self.__active_row][pos] = color

    def advance_active_row(self) -> None:
        """Moves game to the next row, or records end of game if the last row is reached."""
        if self.__active_row < self.__no_rows - 1:
            self.__active_row += 1
        else:
            self.end_row_reached = True

    def set_active_row(self, pos: int) -> None:  # Probably won't need this but will help with tests
        """Sets the active row to a specified location.
        :param pos: the active row's destination
        """
        self.__active_row = pos
