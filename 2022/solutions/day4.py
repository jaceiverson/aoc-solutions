"""https://adventofcode.com/2022/day/4"""

from aoc_util import read

# READ INPUT
data = read("./2022/inputs/4.txt").strip().split("\n")
# TEST INPUT
# data = read("./2022/inputs/4-test.txt").strip().split("\n")
# PARSE INPUT

# PART 1
contains = 0
for x in data:
    a, b = x.split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    # if a is inside b or b is inside a
    if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
        contains += 1
        # print(a, b)

part_1_answer = contains
print(f"PART 1: {part_1_answer}")
# 598 not it
# PART 2

contains = 0
for x in data:
    a, b = x.split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))
    # if a is inside b or b is inside a
    b_ = set(range(b1, b2 + 1))
    a_ = set(range(a1, a2 + 1))
    if a_ & b_:
        contains += 1
        # print(a, b)

part_2_answer = contains
print(f"PART 2: {part_2_answer}")
