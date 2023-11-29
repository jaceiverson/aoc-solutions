"""https://adventofcode.com/2016/day/7"""

from aoc_util import read
import re

# READ INPUT
data = read("./2016/inputs/7.txt").strip().split("\n")
# TEST INPUT
# data = read("./2016/inputs/7-test.txt").strip().split("\n")
# data = read("./2016/inputs/7-test2.txt").strip().split("\n")

# PARSE INPUT


def check_abba(line: str) -> bool:
    for idx, c in enumerate(line[:-3]):
        if (
            line[idx : idx + 2] == line[idx + 2 : idx + 4][::-1]
            and line[idx] != line[idx + 1]
        ):
            return True


def validate_line_part_1(line: str) -> int:
    inside_brackets = False
    valid_line = False
    for idx, c in enumerate(line[:-3]):
        if c == "[":
            inside_brackets = True
        elif c == "]":
            inside_brackets = False
        if (
            inside_brackets
            and line[idx : idx + 2] == line[idx + 2 : idx + 4][::-1]
            and line[idx] != line[idx + 1]
        ):
            return False
        if (
            line[idx : idx + 2] == line[idx + 2 : idx + 4][::-1]
            and line[idx] != line[idx + 1]
        ):
            valid_line = True

    return valid_line


# PART 1
ip_count = 0
for line in data:
    if validate_line_part_1(line):
        # print(line)
        ip_count += 1


part_1_answer = ip_count
print(f"PART 1: {part_1_answer}")


# PART 2
def validate_line_part_2(line: str) -> bool:
    middle = re.findall(r"\[(.*?)\]", line)
    inside_brackets = False
    for idx, char_ in enumerate(line[:-2]):
        if char_ == "[":
            inside_brackets = True
        elif char_ == "]":
            inside_brackets = False

        if line[idx] == line[idx + 2] != line[idx + 1] and inside_brackets == False:
            # check the center for our inverse
            if any(
                "".join(line[idx + 1] + line[idx] + line[idx + 1]) in middle_section
                for middle_section in middle
            ):
                return True
    return False


ip_count = 0
for line in data:
    if validate_line_part_2(line):
        ip_count += 1

part_2_answer = ip_count
print(f"PART 2: {part_2_answer}")
# 368 -> TO HIGH
# I forgot to make sure I wasn't in the center already. inflated the value
