"""
Test cases for Day 5
"""
import pytest
from aoc2020 import day5

TEST_CASES = [
    # Input, row, column, seat ID
    ("FBFBBFFRLR", 44, 5, 357),
    ("BFFFBBFRRR", 70, 7, 567),
    ("FFFBBBFRRR", 14, 7, 119),
    ("BBFFBBFRLL", 102, 4, 820),
]


@pytest.mark.parametrize("data,row,column,seat_id", TEST_CASES)
def test_boarding_pass(data: str, row: int, column: int, seat_id: int):
    """
    Validating row, column, and seat ID logic.
    """
    boarding_pass = day5.BoardingPass(data)
    row_valid = boarding_pass.row == row
    column_valid = boarding_pass.column == column
    seat_id_valid = boarding_pass.seat_id == seat_id
    assert all((row_valid, column_valid, seat_id_valid))


def test_first_star():
    """
    Validating first star logic.
    """
    assert day5.first_star("answers/day5.txt") == 896


def test_second_star():
    """
    Validating second star logic.
    """
    assert day5.second_star("answers/day5.txt") == 659
