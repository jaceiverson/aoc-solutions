"""https://adventofcode.com/2015/day/13"""

from helper import read
from itertools import permutations

# READ INPUT
data = read("./2015/inputs/13.txt").strip().split("\n")
# TEST INPUT
# data = read("./2015/inputs/13-test.txt").strip().split("\n")
# PARSE INPUT
def get_happiness_score(guests: dict, guest_order: list) -> int:
    happiness = 0
    for idx, person in enumerate(guest_order):
        down_neighbor = guest_order[(idx - 1)]
        up_neighbor = guest_order[((idx + 1) % len(guest_order))]
        happiness += guests[person][down_neighbor]
        happiness += guests[person][up_neighbor]
    return happiness


def build_guest_dict(data):
    guests = {x.split()[0]: {} for x in data}
    for rule in data:
        parsed = rule.split()
        person1 = parsed[0]
        person2 = parsed[-1][:-1]
        sign = parsed[2]
        value = int(parsed[3])
        if sign == "lose":
            value *= -1
        guests[person1].update({person2: value})
    return guests


def permutate(guests) -> int:
    table_order = list(guests.keys())
    max_happiness = 0
    for possible_table_orders in permutations(table_order):
        happiness = get_happiness_score(guests, possible_table_orders)
        if happiness > max_happiness:
            max_happiness = happiness
            max_table_order = possible_table_orders
    return max_happiness


guests = build_guest_dict(data)

# PART 1
part_1_answer = permutate(guests)
print(f"PART 1: {part_1_answer}")
# TO HIGH -> 805 -> had a hard coded modular division... oopps

# PART 2
# ADD MYSELF
for key, value in guests.items():
    guests[key].update({"ME": 0})
guests["ME"] = {key: 0 for key, value in guests.items()}

part_2_answer = permutate(guests)
print(f"PART 2: {part_2_answer}")
