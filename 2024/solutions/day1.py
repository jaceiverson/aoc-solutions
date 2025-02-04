"""https://adventofcode.com/2024/day/1"""

from aoc_util import read
from rich import print

# MAIN INPUT
data = read("./2024/inputs/1.txt").strip().split("\n")
# TEST INPUT
# data = read("./2024/inputs/1-test.txt").strip().split("\n")


# EXAMPLE INPUT
# data = read("./2024/inputs/1-test-e.txt").strip().split("\n")
# PARSE INPUT
def get_data():
    left = []
    right = []
    for x in data:
        l, r = x.split()
        left.append(l)
        right.append(r)
    return left, right


# PART 1
def part_1():
    l, r = get_data()
    return sum(
        max(int(l1), int(r1)) - min(int(l1), int(r1))
        for l1, r1 in zip(sorted(l), sorted(r))
    )


print(f"PART 1: {part_1()}")


# PART 2
def part_2():
    l, r = get_data()
    # sum the sim scores
    return sum(r.count(l1) * int(l1) for l1 in l)


print(f"PART 2: {part_2()}")
