from math import prod
from typing import List, Set
from collections import defaultdict

from part1 import NumberBuilder


class DataHandler:
    GEAR_SYMBOL = "*"
    ROTATIONS = [(-1, -1), (-1, 0), (-1, 1),
                 ( 0, -1),          ( 0, 1),
                 ( 1, -1), ( 1, 0), ( 1, 1)]

    def __init__(self, filename: str):
        self._lines = self._load_input_file(filename)
        self._number_locations = self._build_number_locations()

    @classmethod
    def _load_input_file(cls, filename: str) -> List[str]:
        with open(filename) as f:
            return f.read().split("\n")

    def _build_number_locations(self):
        # For our needs it would be the best to have dict in format {y: {x: NumberLocationBuilder}}
        number_locations = defaultdict(dict)

        for y, line in enumerate(self._lines):
            number_builder = NumberBuilder()
            for x_reversed, character in enumerate(reversed(line)):
                if character.isdigit():
                    number_builder.add_string_digit(character)
                    number_locations[y][len(line) - 1 - x_reversed] = number_builder
                else:
                    # Number stops here, reset states and move on
                    number_builder = NumberBuilder()

        return number_locations

    def get_surrounding_numbers(self, x: int, y: int) -> Set[NumberBuilder]:
        surrounding_numbers = set()
        for relative_location in self.ROTATIONS:
            relative_x, relative_y = x + relative_location[0], y + relative_location[1]
            possible_numbers = self._number_locations.get(relative_y)
            if not possible_numbers:
                continue

            number = possible_numbers.get(relative_x)
            if not number or number in surrounding_numbers:
                continue

            surrounding_numbers.add(number)

        return surrounding_numbers

    def solve_gears(self) -> int:
        gear_ratio = 0
        for y, line in enumerate(self._lines):
            for x, character in enumerate(line):
                if character != self.GEAR_SYMBOL:
                    continue

                surrounding_numbers = self.get_surrounding_numbers(x, y)
                if len(surrounding_numbers) == 2:
                    gear_ratio += prod(surrounding_number.number for surrounding_number in surrounding_numbers)

        return gear_ratio


if __name__ == "__main__":
    print(DataHandler("input.txt").solve_gears())
