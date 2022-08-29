"""https://adventofcode.com/2021/day/12"""

from helper import read
from dataclasses import dataclass

# READ INPUT
data = read("./2021/inputs/12.txt")
# TEST INPUT
data = read("./2021/inputs/12-test.txt")
# PARSE INPUT
data = data.strip().split("\n")

NODES = {}


@dataclass
class PathPoint:
    name: str
    next: list
    big: bool
    past: list = None
    visited: bool = False
    is_start: bool = False
    is_end: bool = False


for node in data:
    start = node.split("-")[0]
    end = node.split("-")[1]
    is_big_cave = (len(start) == 1) and (not start.islower())
    is_start = start == "start"
    is_end = end == "end"

C = {}
for node in data:
    start = node.split("-")[0]
    end = node.split("-")[1]
    if C.get(start):
        C[start].append(end)
    else:
        C[start] = [end]

"""
LOGIC

if starting cave is capital, going to a lower cave is one way
if the lower cave has no children, cannot path that way

leave from start, finish with end

"""


def path(path_options, current_path):
    current_cave = current_path[-1]
    # get rid of lower case already in path
    current_options = [
        x
        for x in path_options[current_cave]
        if x.lower not in current_path and "end" not in current_path
    ]

    for selection in current_options:
        current_path.append(selection)
        if selection in path_options:
            path(path_options, current_path)

    return current_path


p = path(C, ["start"])

# PART 1

print(f"PART 1: {part_1_answer}")

# PART 2

print(f"PART 2: {part_2_answer}")
