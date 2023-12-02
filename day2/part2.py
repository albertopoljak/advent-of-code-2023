import math

from part1 import GameLineParser


with open("input.txt") as f:
    game_data = f.read().split("\n")


set_power_sum = 0
for game_line in game_data:
    revealed_dice_maximum_count = GameLineParser(game_line).build_revealed_dice_maximum_count()
    set_power_sum += math.prod(revealed_dice_maximum_count.values())


print(set_power_sum)
