"""Repeating a beat in a loop."""

__author__ = "730443412"

# Begin your solution here...
i: int = 1
beat = str(input("What beat do you want to repeat?"))
repeat = int(input("How many times do you want to repeat it?"))
word: str = ""
word = beat
while i < repeat:
    word = word + " " + beat
    i += 1
print(word)
if repeat == 0 or repeat < 0:
    print("No beat...")