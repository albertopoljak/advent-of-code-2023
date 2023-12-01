NUMBER_MAPPINGS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
LONGEST_NUMBER_LENGTH = len(max(NUMBER_MAPPINGS, key=lambda m: len(m)))


with open("input.txt") as f:
    lines = f.read().split("\n")


def get_first_number(input_string: str, *, reverse: bool = False) -> int:
    if reverse:
        start_index, end_index, step = len(input_string) - 1, -1 , -1
    else:
        start_index, end_index, step = 0, len(input_string), 1

    for current_index in range(start_index, end_index, step):
        try:
            return int(input_string[current_index])
        except ValueError:
            pass

        for number_string in NUMBER_MAPPINGS:
            try:
                number_string_index = input_string.index(number_string, current_index, current_index + LONGEST_NUMBER_LENGTH)
            except ValueError:
                pass
            else:
                if number_string_index == current_index:
                    return NUMBER_MAPPINGS[number_string]

    raise Exception("No number found")



calibration_sum = 0
for line in lines:
    first_number, second_number = get_first_number(line), get_first_number(line, reverse=True)
    calibration_sum += first_number * 10 + second_number


print(calibration_sum)
