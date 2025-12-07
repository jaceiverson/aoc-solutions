"""https://adventofcode.com/2025/day/3"""

from aoc_util import read
from rich import print

# MAIN INPUT
data = read("./2025/inputs/3.txt").strip().split("\n")
# TEST INPUT
# data = read("./2025/inputs/3-test.txt").strip().split("\n")
# EXAMPLE INPUT
# data = read("./2025/inputs/3-test-e.txt").strip().split("\n")
# PARSE INPUT


# PART 1
def part_1(data: list):
    # biggest_pairs = {}
    running_total = 0
    for line_pos, line in enumerate(data):
        line_length = len(line)
        biggest = None
        second = None
        for position, num in enumerate(line,1):
            if biggest is None or (int(num) > biggest and position < line_length):
                # reset to second  to None so we look ahead only
                second = None
                # reset biggest to current number
                biggest = int(num)
            elif second is None:
                second = int(num)
            elif int(num) > second:
                # reset second to current number
                second = int(num)
        line_value = int(f"{biggest}{second}")
        # biggest_pairs[line_pos] = line_value
        running_total += line_value
    # print(biggest_pairs)
    # print(sum(biggest_pairs.values()))
    # print(running_total)
    return running_total
# 17004 - TOO LOW
# 17141 - TOO LOW (changed first if to be only < and not <=)
# GOT it. Forgot to change the line comparison

print(f"PART 1: {part_1(data)}")


# PART 2
def part_2(data: list):
    # IDEA
    # 1 Find all of the biggest digits? Then track around them?
    # 2 Start from the largest number in the sequence and move right, unless < 12 spaces left
    return None


print(f"PART 2: {part_2(data)}")
