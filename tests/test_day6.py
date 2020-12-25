"""
Tests for day 6
"""
import pytest
from aoc2020 import day6
from aoc2020.utilities import line_chunks_from_file

TEST_CASE = [
    ["abc"],
    ["a", "b", "c"],
    ["ab", "ac"],
    ["a", "a", "a", "a"],
    ["b"],
]

TEST_CASE_UNIQUE_LETTERS = [3, 3, 3, 1, 1]
TEST_CASE_LETTERS_IN_EVERY_LINE = [3, 0, 1, 1, 1]


def test_line_chunks_from_file():
    """
    Test functionality of line_chunks_from_file().
    """
    assert list(line_chunks_from_file("test_cases/line_chunk.txt")) == TEST_CASE


@pytest.mark.parametrize(
    "letter_list,unique_letters", zip(TEST_CASE, TEST_CASE_UNIQUE_LETTERS)
)
def test_count_unique_letters(letter_list, unique_letters):
    """
    Test functionality of count_unique_letters().
    """
    assert day6.count_unique_letters(letter_list) == unique_letters


@pytest.mark.parametrize(
    "letter_list,in_every_line", zip(TEST_CASE, TEST_CASE_LETTERS_IN_EVERY_LINE)
)
def test_count_letters_in_every_line(letter_list, in_every_line):
    """
    Test functionality of count_letters_in_every_line().
    """
    assert day6.count_letters_in_every_line(letter_list) == in_every_line


def test_first_star():
    """
    Validating first star logic.
    """
    assert day6.first_star("answers/day6.txt") == 6878


def test_second_star():
    """
    Validating second star logic.
    """
    assert day6.second_star("answers/day6.txt") == 3464
