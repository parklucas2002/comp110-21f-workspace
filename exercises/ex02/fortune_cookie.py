"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730408456"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says... ")

fortune = randint(1, 4)

if fortune == 1:
    print("A big surprise is right around the corner! ")

if fortune == 2:
    print("You will be very successful in the future. ")

if fortune == 3:
    print("Someone in your life is your secret admirer. ")

if fortune == 4:
    print("The answer to your biggest question will be revealed very soon. ")

print("Now, go spread positive vibes! ")