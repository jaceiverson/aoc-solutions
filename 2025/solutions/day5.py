"""https://adventofcode.com/2025/day/5"""

from aoc_util import read
from rich import print

# MAIN INPUT
# data = read("./2025/inputs/5.txt").strip().split("\n\n")
# TEST INPUT
data = read("./2025/inputs/5-test.txt").strip().split("\n\n")
# EXAMPLE INPUT
# data = read("./2025/inputs/5-test-e.txt").strip().split("\n")
# PARSE INPUT

def consolidate_fresh_range(fresh_ranges:list) -> list[tuple]:
    # WIP
    new_ranges = []
    for r in fresh_ranges:
        start_point, end_point = map(int,r.split('-'))
        for r2 in new_ranges:
            r2s,r2e = r2
            if (r2e > start_point > r2s and end_point > r2e) or (start_point < r2s and r2s < end_point < r2e):
                new_sp = min(start_point,r2s)
                new_ep = max(end_point,r2e)
# PART 1
def part_1(data: list):
    fresh_range, ing = data[0].split("\n"), data[1].split("\n")
    print(fresh_range)
    return None


print(f"PART 1: {part_1(data)}")


# PART 2
def part_2(data: list):
    return None


print(f"PART 2: {part_2(data)}")
