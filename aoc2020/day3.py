"""
Day 3
"""
from math import prod
from typing import List, Iterable
from .utilities import lines_from_file

EMPTY = "."
TREE = "#"

FIXTURE_PATH = "answers/day3.txt"


class Forest:
    """
    Represents a forest of trees. Initliazed from a text file with a rectangular grid
    of empty spaces (.) or trees (#).
    """

    _forest: List[str] = []

    def __init__(self, pattern: Iterable[str]):
        """
        Initialize empty pattern.

        :pattern:
        """
        self._forest = list(pattern)

    @property
    def width(self) -> int:
        """
        :return: Width of the forest.
        :rtype: int
        """
        return len(self._forest[0])

    @property
    def height(self) -> int:
        """
        :return: Height of the forest.
        :rtype: int
        """
        return len(self._forest)

    def _extend(self) -> int:
        """
        Double the width of the forest by repeating each lines' pattern.
        """
        for index, line in enumerate(self._forest):
            self._forest[index] = line + line

    def _is_tree(self, x_coord: int, y_coord: int) -> bool:
        """
        :x_coord: 0-indexed x-coordinate.
        :y_coord: 0-indexed y-coordinate.
        :return: If the space at (x, y) is a tree.
        :rtype: bool
        """
        return self._forest[y_coord][x_coord] == TREE

    def traverse(self, delta_x: int, delta_y: int) -> int:
        """
        Starting at the top-left corner, going right <delta_x> spaces at a time, and
        down <delta_y> spaces at a time, count the number of trees you encounter.

        If you extend beyond the right edge, call _extend(). If you extend past the
        bottom, stop.

        :dx: Number of spaces to move right each step.
        :dy: Number of spaces to move down each step.
        :return: Number of trees encountered.
        :rtype: int
        """
        current_x = 0
        current_y = 0
        trees_encountered = 0

        while current_y < self.height:

            # Increment trees_encountered if we can.
            if self._is_tree(current_x, current_y):
                trees_encountered += 1

            # Move.
            current_x += delta_x
            current_y += delta_y

            # If we went beyond the forests' width, extend it. This is a loop in case
            # dx is such a large value, multiple _extend() calls are necessary.
            while current_x >= self.width:
                self._extend()

        return trees_encountered


def first_star(fixture_path):
    """
    Using the provided input, traverse the forest going down a (3,1) slope.

    :return: Number of trees encountered.
    :rtype: int
    """
    pattern = lines_from_file(fixture_path)
    trees_encountered = Forest(pattern).traverse(3, 1)
    return trees_encountered


def second_star(fixture_path):
    """
    Make five separate runs - (1,1), (3,1), (5,1), (7,1), and (1,2).
    Return the product of all five runs.

    :return: Number of trees encountered.
    :rtype: int
    """
    pattern = lines_from_file(fixture_path)
    forest = Forest(pattern)
    runs = [
        forest.traverse(slope_x, slope_y)
        for slope_x, slope_y in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    ]
    return prod(runs)


if __name__ == "__main__":
    print(first_star(FIXTURE_PATH))
    print(second_star(FIXTURE_PATH))
