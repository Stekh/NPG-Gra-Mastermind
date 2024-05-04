class Game:
    """The core game state class.

            Holds two 2D matrices of pins currently on the board:
                color_pin_matrix -- colored pins used for guessing
                response_pin_matrix -- black and white pins used for verifying guesses
            Initialise with the size of the game and the target combination"""

    def __init__(self, no_rows: int, no_cols: int, combination: list[int]):

        self.__active_row = 0
        self.__no_rows = no_rows
        self.__no_cols = no_cols
        self.__combination = combination
        self.__color_pin_matrix = [[0 for i in range(no_cols)] for j in range(no_rows)]
        self.__response_pin_matrix = [[0 for i in range(no_cols)] for j in range(no_rows)]
        self.end_row_reached = False

    def get_color_pin_color(self, row: int, col: int):
        """Color pin getter."""
        return self.__color_pin_matrix[row][col]

    def get_response_pin_color(self, row: int, col: int):
        """Response pin getter."""
        return self.__response_pin_matrix[row][col]

    def get_active_row(self):
        """Active row getter."""
        return self.__active_row

    def get_no_rows(self):
        """Getter for number of rows."""
        return self.__no_rows

    def get_no_cols(self):
        """Getter for number of cols."""
        return self.__no_cols

    def get_combination(self):
        """Combination getter."""
        return self.__combination

    def place_color_pin(self, color: int, pos: int):
        """Places a color pin in given position of active row."""
        self.__color_pin_matrix[self.__active_row][pos] = color

    def place_response_pin(self, color: int, pos: int):
        """Places a response pin in given position of active row."""
        self.__response_pin_matrix[self.__active_row][pos] = color

    def advance_active_row(self):
        """Moves game to the next row, or records end of game if the last row is reached."""
        if self.__active_row < self.__no_rows - 1:
            self.__active_row += 1
        else:
            self.end_row_reached = True

    def set_active_row(self, pos: int):  # Probably won't need this but will help with tests
        """Sets the active row to a specified location."""
        self.__active_row = pos
