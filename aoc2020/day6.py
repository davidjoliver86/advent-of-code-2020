"""
Day 6
"""
from typing import List
from collections import Counter
from functools import reduce
from .utilities import line_chunks_from_file


FIXTURE_PATH = "answers/day6.txt"


def count_unique_letters(letter_list: List[str]) -> int:
    """
    :return: The number of unique letters among all strings in letter_list.
    """

    def merge_counters(counter_1: Counter, counter_2: Counter) -> Counter:
        """
        :return: The combined counter after calling counter_1.update(counter_2).
        """
        counter_1.update(counter_2)
        return counter_1

    counter = reduce(merge_counters, letter_list, Counter())
    return len(counter.keys())


def count_letters_in_every_line(letter_list: List[str]) -> int:
    """
    :return: The number of letters that appear in all strings in letter_list.
    """
    in_all = reduce(set.intersection, (set(letters) for letters in letter_list))
    return len(in_all)


def first_star(fixture_path: str) -> int:
    """
    :return: The sum of each groups' unique 'yes' responses.
    """
    counts = [
        count_unique_letters(chunk) for chunk in line_chunks_from_file(fixture_path)
    ]
    return sum(counts)


def second_star(fixture_path: str) -> int:
    """
    :return: The sum of questions within each group of which all respondants answered
    "yes".
    """
    counts = [
        count_letters_in_every_line(chunk)
        for chunk in line_chunks_from_file(fixture_path)
    ]
    return sum(counts)


if __name__ == "__main__":
    print(first_star(FIXTURE_PATH))
    print(second_star(FIXTURE_PATH))
