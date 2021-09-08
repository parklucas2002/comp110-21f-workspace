"""Repeating a beat in a loop."""

__author__ = "730408456"

beat = str(input("What beat do you want to repeat? "))

beats = beat

x = int(input("How many times do you want to repeat it? "))

if x < 1: 
    print("No beat...")
else:
    while x > 1:
        beats = beats + " " + beat
        x = x - 1
    print(beats)