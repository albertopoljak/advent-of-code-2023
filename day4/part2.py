from collections import defaultdict


with open("input.txt") as f:
    data = f.read().split("\n")


 # Simple dict where key is card index and value is number of cards
card_count = defaultdict(int)
for card_index, line in enumerate(data):
    card_number = card_index + 1  # for easier visualization
    card_count[card_number] += 1

    _, all_numbers = line.split(":")
    winning_numbers, current_numbers = all_numbers.split("|")
    winning_numbers = set(map(int, winning_numbers.split()))
    current_numbers = set(map(int, current_numbers.split()))
    matching_number_count = len(current_numbers.intersection(winning_numbers))

    for card_copy_addition_index in range(matching_number_count):
        card_count[card_number + card_copy_addition_index + 1] += 1 * card_count.get(card_number, 1)


print(sum(card_count.values()))
