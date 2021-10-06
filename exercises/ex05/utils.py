"""List utility functions part 2."""

__author__ = "730443412"

# Define your functions below


def only_evens(x: list[int]) -> list[int]:
    result: list[int] = []
    for num in x:
        if num % 2 == 0:
            result.append(num)
    return result


def sub(x: list[int], start: int, end: int) -> list[int]:
    result: list[int] = []
    if start < 0: 
        start = 0
    if end > len(x):
        end = len(x)
    while start < end:
        result.append(x[start])
        start += 1
    return result


def concat(x: list[int], y: list[int]) -> list[int]:
    newList: list[int] = []
    i = 0
    j = 0
    while i < len(x):
        newList.append(x[i])
        i += 1
    while j < len(y):
        newList.append(y[j])
        j += 1
    return newList
