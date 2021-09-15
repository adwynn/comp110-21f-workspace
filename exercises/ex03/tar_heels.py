"""An exercise in remainders and boolean logic."""

__author__ = "730443412"


# Begin your solution here...

nmbr = int(input("Enter an int: "))
if nmbr % 2 == 0 and nmbr % 7 == 0:
    print("TAR HEELS")
elif nmbr % 2 == 0:
    print("TAR")
elif nmbr % 7 == 0:
    print("HEELS")
else:
    print("CAROLINA")
