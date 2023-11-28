"""https://adventofcode.com/2020/day/9"""

from aoc_util import read

# READ INPUT
data = read("./2020/inputs/9.txt")
# TEST INPUT
# data = read("./2020/inputs/9-test.txt")
# PARSE INPUT
r = data.strip().split("\n")

# PART 1

# change all to ints
r = [int(x) for x in r]


def check_rule(start, end):
    bin = r[start:end]
    next = r[end]

    for y in bin:
        for z in bin:
            if y < next and z < next and y != z and y + z == next:
                return True

    return False


start = 0
end = 25

for x in range(len(r)):
    if not check_rule(start, end):
        break
    start += 1
    end += 1

r[x]

print(f"PART 1: {part_1_answer}")

# PART 2

print(f"PART 2: {part_2_answer}")
