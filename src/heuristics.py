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


def evaluate_round(player: list[int], secret: list[int]) -> (bool, int, int):
    """Evaluates how many points to give, and whether the player has guessed the secret code
    :param player: player's row of pins
    :param secret: secret row of pins
    :return: tuple of: boolean representing whether the player has guessed the secret code,
    number of black and white pins, in that order
    """
    black_pins, white_pins = evaluate_row(player, secret)   # type: (int, int)
    has_guessed = False                                     # type: bool
    if black_pins == 4:
        has_guessed = True
    return has_guessed, black_pins, white_pins
