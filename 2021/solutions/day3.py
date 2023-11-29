"""https://adventofcode.com/2021/day/3"""

from aoc_util import read

report = read("./inputs/3.txt")
report = report.strip().split("\n")


def find_totals(report):
    # make list to house totals in each position
    # we will start with everything as 0
    # this list will tell us how many 1's there are in the input
    # then we can determine 0's from row_count - 1's
    totals = [0] * len(report[0])
    # each line in the input
    for line in report:
        # each digit in the line
        for idx, digit in enumerate(line):
            # we can just add the value at each position to calculate the totals
            totals[idx] += int(digit)
    # return the total list as well as half (to use to determine which is majority)
    return totals, len(report) / 2


# PART 1
# keep a list (len of each line) of totals (1s)
# if above half it is the most common bit
totals, half = find_totals(report)
# most common bit
gamma = [x > half for x in totals]
# least common bit
epsilon = [x < half for x in totals]
# make each into a binary number
gamma = "".join([str(x + 0) for x in gamma])
epsilon = "".join([str(x + 0) for x in epsilon])

# answer for power
# convert gamma & epsilon from binary to ints
part_1_answer = int(gamma, 2) * int(epsilon, 2)
print(f"PART 1: {part_1_answer}")


# PART 2
def filter(key, position, stack, above_half):
    # create the sub_stack
    sub_stack = [x for x in stack if x[position] == key[position]]
    # if there is one left, return
    if len(sub_stack) == 1:
        return sub_stack[0]
    # if not, we need to generate a new key
    totals, half = find_totals(sub_stack)
    if above_half:
        key = [x >= half for x in totals]
        key = "".join([str(x + 0) for x in key])
    else:
        key = [x < half for x in totals]
        key = "".join([str(x + 0) for x in key])

    print(key, totals)
    return filter(key, position + 1, sub_stack, above_half)


oxygen = filter(gamma, 0, report, True)
co2 = filter(epsilon, 0, report, False)

# answer for life support
part_2_answer = int(oxygen, 2) * int(co2, 2)
print(f"PART 2: {part_2_answer}")

# to high: 4172330 (initial try)
# to low: 3391320 (forgot to return the full tuple (half) was being used from above)
# to low: 3392278 (added equal to set equal to 1)
# 4125600 -> forgot I had switch gamma and epsilon in frustration for testing
# swtiched back and got the right answer
