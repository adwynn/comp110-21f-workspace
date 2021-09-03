"""This is the relational operators program for Comp 110"""
__author__ = "730443412"

left_side = int(input("Input number"))

right_side = int(input("Input Number"))

grtr_than: int = (left_side < right_side)
at_least: int = (left_side >= right_side)
equal: int = (left_side == right_side)
not_equal: int = (left_side != right_side)

print("Left-hand side: " + str(left_side))
print("Right-hand side: " + str(right_side))
print(str(left_side) + " < " + str(right_side) + " is " + str(grtr_than))
print(str(left_side) + " >= " + str(right_side) + " is " + str(at_least))
print(str(left_side) + " == " + str(right_side) + " is " + str(equal))
print(str(left_side) + " != " + str(right_side) + " is " + str(not_equal))