import pytest
from src import heuristics


def test_evaluate_row():
    assert heuristics.evaluate_row([1, 2, 3, 4], [1, 2, 3, 4]) == (4, 0)
    assert heuristics.evaluate_row([1, 2, 3, 4], [4, 3, 2, 1]) == (0, 4)
    assert heuristics.evaluate_row([1, 2, 3, 4], [4, 2, 3, 1]) == (2, 2)
    assert heuristics.evaluate_row([1, 2, 3, 4], [5, 6, 7, 8]) == (0, 0)
    assert heuristics.evaluate_row([1, 2, 3, 4], [1, 2, 4, 1]) == (2, 1)
