"""
Day 8
"""
from typing import List
from copy import deepcopy
from .console import Console, ProgramHalted
from .utilities import lines_from_file

FIXTURE_PATH = "answers/day8.txt"


class TrackingConsole(Console):
    """
    TrackingConsole keeps a track of all instruction indicies visited. As soon as
    a duplicate instruction is encountered, it's likely we're in an infinite loop, so
    immediately raise ProgramHalted.
    """

    def __init__(self, instructions: List[str]):
        super().__init__(instructions)
        self._visited: List[int] = []

    def pre_exec_hook(self):
        """
        Add the current index to the list of visited indicies.
        If the current index has been visited twice, halt the program.
        """
        if self._current in self._visited:
            raise ProgramHalted
        self._visited.append(self._current)


def first_star(fixture_path: str) -> int:
    """
    Run the provided program, and return the accumulator value when ProgramHalted
    is raised.

    :return: Accumulator value at the time ProgramHalted is raised.
    """
    instructions = list(lines_from_file(fixture_path))
    console = TrackingConsole(instructions)
    try:
        console.run()
    except ProgramHalted:
        pass
    return console.accumulator


def second_star(fixture_path: str) -> int:
    """
    There should be exactly one jmp or nop instruction that needs to be changed to the
    other. After finding what that is, return the value of the accumulator.

    We should assume that if ProgramHalted is raised from the TrackingConsole that we
    didn't change the right instruction. Therefore, we try every line until we find
    the right one.

    :return: Accumulator value from the program run that did not raise ProgramHalted.
    """
    instructions = list(lines_from_file(fixture_path))
    for index, line in enumerate(instructions):
        # Skip if it's an acc instruction.
        if line.startswith("acc"):
            continue
        new_instructions = deepcopy(instructions)
        if line.startswith("jmp"):
            new_instructions[index] = line.replace("jmp", "nop")
        if line.startswith("nop"):
            new_instructions[index] = line.replace("nop", "jmp")

        # Run the new instructions.
        console = TrackingConsole(new_instructions)
        try:
            console.run()
            return console.accumulator
        except ProgramHalted:
            continue


if __name__ == "__main__":
    print(first_star(FIXTURE_PATH))
    print(second_star(FIXTURE_PATH))
