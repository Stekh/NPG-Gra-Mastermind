import pytest
from src import state


def test_getters():
    game = state.Game(10, 4, [2, 1, 3, 7])
    game.place_color_pin(3, 2)
    game.place_response_pin(2, 3)
    assert game.get_combination() == [2, 1, 3, 7]
    assert game.get_no_cols() == 4
    assert game.get_no_rows() == 10
    assert game.get_active_row() == 0
    assert game.get_color_pin_color(0, 2) == 3
    assert game.get_response_pin_color(0, 3) == 2
