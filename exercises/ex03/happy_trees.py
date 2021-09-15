"""Drawing forests in a loop."""

__author__ = "730443412"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
i: int = 0
depth = int(input("Enter an integer depth: "))
row: str = ""
row = TREE
while i < depth:
    row = row + TREE
    i += 1
    print(row)
if depth == 0 or depth < 0:
    print("")