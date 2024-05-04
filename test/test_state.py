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


def test_active_row_movement():
    game = state.Game(10, 4, [2, 2, 3, 4])
    game.place_color_pin(2, 3)
    game.place_response_pin(1, 2)
    game.advance_active_row()
    game.place_color_pin(1, 3)
    game.place_response_pin(2, 2)
    assert game.get_color_pin_color(0, 3) == 2
    assert game.get_response_pin_color(0, 2) == 1
    assert game.get_color_pin_color(1, 3) == 1
    assert game.get_response_pin_color(1, 2) == 2


def test_end_of_space():
    game = state.Game(10, 4, [5, 6, 7, 3])
    game.set_active_row(9)
    game.advance_active_row()
    assert game.get_active_row() == 9
    assert game.end_row_reached
