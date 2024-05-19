import pytest
import pygame as pg
from src import board


class TestHeuristics:
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

    # def test_screen_state_connection(self):
    # assert
