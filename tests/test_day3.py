"""
Test cases for day 3
"""

from aoc2020 import day3
from aoc2020.utilities import lines_from_file


def test_forest():
    """
    Validating that we hit 7 trees with the test pattern.
    """
    pattern = lines_from_file("test_cases/day3.txt")
    forest = day3.Forest(pattern)
    assert forest.traverse(3, 1) == 7


def test_first_star():
    """
    Validating first star logic.
    """
    assert day3.first_star("answers/day3.txt") == 193


def test_second_star():
    """
    Validating second star logic.
    """
    assert day3.second_star("answers/day3.txt") == 1355323200
