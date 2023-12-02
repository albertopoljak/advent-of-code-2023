from typing import List, Dict


class GameLineParser:
    def __init__(self, input_game_line: str):
        self._game_id, self._cube_subsets = self.parse_input_game_line_data(input_game_line)

    @property
    def game_id(self) -> int:
        return self._game_id

    @classmethod
    def _parse_game_id_partition(cls, game_id_partition: str) -> int:
        return int(game_id_partition.replace("Game", ""))

    @classmethod
    def _parse_cube_subsets_partition(cls, cube_subsets_partition: str) -> List[str]:
        return cube_subsets_partition.split(";")

    @classmethod
    def parse_input_game_line_data(cls, input_game_line: str):
        game_id_partition, cube_subsets_partition = input_game_line.split(":")
        return cls._parse_game_id_partition(game_id_partition), cls._parse_cube_subsets_partition(cube_subsets_partition)

    @classmethod
    def _parse_cube_subset(cls, cube_subset: str) -> Dict[str, int]:
        cube_count_by_colors = {}
        for cube_data in cube_subset.split(","):
            cube_number_data, cube_color_data = cube_data.strip().split(" ")
            cube_count_by_colors[cube_color_data] = int(cube_number_data)
        return cube_count_by_colors

    def build_revealed_dice_maximum_count(self):
        revealed_dice_maximum_count = {}
        for cube_subset in self._cube_subsets:
            cube_count_by_colors = self._parse_cube_subset(cube_subset)
            for cube_color, cube_count in cube_count_by_colors.items():
                current_maximum_count_by_color = revealed_dice_maximum_count.get(cube_color, 0)
                if cube_count > current_maximum_count_by_color:
                    revealed_dice_maximum_count[cube_color] = cube_count
        return revealed_dice_maximum_count


class GameValidator:
    VALID_MAXIMUM_DICE_COUNT = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    def __init__(self, input_game_line: str):
        self._game_line_parser = GameLineParser(input_game_line)

    @property
    def game_id(self) -> int:
        return self._game_line_parser.game_id

    def is_game_valid(self) -> bool:
        revealed_dice_maximum_count = self._game_line_parser.build_revealed_dice_maximum_count()
        for cube_color, cube_count in revealed_dice_maximum_count.items():
            maximum_count_for_color = self.VALID_MAXIMUM_DICE_COUNT.get(cube_color)
            if not maximum_count_for_color:
                continue

            if cube_count > maximum_count_for_color:
                return False

        return True


if __name__ == "__main__":
    with open("input.txt") as f:
        game_data = f.read().split("\n")


    game_ids_sum = 0
    for game_line in game_data:
        game_validator = GameValidator(game_line)
        if game_validator.is_game_valid():
            game_ids_sum += game_validator.game_id

    print(game_ids_sum)
