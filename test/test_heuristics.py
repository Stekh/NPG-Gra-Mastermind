import pytest
from src import heuristics


def test_evaluate_row():
    assert heuristics.evaluate_row([1, 2, 3, 4], [1, 2, 3, 4]) == (0, 0)
