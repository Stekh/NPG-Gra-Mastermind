def evaluate_row(player: list[int], secret: list[int]) -> (int, int):
    """Evaluate given row against the given secret row
    :param player: player's row of pins
    :param secret: secret row of pins
    :return: number of black and white pins, in that order
    """
    black_pins = 0                  # type: int
    white_pins = 0                  # type: int
    mut_player = player.copy()      # type: list[int]
    mut_secret = secret.copy()      # type: list[int]
    i = 0                           # type: int

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
    black_pins, white_pins = evaluate_row(player, secret)    # type: int, int
    points = 0  # type: int
    if round_no == round_limit:
        points = 2
    elif black_pins < 4:
        points = 1

    return points, black_pins, white_pins
