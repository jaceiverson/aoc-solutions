"""https://adventofcode.com/2023/day/8"""

from aoc_util import read
import math

# MAIN INPUT
data = read("./2023/inputs/8.txt").strip().split("\n\n")


# TEST INPUT
# data = read("./2023/inputs/8-test.txt").strip().split("\n\n")
# EXAMPLE INPUT
# data = read("./2023/inputs/8-test-e.txt").strip().split("\n\n")
# PARSE INPUT
def parse(data):
    directions, data = data
    map_ = {}
    for line in data.split("\n"):
        k, v = line.split(" = ")
        l, r = v.strip("(").strip(")").split(", ")
        map_[k] = {"r": r, "l": l}

    return directions.lower(), map_


# PART 1
def part_1(order: str, map_: dict):
    current = "AAA"
    count_ = 0
    while current != "ZZZ":
        for step in order:
            current = map_[current][step]
            count_ += 1

    return count_


d, m = parse(data)
# print(f"PART 1: {part_1(d,m)}")


# PART 2
def part_2(order: str, map_: dict):
    current = [x for x in map_ if x[-1] == "A"]
    steps = []
    for c in current:
        count_ = 0
        while c[-1] != "Z":
            # print(current)
            for step in order:
                c = map_[c][step]
                count_ += 1
        steps.append(count_)
    # print(steps)
    return math.lcm(*steps)


# works on the test.txt file, might take a second to run for the main input
print(f"PART 2: {part_2(d,m)}")
# TOO HIGH: 24085386913221873651759779 - product of all the steps in part 2
"""
could find the cycle

see how long it takes each node to reach Z
find the least common multiple of all the values
"""
