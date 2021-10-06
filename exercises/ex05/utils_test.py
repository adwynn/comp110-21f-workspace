"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730443412"


def test_only_evens() -> None:
    assert len(only_evens([1, 5, 3])) == 0
    assert len(only_evens([2, 4, 6])) == 3
    assert len(only_evens([-1, -2, -3])) == 1


def test_sub() -> None:
    testList = [10, 5, 20, 30]
    assert len(sub(testList, 1, 3,)) == 2
    assert len(sub(testList, 1, 4,)) == 3
    assert len(sub(testList, 0, 7, )) == 4


def test_concat() -> None:
    list1 = [5, 2, 8]
    list2 = [10, 1, 4, 7]
    list3 = []
    assert len(concat(list1, list2)) == (len(list1) + len(list2))
    assert len(concat(list1, list1)) == (len(list1) + len(list1))
    assert(len(concat(list1, list3)) == len(list1))