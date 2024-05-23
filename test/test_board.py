import pytest
import pygame as pg
from src import board
from src import heuristics as hr


class TestBoard:
    def test_pick_color_for_pin(self):
        test_board = board.Board(2, 2, 0, 0)

        test_board.state.place_color_pin(2, 0)
        test_board.state.place_color_pin(1, 1)

        assert test_board.pick_color_for_pin("color_pin", 0, 0) == pg.Color(246, 250, 42)
        assert test_board.pick_color_for_pin("color_pin", 0, 1) == pg.Color(255, 23, 23)
        assert test_board.pick_color_for_pin("color_pin", 1, 0) == pg.Color(0, 0, 0)
        assert test_board.pick_color_for_pin("color_pin", 1, 1) == pg.Color(0, 0, 0)

        for i in range(2):
            for j in range(2):
                test_board.color_pins[i][j].hover = True

        assert test_board.pick_color_for_pin("color_pin", 0, 0) == pg.Color(196, 200, 0)
        assert test_board.pick_color_for_pin("color_pin", 0, 1) == pg.Color(205, 0, 0)
        assert test_board.pick_color_for_pin("color_pin", 1, 0) == pg.Color(0, 0, 0)
        assert test_board.pick_color_for_pin("color_pin", 1, 1) == pg.Color(0, 0, 0)

    def test_screen_state_connection(self):
        test_board = board.Board(8, 4, 10, 10)

        test_board.update_state([True, (104, 553)])
        assert test_board.state.get_combination() == [0, 0, 0, 0]
        test_board.secret_visible = True

        test_board.update_state([True, (42, 42)])
        assert test_board.state.get_active_color_row() == [1, 0, 0, 0]
        test_board.update_state([True, (50, 50)])
        assert test_board.state.get_active_color_row() == [2, 0, 0, 0]

        test_board.update_state([True, (104, 553)])
        assert test_board.state.get_combination() == [0, 1, 0, 0]
        test_board.update_state([True, (116, 542)])
        assert test_board.state.get_combination() == [0, 2, 0, 0]

        test_board.update_state([True, (50, 50)])
        test_board.update_state([True, (50, 50)])
        test_board.update_state([True, (50, 50)])
        test_board.update_state([True, (50, 50)])
        assert test_board.state.get_active_color_row() == [0, 0, 0, 0]
        test_board.update_state([True, (50, 50)])
        assert test_board.state.get_active_color_row() == [0, 0, 0, 0]

    def test_pins_resize(self):
        test_board = board.Board(8, 4, 10, 10)

        assert test_board.color_pins[0][0].rect == pg.Rect(38, 38, 8, 8)
        test_board.update_state([True, (42, 42)])
        assert test_board.color_pins[0][0].rect == pg.Rect(26, 26, 32, 32)
        test_board.update_state([True, (42, 42)])
        test_board.update_state([True, (42, 42)])
        test_board.update_state([True, (42, 42)])
        test_board.update_state([True, (42, 42)])
        test_board.update_state([True, (42, 42)])
        assert test_board.color_pins[0][0].rect == pg.Rect(38, 38, 8, 8)

    def test_response_pins_behaviour(self):
        test_board = board.Board(8, 4, 10, 10)

        test_board.update_state([True, (42, 42)])
        test_board.update_state([True, (104, 553)])
        assert test_board.response_pins[0][0].rect == pg.Rect(304, 38, 8, 8)
        assert test_board.response_pins[0][1].rect == pg.Rect(368, 38, 8, 8)
        assert test_board.response_pins[0][2].rect == pg.Rect(432, 38, 8, 8)
        assert test_board.response_pins[0][3].rect == pg.Rect(496, 38, 8, 8)

        hr.advance_row(test_board)
        test_board.state.set_active_row(0)
        assert test_board.state.get_active_response_row() == [2, 2, 1, 1]
        assert test_board.response_pins[0][0].rect == pg.Rect(300, 34, 16, 16)
        assert test_board.response_pins[0][1].rect == pg.Rect(364, 34, 16, 16)
        assert test_board.response_pins[0][2].rect == pg.Rect(428, 34, 16, 16)
        assert test_board.response_pins[0][3].rect == pg.Rect(492, 34, 16, 16)
