"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730408456"


def test_invert_one() -> None:
    """Test invert 1."""
    x = {'b': 'c', 'a': 'd', 'c': 'a'}
    assert invert(x) == {'c': 'c', 'd': 'd', 'a': 'a'}


def test_invert_two() -> None:
    """Test invert 2."""
    x = {'apple': '1', 'banana': '2'}
    assert invert(x) == {'1': '1', '2': '2'}


def test_invert_three() -> None:
    """Test invert 3."""
    x = {'1': '1', '2': '2'}
    assert invert(x) == {'1': '1', '2': '2'}


def test_favorite_color_one() -> None:
    """Test favorite_color 1."""
    c = {'Lucas': 'blue', 'Owen': 'blue', 'George': 'red'}
    assert favorite_color(c) == "blue"


def test_favorite_color_two() -> None:
    """Test favorite_color 2."""
    c = {'Lucas': 'orange', 'Owen': 'blue', 'George': 'red'}
    assert favorite_color(c) == "orange"


def test_favorite_color_three() -> None:
    """Test favorite_color 3."""
    c = {'Lucas': 'blue', 'Owen': 'red', 'George': 'red'}
    assert favorite_color(c) == "red"


def test_count_one() -> None:
    """Test count 1."""
    a = ['1', '2', '1', '2', '1', '1', '3']
    assert count(a) == {'1': 4, '2': 2, '3': 1}


def test_count_two() -> None:
    """Test count 1."""
    a = ['1', '1', '1', '1', '1', '1', '1']
    assert count(a) == {'1': 7}


def test_count_three() -> None:
    """Test count 3."""
    a = ['apple', 'orange', 'orange', 'apple', 'apple', 'banana', 'orange']
    assert count(a) == {'apple': 3, 'orange': 3, 'banana': 1}