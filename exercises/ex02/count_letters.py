"""Counting letters in a string."""

__author__ = "730408456"

letter = str(input("What letter do you want to search for? "))

word = str(input("Enter a word: "))

length = len(word)

x = 0

n = 0

while length > 0:
    if word[x] == letter:
        x = x + 1
        n = n + 1 
    else:
        x = x + 1
    length = length - 1

output = str(n)

print("Count: " + output)