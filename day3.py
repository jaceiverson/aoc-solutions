"""https://adventofcode.com/2021/day/3"""

from read import read

report = read("./inputs/3.txt")
report = report.strip().split("\n")


def find_totals(report):
    totals = [0] * len(report[0])
    for line in report:
        for idx, digit in enumerate(line):
            totals[idx] += int(digit)
    return totals, len(report) / 2


# PART 1
# keep a list (len of each line) of totals (1s)
# if above half it is the most common bit
totals, half = find_totals(report)

gamma = [x > half for x in totals]
epsilon = [x < half for x in totals]
gamma = "".join([str(x + 0) for x in gamma])
epsilon = "".join([str(x + 0) for x in epsilon])

# answer
power = int(gamma, 2) * int(epsilon, 2)
power

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

life_support = int(oxygen, 2) * int(co2, 2)
life_support

# to high: 4172330 (initial try)
# to low: 3391320 (forgot to return the full tuple (half) was being used from above)
# to low: 3392278 (added equal to set equal to 1)
# 4125600 -> forgot I had switch gamma and epsilon in frustration for testing
# swtiched back and got the right answer
