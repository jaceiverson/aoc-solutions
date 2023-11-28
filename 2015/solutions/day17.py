"""https://adventofcode.com/2015/day/17"""

from aoc_util import read

# READ INPUT
data = read("./2015/inputs/17.txt")
# TEST INPUT
data = read("./2015/inputs/17-test.txt").strip().split("\n")
# PARSE INPUT


def subset_sum(numbers, target, partial=None):
    if partial is None:
        partial = []
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print(f"sum({partial})={target}")
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1 :]
        subset_sum(remaining, target, partial + [n])


# PART 1

part_1_answer = subset_sum(data)
print(f"PART 1: {part_1_answer}")

# PART 2

part_2_answer = None
print(f"PART 2: {part_2_answer}")
