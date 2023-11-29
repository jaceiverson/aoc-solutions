"""https://adventofcode.com/2015/day/1"""

from aoc_util import read

# READ INPUT
data = read("./2015/inputs/1.txt")
# TEST INPUT
# data = read("./2015/inputs/1-test.txt")
# PARSE INPUT


# PART 1
def part_1(data):
    while True:
        start_len = len(data)
        data = data.replace("()", "")
        if len(data) == start_len:
            return data


cleaned_data = part_1(data)
part_1_answer = cleaned_data.count("(") - cleaned_data.count(")")
print(f"PART 1: {part_1_answer}")


# PART 2
def part_2(data):
    up_count = 0
    for idx, x in enumerate(data):
        if x == "(":
            up_count += 1
        else:
            up_count -= 1
        # if our up_count is less than 0, we enter the basement
        if up_count < 0:
            return idx + 1


part_2_answer = part_2(data)
print(f"PART 2: {part_2_answer}")
# TO LOW -> 1782
# they consider the positions starting at 1 not starting at 0
