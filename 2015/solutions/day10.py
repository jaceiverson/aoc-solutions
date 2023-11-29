"""https://adventofcode.com/2015/day/10"""

from aoc_util import read

# READ INPUT
data = read("./2015/inputs/10.txt").strip()
# TEST INPUT
# data = "1"
# PARSE INPUT


def extract_values(data):
    output = []
    idx = 0
    temp = [data[0]]
    while idx < len(data) - 1:
        if data[idx] == data[idx + 1]:
            temp.append(data[idx + 1])
        else:
            output.append(temp)
            temp = [data[idx + 1]]
        idx += 1

    output.append(temp)
    return output


def get_next_sequence(value: list):
    output = ""
    for number in value:
        output += str(len(number))
        output += str(number[0])
    return output


# PART 1


def iterate_sequence(sequence: str, iterations: int) -> int:
    for _ in range(iterations):
        values = extract_values(sequence)
        sequence = get_next_sequence(values)
    return len(sequence)


part_1_answer = iterate_sequence(data, 40)
print(f"PART 1: {part_1_answer}")

# PART 2

part_2_answer = iterate_sequence(data, 50)
print(f"PART 2: {part_2_answer}")
