"""https://adventofcode.com/2024/day/3"""

from aoc_util import read
from rich import print

import re

# MAIN INPUT
data = read("./2024/inputs/3.txt").strip().split("\n")
# TEST INPUT
# data = read("./2024/inputs/3-test.txt").strip().split("\n")
# data = read("./2024/inputs/3-test-b.txt").strip().split("\n")
# EXAMPLE INPUT
# data = read("./2024/inputs/3-test-e.txt").strip().split("\n")
# PARSE INPUT

pattern = r"mul\((\d{1,3},\d{1,3})\)"


# PART 1
def part_1(data: list):
    sum_total = 0
    for line in data:
        groups = re.findall(pattern=pattern, string=line)
        for pair in groups:
            x, y = map(int, pair.split(","))
            sum_total += x * y
    return sum_total


print(f"PART 1: {part_1(data)}")


# PART 2
def part_2(data: list):
    sum_total = 0
    for line_idx, line in enumerate(data):
        active_mul = True
        # correct muls will be at least 8 chars
        # and at most 12
        # so we will look ahead 12 chars
        char_idx = 0
        while char_idx < len(line) - 1:
            char = line[char_idx]
            # do the check for dos and don'ts
            if char == "d":
                if line[char_idx : char_idx + 7] == "don't()":
                    active_mul = False
                    char_idx += 7
                elif line[char_idx : char_idx + 4] == "do()":
                    active_mul = True
                    char_idx += 4

            elif active_mul:
                # then we can check our substring for muls
                sub_string = line[char_idx : char_idx + 13]
                matched_pattern = re.findall(pattern=pattern, string=sub_string)
                if matched_pattern:
                    x, y = map(int, matched_pattern[0].split(","))
                    sum_total += x * y
                    char_idx += len(matched_pattern[0]) + 6
                elif "m" in sub_string:
                    char_idx += max(sub_string.find("m"), 1)
                elif "d" in sub_string:
                    char_idx += max(sub_string.find("d"), 1)
                else:
                    char_idx += 13

            else:
                char_idx += 1

            # print(
            #     f"{active_mul=} | {char_idx=} | {char=} | {line[char_idx : char_idx + 12]} | {len(line)=} | {line_idx=}"
            # )

    return sum_total


def part_2_better(data: list) -> int:
    pattern = r"mul\((\d{1,3},\d{1,3})\)|(do\(\))|(don\'t\(\))"
    sum_total = 0
    for line in data:
        what_we_care_about = re.findall(pattern=pattern, string=line)
        is_active = True
        for entry in what_we_care_about:
            if "do()" == entry[1]:
                is_active = True
            elif "don't()" == entry[2]:
                is_active = False
            elif is_active:
                x, y = map(int, entry[0].split(","))
                sum_total += x * y
    return sum_total


# WRONG: 110,108,861 (high)
# WRONG: 92,057,598 (low)
# WRONG: 96,036,669 (high)
print(f"PART 2: {part_2(data)}")

# WRONG: 94,810,037
print(f"PART 2: {part_2_better(data)}")
