# Advent of Code 2020

Running through Advent of Code 2020 in Python 3.8. I may backport these answers to
another language; most likely Go.

Aside from the mental stimulation of solving the problem at hand, the purpose of this
is not to necessarily demonstrate the "fastest" or "most clever one-line" solution, but
rather to demonstrate a pragmatic, "professional" approach to solving these problems
with respect to industry best practices.

## Conventions

* Everything is unit-tested against the examples provided. Pure TDD.
* Only Python code goes in the `aoc2020` folder. All puzzle input is saved in `fixtures`.
* Everything should be runnable as a module - e.g. `python -m aoc2020.day1`.
* Pylint code quality must be 10/10. No exceptions will be made yet.
* Code shall be formatted be `black`.
* Type annotations for function arguments and return types shall be used whenever possible.
* Remember that your input is not necessarily going to match mine. That being said,
  `tests` will contain spoilers. Tread carefully.

# Workflow
* Install the virtualenv: `poetry install`.
* Run `make`.
* Take a shot of egg nog.
