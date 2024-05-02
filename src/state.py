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
        self.combination_found = False

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
