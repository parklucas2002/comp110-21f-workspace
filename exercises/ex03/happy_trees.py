"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth = int(input("Depth: "))

i: int = 0

trees: str = ("")

if depth <= 0:
    print()
else:
    while depth > i:
        trees = trees + TREE
        print(trees)
        i += 1