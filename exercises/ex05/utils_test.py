"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730408456"


def test_only_evens() -> None:
    evens: list[int] = [1, 2, 3]
    assert only_evens(evens) == [2]


def test_only_evens_two() -> None:
    evens: list[int] = [2, 5, 6, 10, 13, 14]
    assert only_evens(evens) == [2, 6, 10, 14]


def test_only_evens_three() -> None:
    evens: list[int] = [1, 3, 5, 7]
    assert only_evens(evens) == []


def test_sub() -> None:
    a_list: list[int] = [10, 15, 20, 25, 30]
    x: int = 1
    y: int = 4
    assert sub(a_list, x, y) == [15, 20, 25]


def test_sub_two() -> None:
    a_list: list[int] = [0, 1, 3]
    x: int = 1
    y: int = 3
    assert sub(a_list, x, y) == [1, 3]


def test_sub_three() -> None:
    a_list: list[int] = [1, 2]
    x: int = 1
    y: int = 2
    assert sub(a_list, x, y) == [2]


def test_concat() -> None:
    c_list: list[int] = [1, 2, 3]
    d_list: list[int] = [4, 5, 6]
    assert concat(c_list, d_list) == [1, 2, 3, 4, 5, 6]


def test_concat_two() -> None:
    c_list: list[int] = [2, 4]
    d_list: list[int] = [10, 13, 15]
    assert concat(c_list, d_list) == [2, 4, 10, 13, 15]


def test_concat_three() -> None:
    c_list: list[int] = []
    d_list: list[int] = [110, 111]
    assert concat(c_list, d_list) == [110, 111]