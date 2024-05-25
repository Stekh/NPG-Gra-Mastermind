from src import board


def evaluate_row(player: list[int], secret: list[int]) -> (int, int):
    """Evaluate given row against the given secret row
    :param player: player's row of pins
    :param secret: secret row of pins
    :return: number of black and white pins, in that order
    """
    black_pins: int = 0
    white_pins: int = 0
    mut_player: list[int] = player.copy()
    mut_secret: list[int] = secret.copy()
    i: int = 0

    # evaluate number of black pins
    while i < len(mut_player):
        if mut_player[i] == mut_secret[i]:
            black_pins += 1
            mut_player.pop(i)
            mut_secret.pop(i)
        else:
            i += 1

    i = 0
    # evaluate number of white pins
    while i < len(mut_player):
        if mut_player[i] in mut_secret:
            white_pins += 1
            mut_secret.pop(mut_secret.index(mut_player[i]))
            mut_player.pop(i)
        else:
            i += 1

    return black_pins, white_pins


def assign_points(player: list[int], secret: list[int], round_no: int, round_limit: int) -> (int, int, int):
    """Evaluate the round and assign the points accordingly
    :param player: player's row of pins
    :param secret: secret row of pins
    :param round_no: current round number
    :param round_limit: maximum amount of rounds
    :return: tuple of: number of points to assign, number of black and white pins, in that order
    """
    black_pins: int
    white_pins: int
    black_pins, white_pins = evaluate_row(player, secret)
    points: int = 0
    if round_no == round_limit - 1:
        points = 2
    elif black_pins < len(player):
        points = 1
    return points, black_pins, white_pins


def advance_row(board1: board.Board) -> int:
    """Evaluates current round, places response pins and moves to the next row
    :param board1: object that describes the current state of the board"""
    score: (int, int, int) = assign_points(board1.state.get_active_color_row(), board1.state.get_combination(),
                                           board1.state.get_active_row_no(), board1.state.get_no_rows_turn_limit())

    for i in range(score[1]):
        board1.state.place_response_pin(2, i)
    for i in range(score[2]):
        board1.state.place_response_pin(1, score[1] + i)
    for i in range(score[2] + score[1], board1.cols):
        board1.state.place_response_pin(0, i)
    board1.update_state_before_row_advance()
    board1.state.advance_active_row()
    return score[0]
