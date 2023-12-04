with open("input.txt") as f:
    data = f.read().split("\n")


points = 0
for line in data:
    _, all_numbers = line.split(":")
    winning_numbers, current_numbers = all_numbers.split("|")
    winning_numbers = set(map(int, winning_numbers.split()))
    current_numbers = set(map(int, current_numbers.split()))
    win_count = len(current_numbers.intersection(winning_numbers))
    if win_count > 0:
        points += 2 ** (win_count - 1)


print(points)
