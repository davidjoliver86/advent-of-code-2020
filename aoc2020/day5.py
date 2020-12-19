"""
Day 5
"""
from operator import attrgetter
from typing import Iterable, Dict
from .utilities import lines_from_file

FIXTURE_PATH = "answers/day5.txt"


class BoardingPass:
    """
    Boarding passes are represented as a 10-character string:
        First seven letters: F or B.
        Last three letters: L or R
    Essentially, they're just binary: {F, L} = 0, and {B, R} = 1.

    The first seven characters represents the row, and the last three the column.
    """

    _CHAR_MAP: Dict[int, int] = {
        ord("F"): ord("0"),
        ord("L"): ord("0"),
        ord("B"): ord("1"),
        ord("R"): ord("1"),
    }

    def __init__(self, content: str):
        """
        Translate F and B to 0 and 1, then store their decimal values as row and
        column.
        """
        converted = content.translate(self._CHAR_MAP)
        self.row = int(converted[:7], 2)
        self.column = int(converted[7:], 2)

    @property
    def seat_id(self) -> int:
        """
        The seat ID is defined as multiplying the row by 8, then adding the column.

        :return: The seat ID.
        :rtype: int
        """
        return self.row * 8 + self.column


def get_boarding_passes(fixture_file: str) -> Iterable[BoardingPass]:
    """
    Read boarding pass data from a file and yield boarding passes.

    :return: Iterable of boarding passes.
    :rtype: Iterable[BoardingPass]
    """
    yield from (BoardingPass(line) for line in lines_from_file(fixture_file))


def first_star(fixture_path: str) -> int:
    """
    :return: The highest seat ID among the boarding passes.
    :rtype: int
    """
    passes = get_boarding_passes(fixture_path)
    return max(passes, key=attrgetter("seat_id")).seat_id


def second_star(fixture_path: str) -> int:
    """
    Your seat ID is missing. You know it's not at the extreme front or back. Assume
    every other seat ID is accounted for.

    :return: The seat ID missing in sequence.
    :rtype: int
    """
    passes = get_boarding_passes(fixture_path)
    seat_ids = sorted([bpass.seat_id for bpass in passes])

    # Comparing sequential pairs of seat IDs. If the difference is more than 1, we
    # can assume it's the missing ID. Return the previous seats' ID + 1.
    for i in range(1, len(seat_ids)):
        if seat_ids[i] - seat_ids[i - 1] > 1:
            return seat_ids[i - 1] + 1
    raise ValueError("Unable to find missing seat ID")


if __name__ == "__main__":
    print(first_star(FIXTURE_PATH))
    print(second_star(FIXTURE_PATH))
