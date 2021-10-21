"""List utility functions part 2."""

__author__ = "730408456"


def only_evens(evens: list[int]) -> list[int]:
    """Returns a list with only even elements."""
    x: int = 0
    while x < len(evens):
        if evens[x] % 2 == 0:
            x += 1
        else:
            evens.pop(x)
    return evens


def sub(a_list: list[int], x: int, y: int) -> list[int]:
    """Generate a subset of another list."""
    b_list: list[int] = list()
    if x == len(a_list) or y <= 0:
        return b_list
    if x < 0:
        x = 0
    if y > len(a_list):
        y = len(a_list)
    while x < y:
        b_list.append(a_list[x])
        x += 1
    else:
        return b_list


def concat(c_list: list[int], d_list: list[int]) -> list[int]:
    """When given two lists, concat them."""
    e_list: list[int] = list()
    x = 0
    a = 0
    while x < len(c_list):
        e_list.append(c_list[x])
        x += 1
    while a < len(d_list):
        e_list.append(d_list[a])
        a += 1
    return e_list