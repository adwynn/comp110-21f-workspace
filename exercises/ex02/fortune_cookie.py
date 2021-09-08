"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730443412"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint
# Begin your solution here..
ri = randint(1,4)
print("Your fortune cookie says...")
if (ri == 1):
    print("A sum of money is headed your way!")
elif (ri == 2):
    print("A lovely person is about to enter your life")
elif (ri == 3):
    print("I sense a string of good luck soon!")
else:
    print("Try something new! Something amazing will happen!")
print("Now, go spread positive vibes!")
