"""
Test cases for day 1
"""

from aoc2020 import day1


def test_first_star():
    """
    Validating first star logic.
    """
    assert day1.first_star("test_cases/day1.txt") == 514579


def test_second():
    """
    Validating second star logic.
    """
    assert day1.second_star("test_cases/day1.txt") == 241861950
