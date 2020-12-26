"""
Virtual machine representing the game console in Day 8.
I figure this is probably this year's version of "Intcode".
"""
from typing import List, Tuple, Callable


class ProgramHalted(Exception):
    """
    When raised, immediately halts program execution.
    """

    pass  # pylint: disable=unnecessary-pass


class Console:
    """
    Representation of the "game console" as a VM.
    """

    def __init__(self, instructions: List[str]):
        """
        Pass in a list of instructions, then start the computer.
        """
        self._instructions: List[str] = instructions

        # Initlialize accumulator.
        self._accumulator: int = 0

        # Initlialize index of current instruction.
        self._current: int = 0

    def parse_instruction(self, instruction: str) -> Tuple[Callable, int]:
        """
        Parses an instruction line to determine the function to be called.

        :return: A tuple of the function itself and the int-cast value.
        """
        instruction_name, value = instruction.split()
        instruction_func = getattr(self, f"_{instruction_name}")
        return (instruction_func, int(value))

    # Instruction functions, what's your conjunction?

    def _nop(self):
        """
        Does nothing except increment the current index.
        """
        self._current += 1

    def _acc(self, value: int):
        """
        Adds value to the accumulator, then increments the current index.
        """
        self._accumulator += value
        self._current += 1

    def _jmp(self, value: int):
        """
        Adds value to the current index.
        """
        self._current += value

    def run(self):
        """
        Run the program.

        For now, we assume that reaching the end of the instruction list halts the
        program. Also, it's the instructions' responsibility to alter the current index
        since not all instructions are handled equally.
        """
        program_length = len(self._instructions)
        while self._current < program_length:
            instruction = self._instructions[self._current]
            inst_func, argument = self.parse_instruction(instruction)
            self.pre_exec_hook()
            if inst_func == self._nop:  # pylint: disable=comparison-with-callable
                inst_func()
            else:
                inst_func(argument)

    @property
    def accumulator(self):
        """
        :return: Value of the accumulator.
        """
        return self._accumulator

    def pre_exec_hook(self):
        """
        Overridden as needed to handle events before every instruction.
        """
        pass  # pylint: disable=unnecessary-pass
