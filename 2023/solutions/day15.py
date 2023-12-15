"""https://adventofcode.com/2023/day/15"""

from aoc_util import read
from rich import print

# MAIN INPUT
data = read("./2023/inputs/15.txt").strip().split(",")


# TEST INPUT
# data = read("./2023/inputs/15-test.txt").strip().split("\n")
# EXAMPLE INPUT
# data = read("./2023/inputs/15-test-e.txt").strip().split(",")
# PARSE INPUT
def find_hash(line: str) -> int:
    hash_ = 0
    for c in line:
        hash_ += ord(c)
        hash_ *= 17
        hash_ = hash_ % 256
    return hash_


# PART 1
def part_1(data: list):
    return sum(find_hash(x) for x in data)


print(f"PART 1: {part_1(data)}")


# PART 2
def part_2(data: list):
    return None


print(f"PART 2: {part_2(data)}")
