"""
Day 7
"""
import re
import functools
import collections
from typing import List, Dict, Collection
from .utilities import lines_from_file

Bag = collections.namedtuple("Bag", "color,quantity")

REGEX_BAG_COLOR = r"(\w+ \w+) bags contain"
REGEX_BAG_QUANTITY = r"(\d+) (\w+ \w+) bag"

FIXTURE_PATH = "answers/day7.txt"


def bag_contents(description: str) -> Dict[str, List[Bag]]:
    """
    Parse the description of the bag contents and return a dict of the bag with a list
    of the bags held by that bag.

    Does not attempt to do any recursive lookups; this strictly parses the description
    and returns the bags in that line.

    :return: A dict with a list of the color and quantity of bags held according to
    the description.
    """
    color = re.match(REGEX_BAG_COLOR, description).group(1)
    bags = []
    if "no other bags" not in description:
        bags = [
            Bag(color=match[1], quantity=int(match[0]))
            for match in re.findall(REGEX_BAG_QUANTITY, description)
        ]
    return {color: bags}


@functools.lru_cache
def generate_bags_from_file(filename: str) -> Dict[str, List[Bag]]:
    """
    Read a file of bag descriptions, then generate a dictionary of all bags found and
    their contents.
    """
    bags = {}
    for line in lines_from_file(filename):
        bags.update(bag_contents(line))
    return bags


def contains(bags: Dict[str, List[Bag]], starting_bag_color: str) -> Collection[Bag]:
    """
    From a given starting bag color, recursively determine the total contents of that
    bag, taking into account all the bags those bags contain, etc.

    This function doesn't necessarily care about total *counts* of bags, just what's
    recursively in the bags at a higher level.

    :return: A collection of all bags encountered.
    """
    processed = collections.deque()
    to_process = collections.deque(bags[starting_bag_color])
    while to_process:
        item = to_process.popleft()
        processed.append(item)
        to_process.extend(bags[item.color])
    return processed


def count_bags(bags: Dict[str, List[Bag]], starting_bag_color: str) -> int:
    """
    :return: The total number of bags recursively found within the bag, not including
    the starting bag itself.
    """
    searching = collections.deque(bags[starting_bag_color])
    total = 0
    while searching:
        this_bag = searching.popleft()
        total += this_bag.quantity
        searching.extend(bags[this_bag.color] * this_bag.quantity)
    return total


def first_star(fixture_path: str) -> int:
    """
    Use contains() on each starting bag color to see which ones contain a shiny
    gold bag at some point in their unboxing.

    :return: The number of starting bag colors that ultimately contain a shiny
    gold bag.
    """
    bags = generate_bags_from_file(fixture_path)
    contains_shiny_gold = {
        color: any((bag.color == "shiny gold" for bag in contains(bags, color)))
        for color in bags
    }
    return list(contains_shiny_gold.values()).count(True)


def second_star(fixture_path: str) -> int:
    """
    Use count_bags() to determine how many total recursive bags are within one shiny
    gold bag.

    :return: The grand total of all recursive sub-bags within one shiny gold bag.
    """
    bags = generate_bags_from_file(fixture_path)
    return count_bags(bags, "shiny gold")


if __name__ == "__main__":
    print(first_star(FIXTURE_PATH))
    print(second_star(FIXTURE_PATH))
