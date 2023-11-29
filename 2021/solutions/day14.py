"""https://adventofcode.com/2021/day/14"""

from aoc_util import read
from collections import Counter

# READ INPUT
data = read("./2021/inputs/14.txt")
# TEST INPUT
# data = read("./2021/inputs/14-test.txt")
# PARSE INPUT
seed, rules = data.strip().split("\n\n")
seed = list(seed)
rules = rules.split("\n")
rd = {}
for r in rules:
    key, val = r.split(" -> ")
    rd[key] = val


# PART 1
def process_polymer(seed):
    to_insert = []
    # find what you need to insert
    for idx, step in enumerate(seed[:-1]):
        base = seed[idx : idx + 2]
        to_insert.append(rd["".join(base)])

    # insert them backwords
    for insertion in range(len(seed) - 1, 0, -1):
        seed.insert(insertion, to_insert[insertion - 1])

    return seed


# process
counter = 10
while counter != 0:
    seed = process_polymer(seed)
    counter -= 1

c = Counter(seed)
part_1_answer = max(c.values()) - min(c.values())
print(f"PART 1: {part_1_answer}")

# PART 2
# Probably won't work with the brute force method
# Yeah, brute force isn't really the way
seed, rules = data.strip().split("\n\n")
seed = list(seed)
counter = 40
while counter != 0:
    seed = process_polymer(seed)
    counter -= 1

c2 = Counter(seed)
part_2_answer = max(c2.values()) - min(c2.values())
print(f"PART 1: {part_1_answer}")
print(f"PART 2: {part_2_answer}")
