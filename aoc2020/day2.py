"""
Day 2
"""
import re
from typing import Callable
from .utilities import lines_from_file

PASSWORD_PATTERN = re.compile(
    r"(?P<low>\d+)-(?P<high>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)"
)
FIXTURE_PATH = "answers/day2.txt"


def validate_first_star_policy(policy: str) -> bool:
    """
    Evaluate a given password policy and a sample policy.

    Policy statements are defined as:
      <[0-9]:n1>-<[0-9]:n2> <[a-z]:letter>: <str:password>

    Where n2 > n1. A valid password is one that contains between <n1>-<n2> (inclusive)
    occurrences of <letter>.

    :return: Whether the password is valid given its policy.
    :rtype: bool
    """
    groups = PASSWORD_PATTERN.match(policy).groupdict()
    low = int(groups["low"])
    high = int(groups["high"])
    letter = groups["letter"]
    password = groups["password"]

    letter_occurences = password.count(letter)
    return low <= letter_occurences <= high


def validate_second_star_policy(policy: str) -> bool:
    """
    Same policy definitions as above, but a new interpretation of the rules.

    The <n1>'th *xor* <n2>'th character in the password must be <letter>. 1-indexed.

    :return: Whether the password is valid given its policy.
    :rtype: bool
    """
    groups = PASSWORD_PATTERN.match(policy).groupdict()
    low = int(groups["low"])
    high = int(groups["high"])
    letter = groups["letter"]
    password = groups["password"]

    first_match = password[low - 1] == letter
    second_match = password[high - 1] == letter

    return (first_match and not second_match) or (second_match and not first_match)


def _star(fixture_path: str, func: Callable[[str], int]) -> int:
    """
    Helper function to count passwords that conform to a policy function.
    """
    return [func(policy) for policy in lines_from_file(fixture_path)].count(True)


def first_star(fixture_path: str) -> int:
    """
    :return: The number of passwords that conform to the first stars' rule.
    :rtype: int
    """
    return _star(fixture_path, validate_first_star_policy)


def second_star(fixture_path: str) -> int:
    """
    :return: The number of passwords that conform to the second stars' rule.
    :rtype: int
    """
    return _star(fixture_path, validate_second_star_policy)


if __name__ == "__main__":
    print(first_star(FIXTURE_PATH))
    print(second_star(FIXTURE_PATH))
