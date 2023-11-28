"""https://adventofcode.com/2021/day/8"""

from typing import final
from aoc_util import read

# READ INPUT
data = read("./2021/inputs/8.txt")
# TEST INPUT
# data = read("./2021/inputs/8-test.txt")
# PARSE INPUT
data = data.strip().split("\n")

# key -> count of signals
# value -> decimal number
COUNTS = {2: 1, 4: 4, 3: 7, 7: 8}
# PART 1
part_1_answer = 0
for row in data:
    temp = row.split(" | ")[1]
    for word in temp.split():
        if len(word) in COUNTS.keys():
            part_1_answer += 1

print(f"PART 1: {part_1_answer}")

# PART 2
"""
LOGIC
0 -> 6 # does not contain 4
1 -> 2 # unique
2 -> 5 # 
3 -> 5 # contains 1
4 -> 4 # unique
5 -> 5 # 
6 -> 6 # does not contain 1
7 -> 3 # unique
8 -> 7 # unique (all)
9 -> 6 # contains 4 exactly
"""
L = ["a", "b", "c", "d", "e", "f", "g"]


def get_difference(one, two):
    return list((set(one) - set(two)))


def find_solutions(nums):
    solutions = {}
    # get the unique ones out of the way
    for key in nums:
        # EASY ONES
        if len(key) == 2:
            solutions[1] = key
        elif len(key) == 3:
            solutions[7] = key
        elif len(key) == 4:
            solutions[4] = key
        elif len(key) == 7:
            solutions[8] = key

    # remove those elements we found
    nums = [x for x in nums if x not in solutions.values()]

    # now solve for the harder ones
    for key in nums:
        # 6 lights 0,6,9
        if len(key) == 6:
            if set(solutions[4]).issubset(key):
                solutions[9] = key
            elif set(solutions[1]).issubset(key):
                solutions[0] = key
            else:
                solutions[6] = key

    # remove those elements
    nums = [x for x in nums if x not in solutions.values()]

    for key in nums:
        # 5 lights 2,3,5
        # i need to know 6 for this
        if len(key) == 5:
            if set(solutions[1]).issubset(key):
                solutions[3] = key
            elif set(key).issubset(solutions[6]):
                solutions[5] = key
            else:
                solutions[2] = key

    return solutions


def find_positions(solutions):
    positions = {key: None for key in L}
    # find f & c's positions with 1 & 5
    if solutions[1][0] in solutions[5]:
        positions["f"] = solutions[1][0]
        positions["c"] = solutions[1][1]
    else:
        positions["f"] = solutions[1][1]
        positions["c"] = solutions[1][0]
    # find a's position of 7
    positions["a"] = get_difference(solutions[7], solutions[1])[0]
    # find d & g's from 3 compared to 4
    dee_gee = get_difference(solutions[3], solutions[7])
    if dee_gee[0] in solutions[4]:
        positions["d"] = dee_gee[0]
        positions["g"] = dee_gee[1]
    else:
        positions["d"] = dee_gee[1]
        positions["g"] = dee_gee[0]
    # find b & e's from 8 compared to 3
    bee_eee = get_difference(solutions[8], solutions[3])
    if bee_eee[0] in solutions[5]:
        positions["b"] = bee_eee[0]
        positions["e"] = bee_eee[1]
    else:
        positions["b"] = bee_eee[1]
        positions["e"] = bee_eee[0]

    return positions


CODE_NUMS = []
for row in data:
    # separate the input vs the code
    nums, code = row.split(" | ")
    nums = nums.split()
    code = code.split()

    # go through the process of determining which letters are which
    s = find_solutions(nums)
    s2 = {"".join(sorted(value)): key for key, value in s.items()}
    p = find_positions(s)
    p2 = {value: key for key, value in p.items()}
    final_num = [s2["".join(sorted(c.translate(p2)))] for c in code]
    CODE_NUMS.append("".join(str(x) for x in final_num))

part_2_answer = sum(int(x) for x in CODE_NUMS)
print(f"PART 2: {part_2_answer}")
