"""Relational Operators Exercise."""

__author__ = "730408456"

left_argument: str = input("Left hand side? ")

right_argument: str = input("Right hand side? ")

print(left_argument + " < " + right_argument + " is " + str(bool(left_argument < right_argument)))

print(left_argument + " >= " + right_argument + " is " + str(bool(left_argument >= right_argument)))

print(left_argument + " == " + right_argument + " is " + str(bool(left_argument == right_argument)))

print(left_argument + " != " + right_argument + " is " + str(bool(left_argument != right_argument)))