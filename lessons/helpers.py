"""Examples of functions imported elsewhere."""

THE_ANSWER: int = 42


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


if __name__ == "__main__":
    print(f"imports.py: {__name__}")
    print("Evaluated as a program.")
else:
    print("Evaluated as an imported module.")