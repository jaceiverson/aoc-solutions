"""https://adventofcode.com/2023/day/7"""

from aoc_util import read

from collections import Counter

# MAIN INPUT
data = read("./2023/inputs/7.txt").strip().split("\n")


# TEST INPUT
# data = read("./2023/inputs/7-test.txt").strip().split("\n")
# EXAMPLE INPUT
# data = read("./2023/inputs/7-test-e.txt").strip().split("\n")
# PARSE INPUT
def trick_value(hand: str) -> int:
    cards = Counter(hand)
    # 5
    if max(cards.values()) == 5:
        return 7
    # 4
    elif max(cards.values()) == 4:
        return 6
    # full house
    elif max(cards.values()) == 3 and len(cards.values()) == 2:
        return 5
    # 3
    elif max(cards.values()) == 3:
        return 4
    # 2 pair
    elif list(cards.values()).count(2) == 2:
        return 3
    # 1 pair
    elif list(cards.values()).count(2) == 1:
        return 2
    else:
        return 1


def trick_value_part_2(hand: str) -> int:
    cards = Counter(hand)
    if no_j_cards := {k: v for k, v in cards.items() if k != "J"}:
        max_value = [k for k, v in no_j_cards.items() if v == max(no_j_cards.values())][
            0
        ]
        no_j_cards[max_value] += cards.get("J", 0)
        cards = no_j_cards

    # 5
    if max(cards.values()) == 5:
        return 7
    # 4
    elif max(cards.values()) == 4:
        return 6
    # full house
    elif max(cards.values()) == 3 and len(cards.values()) == 2:
        return 5
    # 3
    elif max(cards.values()) == 3:
        return 4
    # 2 pair
    elif list(cards.values()).count(2) == 2:
        return 3
    # 1 pair
    elif list(cards.values()).count(2) == 1:
        return 2
    else:
        return 1


def convert_to_number(hand: str):
    letter_map = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    return [int(line) if line.isnumeric() else letter_map[line] for line in hand]


def convert_to_number_part_2(hand: str):
    letter_map = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
    return [int(line) if line.isnumeric() else letter_map[line] for line in hand]


# PART 1
def part_1(data: list):
    clean_data = [
        [
            line.split()[0],
            convert_to_number(line.split()[0]),
            int(line.split()[1]),
            trick_value(line.split()[0]),
        ]
        for line in data
    ]
    clean_data.sort(key=lambda x: (x[3], x[1]), reverse=True)
    return sum(int(bet[2]) * idx for idx, bet in enumerate(clean_data[::-1], 1))


print(f"PART 1: {part_1(data)}")
# TO HIGH: 250944801
# TO HIGH: 249935005
# I needed to fix a bug in the trick value function... opps


# PART 2
def part_2(data: list):
    clean_data = [
        [
            line.split()[0],
            convert_to_number_part_2(line.split()[0]),
            int(line.split()[1]),
            trick_value_part_2(line.split()[0]),
        ]
        for line in data
    ]
    clean_data.sort(key=lambda x: (x[3], x[1]), reverse=True)
    return sum(int(bet[2]) * idx for idx, bet in enumerate(clean_data[::-1], 1))


print(f"PART 2: {part_2(data)}")
