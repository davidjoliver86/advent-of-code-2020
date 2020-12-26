"""
Test cases for Day 8
"""
from aoc2020 import day8
from aoc2020.console import ProgramHalted

TEST_PROGRAM = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

# The "fixed" test program from part 2.

FIXED_TEST_PROGRAM = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
nop -4
acc +6
"""


def test_tracking_console():
    """
    Validating functionality of the TrackingConsole.
    When the program halts, the accumulator should be 5.
    """
    console = day8.TrackingConsole(TEST_PROGRAM.splitlines())
    try:
        console.run()
    except ProgramHalted:
        assert console.accumulator == 5


def test_console_on_fixed_program():
    """
    Validating functionality of the fixed program.
    When the program halts, the accumulator should be 8.
    """
    console = day8.TrackingConsole(FIXED_TEST_PROGRAM.splitlines())
    console.run()
    assert console.accumulator == 8


def test_first_star():
    """
    Validating first star logic.
    """
    assert day8.first_star("answers/day8.txt") == 1584


def test_second_star():
    """
    Validating second star logic.
    """
    assert day8.second_star("answers/day8.txt") == 920
