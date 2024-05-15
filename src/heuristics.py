from src import board
from src import state


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
    if round_no == round_limit:
        points = 2
    elif black_pins < 4:
        points = 1

    return points, black_pins, white_pins


def advance_row(board: board.Board) -> None:
    """Evaluates current round, places response pins and moves to the next row
    :param board: board is made of board"""
    score: (int, int) = evaluate_row(board.state.get_active_row(), board.state.get_combination())
    for i in range(score[0]):
        board.state.place_response_pin(2, i)
    for i in range(score[0], score[1]):
        board.state.place_pin(1, score[0]+i)
    board.state.advance_active_row()
    board.update_state_after_evaluation()
