"""
Test cases for day 2
"""

import pytest

from aoc2020 import day2

TEST_CASES_1 = [
    ("1-3 a: abcde", True),
    ("1-3 b: cdefg", False),
    ("2-9 c: ccccccccc", True),
]

TEST_CASES_2 = [
    ("1-3 a: abcde", True),
    ("1-3 b: cdefg", False),
    ("2-9 c: ccccccccc", False),
]


@pytest.mark.parametrize("policy,expected", TEST_CASES_1)
def test_validate_first_star_policy(policy: str, expected: bool):
    """
    Test that a given password policy is valid according to the first stars' rules.
    """
    assert day2.validate_first_star_policy(policy) == expected


@pytest.mark.parametrize("policy,expected", TEST_CASES_2)
def test_validate_second_star_policy(policy: str, expected: bool):
    """
    Test that a given password policy is valid according to the second stars' rules.
    """
    assert day2.validate_second_star_policy(policy) == expected


def test_first_star():
    """
    Validating first star logic.
    """
    assert day2.first_star("answers/day2.txt") == 536


def test_second():
    """
    Validating second star logic.
    """
    assert day2.second_star("answers/day2.txt") == 558
