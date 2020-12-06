"""
Day 1
"""
from functools import lru_cache
from .utilities import lines_from_file

FIXTURE_PATH = "answers/day1.txt"


@lru_cache
def get_expense_report(fixture_path: str):
    """
    Read the file and return a list of ints.
    """
    return [int(l) for l in lines_from_file(fixture_path)]


def first_star(fixture_path: str):
    """
    Find two numbers in the file that add up to 2020, then return their product.
    """
    expenses = get_expense_report(fixture_path)
    for index, num1 in enumerate(expenses):
        for _, num2 in enumerate(expenses[index + 1 :]):
            if num1 + num2 == 2020:
                return num1 * num2
    raise AssertionError("Cannot find two numbers that sum to 2020")


def second_star(fixture_path: str):
    """
    Find three numbers in the file that add up to 2020, then return their product.
    """
    expenses = get_expense_report(fixture_path)
    for index, num1 in enumerate(expenses):
        for _, num2 in enumerate(expenses[index + 1 :]):
            for _, num3 in enumerate(expenses[index + 2 :]):
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3
    raise AssertionError("Cannot find three numbers that sum to 2020")


if __name__ == "__main__":
    print(first_star(FIXTURE_PATH))
    print(second_star(FIXTURE_PATH))
