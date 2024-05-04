import pytest
from src import heuristics


def test_evaluate_row():
    assert heuristics.evaluate_row([1, 2, 3, 4], [1, 2, 3, 4]) == (4, 0)
    assert heuristics.evaluate_row([1, 2, 3, 4], [4, 3, 2, 1]) == (0, 4)
    assert heuristics.evaluate_row([1, 2, 3, 4], [4, 2, 3, 1]) == (2, 2)
    assert heuristics.evaluate_row([1, 2, 3, 4], [5, 6, 7, 8]) == (0, 0)
    assert heuristics.evaluate_row([1, 2, 3, 4], [1, 2, 4, 1]) == (2, 1)


def test_evaluate_round():
    assert heuristics.evaluate_round([1, 2, 3, 4], [1, 2, 3, 4]) == (True, 0, 4, 0)
    assert heuristics.evaluate_round([1, 2, 3, 4], [4, 3, 2, 1]) == (False, 1, 0, 4)
    assert heuristics.evaluate_round([1, 2, 3, 4], [4, 2, 3, 1]) == (False, 0, 2, 2)
    assert heuristics.evaluate_round([1, 2, 3, 4], [5, 6, 7, 8]) == (False, 0, 0, 0)
    assert heuristics.evaluate_round([1, 2, 3, 4], [1, 2, 4, 1]) == (False, 0, 2, 2)