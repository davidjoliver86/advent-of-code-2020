# pylint: disable=redefined-outer-name
"""
Test cases for day 9
"""

import pytest

from aoc2020 import day9


@pytest.fixture
def test_number_list():
    """
    :return: Number list from example test cases.
    """
    return day9.get_number_list("test_cases/day9.txt")


@pytest.fixture
def actual_number_list():
    """
    :return: Actual number list input.
    """
    return day9.get_number_list("answers/day9.txt")


def test_xmas(test_number_list):
    """
    Validating the XMAS cipher.
    """
    first_invalid = next(day9.find_invalid_numbers(test_number_list, 5))
    assert first_invalid == 127


def test_contiguous_sum(test_number_list):
    """
    Validating the first part of the encryption weakness algorithm.
    """
    assert day9.find_contiguous_sum(test_number_list, 127) == [15, 25, 47, 40]


def test_encryption_weakness(test_number_list):
    """
    Validating the overall encryption weakness algorithm.
    """
    contiguous_sum = day9.find_contiguous_sum(test_number_list, 127)
    assert day9.find_encryption_weakness(contiguous_sum) == 62


def test_first_star(actual_number_list):
    """
    Validating first star logic.
    """
    assert day9.first_star(actual_number_list) == 1492208709


def test_second_star(actual_number_list):
    """
    Validating second star logic.
    """
    assert day9.second_star(actual_number_list, 1492208709) == 238243506
