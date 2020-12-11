"""
Day 4
"""
import re
from dataclasses import dataclass
from typing import Optional, Iterable

from .utilities import lines_from_file

FIXTURE_PATH = "answers/day4.txt"


@dataclass
class Passport:
    """
    Passport data for a traveler out of the North Pole.
    """

    byr: Optional[str] = None  # Birth year
    iyr: Optional[str] = None  # Issue year
    eyr: Optional[str] = None  # Expiration year
    hgt: Optional[str] = None  # Height
    hcl: Optional[str] = None  # Hair color
    ecl: Optional[str] = None  # Eye color
    pid: Optional[str] = None  # Passport ID
    cid: Optional[str] = None  # Country ID

    def _valid_birth_year(self) -> bool:
        """
        :return: Birthdate is between 1920-2002.
        :rtype: bool
        """
        try:
            return 1920 <= int(self.byr) <= 2002
        except TypeError:
            return False

    def _valid_issue_year(self) -> bool:
        """
        :return: Issue year is between 2010-2020.
        :rtype: bool
        """
        try:
            return 2010 <= int(self.iyr) <= 2020
        except TypeError:
            return False

    def _valid_expiration_year(self) -> bool:
        """
        :return: Expiration year is between 2020-2030.
        :rtype: bool
        """
        try:
            return 2020 <= int(self.eyr) <= 2030
        except TypeError:
            return False

    def _valid_height(self) -> bool:
        """
        Height must be expressed as [0-9]+(cm|in).
        :return: If cm, 150-193. If inches, 59-76.
        :rtype: bool
        """
        try:
            if match := re.match(r"(\d+)(in|cm)", self.hgt):
                units, measurement = match.groups()
                if measurement == "in":
                    return 59 <= int(units) <= 76
                if measurement == "cm":
                    return 150 <= int(units) <= 193
            return False
        except TypeError:
            return False

    def _valid_hair_color(self) -> bool:
        """
        Hair color must be expressed as $[0-9a-f]{6}.
        :return: If the hair color is valid.
        :rtype: bool
        """
        try:
            return bool(re.match(r"#[0-9a-f]{6}$", self.hcl))
        except TypeError:
            return False

    def _valid_eye_color(self) -> bool:
        """
        Eye color must be one of: amb blu brn gry grn hzl oth
        :return: If the eye color is valid.
        :rtype: bool
        """
        return self.ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def _valid_passport_id(self) -> bool:
        """
        Must be exactly 9 digits.
        :return: If the passport ID is exactly 9 digits, including leading zeroes.
        :rtype: bool
        """
        try:
            return bool(re.match(r"[0-9]{9}$", self.pid))
        except TypeError:
            return False

    def is_valid_part_1(self) -> bool:
        """
        All fields are required except cid to be considered valid.

        :return: Whether the passwport is valid.
        :rtype: bool
        """
        return all(
            (self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid)
        )

    def is_valid_part_2(self) -> bool:
        """
        All fields are required except cid. Must pass all validation rules defined.

        :return: Whether the passwport is valid.
        :rtype: bool
        """
        return all(
            (
                self._valid_birth_year(),
                self._valid_expiration_year(),
                self._valid_eye_color(),
                self._valid_hair_color(),
                self._valid_height(),
                self._valid_issue_year(),
                self._valid_passport_id(),
            )
        )


def get_passports(fixture_file: str) -> Iterable[Passport]:
    """
    Read passport data from a file and yield passports.

    :return: Iterable of passports.
    :rtype: Iterable[Passport]
    """
    passport = Passport()
    for line in lines_from_file(fixture_file):
        if not line:
            yield passport
            passport = Passport()
        for field in line.split():
            name, value = field.split(":")
            setattr(passport, name, value)
    yield passport


def first_star(fixture_path: str) -> int:
    """
    :return: The number of valid passports.
    :rtype: int
    """
    return [
        passport.is_valid_part_1() for passport in get_passports(fixture_path)
    ].count(True)


def second_star(fixture_path: str) -> int:
    """
    :return: The number of valid passports according to field validation rules.
    :rtype: int
    """
    return [
        passport.is_valid_part_2() for passport in get_passports(fixture_path)
    ].count(True)


if __name__ == "__main__":
    print(first_star(FIXTURE_PATH))
    print(second_star(FIXTURE_PATH))
