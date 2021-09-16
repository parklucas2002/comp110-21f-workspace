"""An exercise in remainders and boolean logic."""

__author__ = "730408456"


x = int(input("Enter an int: "))

if x % 2 == 0 and x % 7 == 0:
    print("TAR HEELS")
else:
    if x % 2 == 0:
        print("TAR")
    else:
        if x % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")