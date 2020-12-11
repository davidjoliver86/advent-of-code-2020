"""
Test cases for day 4
"""

from aoc2020 import day4


def test_valid_passports_part_1():
    """
    Validating password rules are correct per part 1:
    All fields must be present except for cid. No value validation is performed.
    """
    valid = [
        passport.is_valid_part_1()
        for passport in day4.get_passports("test_cases/day4.txt")
    ]
    assert valid == [True, False, True, False]


def test_valid_passports_part_2():
    """
    Validating password rules are correct per part 2:
    All fields must be present except for cid. Value validation done on other fields.

    I combined the first four invalid passwords with the next four valid ones.
    """
    valid = [
        passport.is_valid_part_2()
        for passport in day4.get_passports("test_cases/day4_part2.txt")
    ]
    assert valid == [False] * 4 + [True] * 4


def test_first_star():
    """
    Validating first star logic.
    """
    assert day4.first_star("answers/day4.txt") == 264


def test_second_star():
    """
    Validating second star logic.
    """
    assert day4.second_star("answers/day4.txt") == 224
