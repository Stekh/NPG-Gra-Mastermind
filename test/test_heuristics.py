import pytest
from src import heuristics


class TestHeuristics:
    def test_evaluate_row(self):
        assert heuristics.evaluate_row([1, 2, 3, 4], [1, 2, 3, 4]) == (4, 0)
        assert heuristics.evaluate_row([1, 2, 3, 4], [4, 3, 2, 1]) == (0, 4)
        assert heuristics.evaluate_row([1, 2, 3, 4], [4, 2, 3, 1]) == (2, 2)
        assert heuristics.evaluate_row([1, 2, 3, 4], [5, 6, 7, 8]) == (0, 0)
        assert heuristics.evaluate_row([1, 2, 3, 4], [1, 2, 4, 1]) == (2, 1)

    def test_assign_points(self):
        assert heuristics.assign_points([1, 2, 3, 4], [1, 2, 3, 4], 3, 10) == (0, 4, 0)
        assert heuristics.assign_points([1, 2, 3, 4], [4, 3, 2, 1], 10, 10) == (2, 0, 4)
        assert heuristics.assign_points([1, 2, 3, 4], [4, 2, 3, 1], 7, 10) == (1, 2, 2)
