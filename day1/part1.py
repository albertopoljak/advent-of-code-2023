from typing import Iterable


with open("input.txt") as f:
    lines = f.readlines()


def get_first_number(string_iterable: Iterable[str]) -> int:
    for i, character in enumerate(string_iterable):
        try:
            return int(character)
        except ValueError:
            pass

    raise Exception("No number found")



calibration_sum = 0
for line in lines:
    first_number, second_number = get_first_number(line), get_first_number(reversed(line))
    calibration_sum += first_number * 10 + second_number


print(calibration_sum)
