"""
Tests for day 7
"""
import pytest
from aoc2020.utilities import lines_from_file
from aoc2020 import day7
from aoc2020.day7 import Bag

EXAMPLE_BAGS = {
    "light red": [
        Bag(color="bright white", quantity=1),
        Bag(color="muted yellow", quantity=2),
    ],
    "dark orange": [
        Bag(color="bright white", quantity=3),
        Bag(color="muted yellow", quantity=4),
    ],
    "bright white": [Bag(color="shiny gold", quantity=1)],
    "muted yellow": [
        Bag(color="shiny gold", quantity=2),
        Bag(color="faded blue", quantity=9),
    ],
    "shiny gold": [
        Bag(color="dark olive", quantity=1),
        Bag(color="vibrant plum", quantity=2),
    ],
    "dark olive": [
        Bag(color="faded blue", quantity=3),
        Bag(color="dotted black", quantity=4),
    ],
    "vibrant plum": [
        Bag(color="faded blue", quantity=5),
        Bag(color="dotted black", quantity=6),
    ],
    "faded blue": [],
    "dotted black": [],
}

EXAMPLE_BAGS_2 = {
    "shiny gold": [Bag(color="dark red", quantity=2)],
    "dark red": [Bag(color="dark orange", quantity=2)],
    "dark orange": [Bag(color="dark yellow", quantity=2)],
    "dark yellow": [Bag(color="dark green", quantity=2)],
    "dark green": [Bag(color="dark blue", quantity=2)],
    "dark blue": [Bag(color="dark violet", quantity=2)],
    "dark violet": [],
}


@pytest.mark.parametrize("description", list(lines_from_file("test_cases/day7.txt")))
def test_bag_contents(description: str):
    """
    Test parsing the description of each bag.
    """
    color, bags = day7.bag_contents(description).popitem()
    assert EXAMPLE_BAGS[color] == bags


@pytest.mark.parametrize("color", EXAMPLE_BAGS.keys())
def test_contains_shiny_gold(color: str):
    """
    Validating the logic to determine which bags ultimately contain at least one
    shiny gold bag.
    """
    bag_contents = day7.contains(EXAMPLE_BAGS, color)
    contains_shiny_gold = any((bag.color == "shiny gold" for bag in bag_contents))
    should_contain = color in {
        "bright white",
        "muted yellow",
        "dark orange",
        "light red",
    }
    assert contains_shiny_gold == should_contain


def test_count_bags():
    """
    Validating the count_bags() logic.
    """
    assert day7.count_bags(EXAMPLE_BAGS_2, "shiny gold") == 126


def test_first_star():
    """
    Validating first star logic.
    """
    assert day7.first_star("answers/day7.txt") == 226


def test_second_star():
    """
    Validating second star logic.
    """
    assert day7.second_star("answers/day7.txt") == 9569
