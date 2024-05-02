def evaluate_row(player: list[int], secret: list[int]) -> (int, int):
    black_pins = 0
    white_pins = 0
    mut_player = player.copy()
    mut_secret = secret.copy()
    i = 0
    while i < len(mut_player):
        if mut_player[i] == mut_secret[i]:
            black_pins += 1
            mut_player.pop(i)
            mut_secret.pop(i)
        else:
            i += 1

    i = 0
    while i < len(mut_player):
        if mut_player[i] in mut_secret:
            white_pins += 1
            mut_secret.pop(mut_secret.index(mut_player[i]))
            mut_player.pop(i)

    return black_pins, white_pins
