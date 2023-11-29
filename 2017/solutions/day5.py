"""https://adventofcode.com/2017/day/5"""

from aoc_util import read

# READ INPUT
data = read("./2017/inputs/5.txt").strip()
# TEST INPUT
# data = read("./2017/inputs/5-test.txt").strip()
# PARSE INPUT
data = list(map(int, data.split("\n")))


# PART 1
def part_1(data):
    position = 0
    steps = 0
    while position < len(data):
        new_position = data[position] + position
        # increment the position
        data[position] += 1
        # go to the new position
        position = new_position
        # increment the steps
        steps += 1
    return steps


part_1_answer = part_1(data.copy())
print(f"PART 1: {part_1_answer}")


# PART 2
def part_2(data):
    position = 0
    steps = 0
    while position < len(data):
        new_position = data[position] + position
        # increment the position
        data[position] += -1 if data[position] >= 3 else 1
        # go to the new position
        position = new_position
        # increment the steps
        steps += 1
    return steps


part_2_answer = part_2(data)
print(f"PART 2: {part_2_answer}")
