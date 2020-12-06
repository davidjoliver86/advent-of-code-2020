.PHONY: pytest pylint

all: clean pytest pylint clean

clean:
	find . -name '__pycache__' -type 'd' | xargs rm -rf
	find . -name '.pytest_cache' -type 'd' | xargs rm -rf

pytest:
	poetry run pytest

pylint:
	poetry run pylint ./aoc2020 ./tests
