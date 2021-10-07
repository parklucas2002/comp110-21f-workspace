"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730408456"


def test_only_evens() -> None:
    '''Test only_evens 1.'''
    evens: list[int] = [1, 2, 3]
    assert only_evens(evens) == [2]


def test_only_evens_two() -> None:
    '''Test only_evens 2.'''
    evens: list[int] = [2, 5, 6, 10, 13, 14]
    assert only_evens(evens) == [2, 6, 10, 14]


def test_only_evens_three() -> None:
    """Test only_evens with an empty list."""
    evens: list[int] = [1, 3, 5, 7]
    assert only_evens(evens) == []


def test_sub() -> None:
    """Test sub 1."""
    a_list: list[int] = [10, 15, 20, 25, 30]
    x: int = 1
    y: int = 4
    assert sub(a_list, x, y) == [15, 20, 25]


def test_sub_two() -> None:
    """Test sub 2."""
    a_list: list[int] = [0, 1, 3]
    x: int = 1
    y: int = 3
    assert sub(a_list, x, y) == [1, 3]


def test_sub_three() -> None:
    """Test sub with only two elements."""
    a_list: list[int] = [1, 2]
    x: int = 1
    y: int = 2
    assert sub(a_list, x, y) == [2]


def test_concat() -> None:
    """Test concat 1."""
    c_list: list[int] = [1, 2, 3]
    d_list: list[int] = [4, 5, 6]
    assert concat(c_list, d_list) == [1, 2, 3, 4, 5, 6]


def test_concat_two() -> None:
    """Test concat 2."""
    c_list: list[int] = [2, 4]
    d_list: list[int] = [10, 13, 15]
    assert concat(c_list, d_list) == [2, 4, 10, 13, 15]


def test_concat_three() -> None:
    """Test concat with an empty list."""
    c_list: list[int] = []
    d_list: list[int] = [110, 111]
    assert concat(c_list, d_list) == [110, 111]