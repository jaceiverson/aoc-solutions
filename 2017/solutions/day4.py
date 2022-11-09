"""https://adventofcode.com/2017/day/4"""

from helper import read
from collections import Counter

# READ INPUT
data = read("./2017/inputs/4.txt").strip().split("\n")
# TEST INPUT
# data = ["a ab abc abd abf abj"]
# data = ["abcde xyz ecdab"]
# PARSE INPUT

# PART 1

part_1_answer = sum(all(x == 1 for x in Counter(d.split()).values()) for d in data)
print(f"PART 1: {part_1_answer}")

# PART 2
part_2_answer = sum(
    all(x == 1 for x in Counter(["".join(sorted(x)) for x in d.split()]).values())
    for d in data
)
print(f"PART 2: {part_2_answer}")
