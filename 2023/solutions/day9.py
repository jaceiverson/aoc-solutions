"""https://adventofcode.com/2023/day/9"""

from aoc_util import read

# MAIN INPUT
data = read("./2023/inputs/9.txt").strip().split("\n")


# TEST INPUT
# data = read("./2023/inputs/9-test.txt").strip().split("\n")
# EXAMPLE INPUT
# data = read("./2023/inputs/9-test-e.txt").strip().split("\n")
# PARSE INPUT
def find_differences(data: list[int]) -> list[int]:
    return [data[idx_ + 1] - x for idx_, x in enumerate(data[:-1])]


# PART 1
def part_1(data: list):
    sum_ = 0

    # loop over each of the lines
    for line in data:
        # we are going to save the lasts (last value in each row)
        # that is all we need in part 1
        lasts = []
        # extract our data from the string
        current = list(map(int, line.split()))

        # get each of the rows of differences
        while current.count(0) != len(current):
            lasts.append(current[-1])
            current = find_differences(current)

        # go back over each of the lasts and find the next value in the main row
        # current_last = 0
        # for reverse_lasts in lasts[::-1]:
        #     current_last += reverse_lasts
        # add that value to the main sum
        sum_ += sum(lasts)

    return sum_


print(f"PART 1: {part_1(data)}")
# TOO HIGH: 2_012_562_489 | bad rule on checking for reaching 0's didn't account for - numbers


# PART 2
def part_2(data: list):
    sum_ = 0

    # loop over each of the lines
    for line in data:
        # we are going to save the firsts (first value in each row)
        # that is all we need in part 2
        firsts = []
        # extract our data from the string
        current = list(map(int, line.split()))

        # get each of the rows of differences
        while current.count(0) != len(current):
            firsts.append(current[0])
            current = find_differences(current)

        # go back over each of the firsts and find the next value in the main row
        current_first = 0
        for reverse_firsts in firsts[::-1]:
            current_first = reverse_firsts - current_first
        # add that value to the main sum
        sum_ += current_first

    return sum_


print(f"PART 2: {part_2(data)}")
