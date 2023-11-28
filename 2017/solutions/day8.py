"""https://adventofcode.com/2017/day/8"""

from aoc_util import read

# READ INPUT
data = read("./2017/inputs/8.txt").strip().split("\n")
# TEST INPUT
# data = read("./2017/inputs/8-test.txt").strip().split("\n")
# PARSE INPUT
R = {}


def opperation(left: int, right: int, o: str):
    if o == "<":
        return left < right
    elif o == ">":
        return left > right
    elif o == "==":
        return left == right
    elif o == "!=":
        return left != right
    elif o == "<=":
        return left <= right
    elif o == ">=":
        return left >= right


def getter(key: str):
    value = R.get(key)
    if value is None:
        R[key] = 0
        return 0
    return value


def part_1(line: str):
    reg, moves, number, _if, reg_to_check, comparison, comparison_value = line.split()
    current_value = getter(reg)
    # check if the condition is met
    if opperation(getter(reg_to_check), int(comparison_value), comparison):
        if moves == "inc":
            R[reg] += int(number)
        else:
            R[reg] -= int(number)
        # print(R)


# PART 1
for l in data:
    part_1(l)
part_1_answer = max(R.values())
print(f"PART 1: {part_1_answer}")

# PART 2
def part_2(data):
    max_value = 0
    for line in data:
        (
            reg,
            moves,
            number,
            _if,
            reg_to_check,
            comparison,
            comparison_value,
        ) = line.split()
        current_value = getter(reg)
        # check if the condition is met
        if opperation(getter(reg_to_check), int(comparison_value), comparison):
            if moves == "inc":
                R[reg] += int(number)
            else:
                R[reg] -= int(number)

            if R[reg] > max_value:
                max_value = R[reg]
        # print(R)
    return max_value


R = {}
part_2_answer = part_2(data)
print(f"PART 2: {part_2_answer}")
# 10494 -> TO HIGH (forgot to clear R)
