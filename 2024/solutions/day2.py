"""https://adventofcode.com/2024/day/2"""

from aoc_util import read
from rich import print
from enum import Enum

# MAIN INPUT
data = read("./2024/inputs/2.txt").strip().split("\n")
# TEST INPUT
# data = read("./2024/inputs/2-test.txt").strip().split("\n")
# EXAMPLE INPUT
# data = read("./2024/inputs/2-test-e.txt").strip().split("\n")
# PARSE INPUT


class Status(Enum):
    ASC = 1
    DESC = 0


def is_safe(report: list) -> bool:
    if report != sorted(report) and report != sorted(report)[::-1]:
        return False
    for item_idx, item in enumerate(report):
        if item_idx == len(report) - 1:
            return True
        next_item = report[item_idx + 1]
        if abs(item - next_item) > 3 or item == next_item:
            return False
    return True


# PART 1
def part_1(data: list):
    safe_count = 0
    for level in data:
        safe_count += is_safe(list(map(int, level.split())))
    return safe_count


print(f"PART 1: {part_1(data)}")


def is_safe_2(report: list) -> bool:
    for item_idx, item_to_remove in enumerate(report):
        new_list = report.copy()
        new_list.pop(item_idx)
        result = is_safe(new_list)
        if result:
            return result
    return False


# PART 2
def part_2(data: list):
    safe_count = 0
    for level in data:
        next_check = 0
        # we will see if it is safe normally
        normal_check = is_safe(list(map(int, level.split())))
        if not normal_check:
            # then we will remove each element and see if it is safe
            next_check = is_safe_2(list(map(int, level.split())))

        safe_count += normal_check + next_check
    return safe_count


print(f"PART 2: {part_2(data)}")
