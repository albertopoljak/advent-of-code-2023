import string
from typing import List, Set


"""
Idea is to go trough each line in reverse and build the found number, at the same time check if any digit
is adjected to symbol and if it is mark the built number as valid.
"""


class NumberBuilder:
    def __init__(self):
        self._built_number = 0
        self._exponent = 0
        self._exponent_base = 10

    @property
    def number(self) -> int:
        return self._built_number

    @classmethod
    def ensure_valid_digit(cls, digit: str):
        """
        :param digit: str single digit number
        :raise: ValueError if digit is not a single digit number.
        """
        if len(digit) != 1:
            raise ValueError(f"Digit {digit} has to be single digit.")

        return int(digit)

    def add_string_digit(self, digit: str):
        self._built_number += self.ensure_valid_digit(digit) * self._exponent_base ** self._exponent
        self._exponent += 1

    def __hash__(self):
        return hash(id(self))


class DataHandler:
    BREAK_CHARACTER = "."
    VALID_SYMBOLS = set(string.punctuation.replace(BREAK_CHARACTER, ""))
    ROTATIONS = [(-1, -1), (-1, 0), (-1, 1),
                 ( 0, -1),          ( 0, 1),
                 ( 1, -1), ( 1, 0), ( 1, 1)]

    def __init__(self, filename: str):
        self.lines = self._load_input_file(filename)

    @classmethod
    def _load_input_file(cls, filename: str) -> List[str]:
        with open(filename) as f:
            return f.read().split("\n")

    def is_surrounded_by(self, x: int, y: int, character_set: Set[str]) -> bool:
        for relative_location in self.ROTATIONS:
            try:
                character = self.lines[y + relative_location[1]][x + relative_location[0]]
                if character in character_set:
                    return True
            except IndexError:
                pass  # Ignore direction out of range, doesn't exist.

        return False

    def solve_valid_engine_number(self) -> List[int]:
        valid_engine_numbers = []

        for y, line in enumerate(self.lines):
            number_builder = NumberBuilder()
            is_valid_engine_part = False

            for x_reversed, character in enumerate(reversed(line)):
                if character.isdigit():
                    number_builder.add_string_digit(character)
                    if not is_valid_engine_part:  # No need to double-check
                        is_valid_engine_part = self.is_surrounded_by(len(line) - 1 - x_reversed, y, self.VALID_SYMBOLS)
                else:
                    # Number stops here, save it, reset states and move on
                    if is_valid_engine_part and number_builder.number:
                        valid_engine_numbers.append(number_builder.number)

                    # Reset state
                    number_builder = NumberBuilder()
                    is_valid_engine_part = False

            if is_valid_engine_part and number_builder.number:
                valid_engine_numbers.append(number_builder.number)

        return valid_engine_numbers


if __name__ == "__main__":
    print(sum(DataHandler("input.txt").solve_valid_engine_number()))
