"""List utility functions."""

__author__ = "730408456"


def all(test: list[int], x: int) -> bool:
    i = 0
    while len(test) > i:
        if test[i] == x:
            i += 1
        else:
            return False
    else:
        return True


def is_equal(list1: list[int], list2: list[int]) -> bool:
    i = 0
    if len(list1) != len(list2):
        return False
    else:
        while i < len(list1) and len(list2):
            if list1[i] == list2[i]:
                i += 1
            else:
                return False
        else:
            return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        most = input[0]
        for x in input:
            if x > most:
                most = x
        return most