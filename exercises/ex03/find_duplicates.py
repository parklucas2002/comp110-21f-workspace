"""Finding duplicate letters in a word."""

__author__ = "123456789"

word: str = input("Enter a word: ")

dupe: bool = False

i: int = 0

j: int = 1

while i < len(word):
    while j < len(word):
        if word[i] == word[j]:
            dupe: bool = True
            j += 1
        else:
            j += 1
    else:
        i += 1
        j = i + 1

print("Found duplicate: " + str(dupe))