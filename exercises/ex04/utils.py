"""List utility functions."""

__author__ = "730443412"


# TODO: Implement your functions here.


def all(x: list[int], y: int) -> bool:
    z = 0
    while z < len(x):
        if x[z] != y:
            return False
        z += 1
    return True


def is_equal(x: list[int], y: list[int]) -> bool:
    z = 0
    while z < len(x):
        if x[z] != y[z]:
            return False
        z += 1
    return True