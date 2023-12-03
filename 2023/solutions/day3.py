"""https://adventofcode.com/2023/day/3"""

from aoc_util import read
import re
from rich import print

# READ INPUT
data = read("./2023/inputs/3.txt").strip().split("\n")


# TEST INPUT
# data = read("./2023/inputs/3-test.txt").strip().split("\n")
# data = read("./2023/inputs/3-test-b.txt").strip().split("\n")
# PARSE INPUT
def get_next_number_index(line: str, start: int):
    """
    identifies the start of the next numeric value in the line
    """
    for x in line[start:]:
        if x.isnumeric():
            return start
        else:
            start += 1
    return -1


def make_number_map(data: list):
    """
    creates our number map to ID numbers based on x,y coordinates
    """
    map_ = {}
    for line_idx, line in enumerate(data):
        nums = re.findall(r"\d+", line)
        last_idx = 0
        # loop through all the numbers found
        for n in nums:
            # get the index of the number accounting for duplicates
            start_idx = line[last_idx:].index(n) + last_idx
            # save the map
            for i in range(start_idx, len(n) + start_idx):
                map_[(line_idx, i)] = n
            # move the point we are jumping off from
            last_idx = get_next_number_index(line, len(n) + start_idx)

    return map_


# TO BE USED LATER
NUMBER_MAP = make_number_map(data)


def scan_area(x: int, y: int) -> list:
    """
    scans area around symbols to return number coordinates that surround it
    """
    numbers = []
    for x_scan in range(-1, 2):
        for y_scan in range(-1, 2):
            if not x_scan == 0 == y_scan:
                chr = data[x + x_scan][y + y_scan]
                # print(chr)
                if chr.isnumeric():
                    numbers.append((x + x_scan, y + y_scan))
    return numbers


def extract_numbers(nums: list) -> list:
    """
    from a list of number coordinates, find the actual numbers
    return a list of all the numbers (converted to ints)
    """
    cleaned_numbers = []
    last_y = None
    last_x = None
    for n in nums:
        x, y = n
        if x == last_x and y == last_y + 1:
            pass
        else:
            # do work
            cleaned_numbers.append(int(NUMBER_MAP[n]))
        last_x = x
        last_y = y
    return cleaned_numbers


def part_1(data: list):
    sum_ = 0
    for line_idx, line in enumerate(data):
        for idx_, chr in enumerate(line):
            if not chr.isnumeric() and chr != ".":
                numbers = scan_area(line_idx, idx_)
                # print(numbers)
                clean_numbers = extract_numbers(numbers)
                for c in clean_numbers:
                    sum_ += c
    return sum_


# PART 1
part_1_answer = part_1(data)
print(f"PART 1: {part_1_answer}")


# PART 2
def part_2(data: list):
    sum_ = 0
    for line_idx, line in enumerate(data):
        for idx_, chr in enumerate(line):
            if chr == "*":
                numbers = scan_area(line_idx, idx_)
                clean_numbers = extract_numbers(numbers)
                if len(clean_numbers) == 2:
                    sum_ += clean_numbers[0] * clean_numbers[1]
    return sum_


part_2_answer = part_2(data)
print(f"PART 2: {part_2_answer}")
