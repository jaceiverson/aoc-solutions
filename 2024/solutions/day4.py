"""https://adventofcode.com/2024/day/4"""

from aoc_util import read
from rich import print

# MAIN INPUT
# data = read("./2024/inputs/4.txt").strip().split("\n")
# TEST INPUT
data = read("./2024/inputs/4-test.txt").strip().split("\n")
# EXAMPLE INPUT
# data = read("./2024/inputs/4-test-e.txt").strip().split("\n")
# PARSE INPUT

KEYWORD = "XMAS"


# PART 1
def part_1(data: list):
    for row in data:
        for column in row:
            pass


print(f"PART 1: {part_1(data)}")


# PART 2
def part_2(data: list):
    return None


print(f"PART 2: {part_2(data)}")
