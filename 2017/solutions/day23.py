"""https://adventofcode.com/2017/day/23"""

from aoc_util import read
from string import ascii_lowercase as alphabet

# READ INPUT
data = read("./2017/inputs/23.txt").strip().split("\n")
# TEST INPUT
# data = read("./2017/inputs/23-test.txt").strip().split("\n")
# PARSE INPUT
R = {letter: 0 for letter in alphabet[:8]}


def get_value(value: str):
    return R[value] if value in alphabet else int(value)


# PART 1
def part_1(data: list[str]):
    position = 0
    mul_count = 0
    while 0 <= position < len(data):
        instruction, register, value = data[position].split()
        if instruction == "set":
            R[register] = get_value(value)
            position += 1
        elif instruction == "sub":
            R[register] -= get_value(value)
            position += 1
        elif instruction == "mul":
            R[register] *= get_value(value)
            mul_count += 1
            position += 1
        elif instruction == "jnz":
            if get_value(register) != 0:
                position += get_value(value) - 1
            position += 1
    return mul_count


part_1_answer = part_1(data)
print(f"PART 1: {part_1_answer}")

# PART 2
# https://www.reddit.com/r/adventofcode/comments/7lms6p/2017_day_23_solutions/
def part_2(data: list[str]):
    position = 0
    passed_positions = []
    while 0 <= position < len(data):
        print(position)
        passed_positions.append(position)
        instruction, register, value = data[position].split()
        if instruction == "set":
            R[register] = get_value(value)
            position += 1
        elif instruction == "sub":
            R[register] -= get_value(value)
            position += 1
        elif instruction == "mul":
            R[register] *= get_value(value)
            position += 1
        elif instruction == "jnz":
            if get_value(register) != 0:
                position += get_value(value) - 1
            position += 1

        if position in passed_positions:
            break

    return R


R = {letter: 0 for letter in alphabet[:8]}
R["a"] = 1
part_2_answer = part_2(data)
print(f"PART 2: {part_2_answer}")
