"""
Day 9
"""
from typing import List
from itertools import combinations
from .utilities import lines_from_file

FIXTURE_PATH = "answers/day9.txt"


def get_number_list(filename: str) -> List[int]:
    """
    Read contents of a file and cast them to ints.
    :return: The integers from filename
    """
    return [int(num) for num in lines_from_file(filename)]


def find_contiguous_sum(numbers: List[int], target_sum: int) -> List[int]:
    """
    In the list of numbers, find a contiguous set of two or more numbers that add up
    to the target number.

    :return: A list of all numbers - found contiguously - that sum up to target_sum.
    """
    for index, start in enumerate(numbers):
        contiguous_set = [start]
        while sum(contiguous_set) < target_sum:
            for _, num in enumerate(numbers[index + 1 :]):
                contiguous_set.append(num)
                if sum(contiguous_set) == target_sum:
                    return contiguous_set
    return []


def find_encryption_weakness(numbers: List[int]) -> int:
    """
    The encryption weakness is simply the sum of the lowest and highest numbers from
    the result of find_contiguous_sum() above.

    :return: The sum of the lowest and highest numbers in the list.
    """
    return min(numbers) + max(numbers)


def find_invalid_numbers(numbers: List[int], preamble_size: int) -> int:
    """
    The "preamble" in the list of numbers is the first <preamble_size> integers in the
    list that don't follow any particular rule. Every subsequent number in the list must
    be the sum of any two unique <preamble_size> numbers immediately preceding it.

    We take the size of the preamble and apply this rule to the list of numbers, then
    determine all combinations of sums of two numbers. If there's a number that does
    *not* comply with this rule, yield it.

    :yield: Numbers that don't follow the "sum of any two previous numbers rule".
    """
    for index, num in enumerate(numbers[preamble_size:], preamble_size):
        start = index - preamble_size
        previous_chunk = numbers[start:index]
        valid = False
        for first, second in combinations(previous_chunk, 2):
            if first + second == num:
                valid = True
                break
        if not valid:
            yield num


def first_star(numbers: List[int]) -> int:
    """
    Use the provided input and a preamble_size of 25; find the first invalid number.
    :return: The first invalid number encountered.
    """
    return next(find_invalid_numbers(numbers, 25))


def second_star(numbers: List[int], target_sum: int) -> int:
    """
    Take the target sum from the first_star - use that to find the encryption weakness.
    :return: The encryption weakness.
    """
    contiguous_sum = find_contiguous_sum(numbers, target_sum)
    return find_encryption_weakness(contiguous_sum)


if __name__ == "__main__":
    nums = get_number_list(FIXTURE_PATH)
    first_invalid = first_star(nums)
    print(first_invalid)
    print(second_star(nums, first_invalid))
