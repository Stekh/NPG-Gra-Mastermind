class Game:
    def __init__(self, no_rows: int, no_cols: int, combination: list[int]):
        """The core game state class.

        Holds two 2D matrices of pins currently on the board:
            color_pin_matrix -- colored pins used for guessing
            response_pin_matrix -- black and white pins used for verifying guesses
        Initialise with the size of the game and the target combination"""

        self.__active_row = 0
        self.__no_rows = no_rows
        self.__no_cols = no_cols
        self.__combination = combination
        self.__color_pin_matrix = [[0 for i in range(no_cols)] for j in range(no_rows)]
        self.__response_pin_matrix = [[0 for i in range(no_cols)] for j in range(no_rows)]
        self.combination_found = False
