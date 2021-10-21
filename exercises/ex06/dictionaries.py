"""Practice with dictionaries."""

__author__ = "730408456"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    inverted: dict[str, str] = {}
    keys = []
    for z in x:
        key: str = x[z]
        for m in keys:
            if key == m:
                raise KeyError("Duplicate keys")
        keys.append(key)
        inverted[key] = key
    print(inverted)
    return inverted


def favorite_color(c: dict[str, str]) -> str:
    """Returns the most common value of a dictionary."""
    new: dict[str, int] = {}
    mostfrequent: str = ""
    a: int = 0
    for i in c:
        if c[i] in new:
            new[c[i]] += 1
        else:
            new[c[i]] = 1
    for i in new:
        if new[i] > a:
            mostfrequent = i
            a = new[i]
    return mostfrequent


def count(a: list[str]) -> dict[str, int]:
    """Returns a dictionary that records how often a value appeared in an original list."""
    b: dict[str, int] = {}
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    return b