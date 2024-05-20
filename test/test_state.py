import pytest
from src import state
from src.board import COLOR_PINS_COLORS


def test_getters():
    game = state.Game(10, 4, [2, 1, 3, 7])
    game.place_color_pin(3, 2)
    game.place_response_pin(2, 3)
    assert game.get_combination() == [2, 1, 3, 7]
    assert game.get_no_cols() == 4
    assert game.get_no_rows_turn_limit() == 10
    assert game.get_active_row_no() == 0
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
    assert game.get_active_row_no() == 9
    assert game.end_row_reached


def test_set_random_combination():
    game = state.Game(10, 4)
    game.set_random_combination()
    for pin in game.get_combination():
        assert 1 <= pin < len(COLOR_PINS_COLORS)
