"""Numeric operators for Comp 110"""
__author__ = "730443412"

left_side = int(input("Input number"))

right_side = int(input("Input Number"))

mult: int = (left_side ** right_side)
divd: int = (left_side / right_side)
remain: int = (left_side // right_side)
mod: int = (left_side % right_side)

print("Left-hand side: " + str(left_side))
print("Right-hand side: " + str(right_side))
print(str(left_side) + " ** " + str(right_side) + " is " + str(mult))
print(str(left_side) + " / " + str(right_side) + " is " + str(divd))
print(str(left_side) + " // " + str(right_side) + " is " + str(remain))
print(str(left_side) + " % " + str(right_side) + " is " + str(mod))
