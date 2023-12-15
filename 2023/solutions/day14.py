"""https://adventofcode.com/2023/day/14"""

from aoc_util import read
from rich import print
from aoc_util.grid import Grid

# MAIN INPUT
data = read("./2023/inputs/14.txt").strip().split("\n")


# TEST INPUT
# data = read("./2023/inputs/14-test.txt").strip().split("\n")
# EXAMPLE INPUT
# data = read("./2023/inputs/14-test-e.txt").strip().split("\n")
# PARSE INPUT
def get_score(line: list) -> int:
    base = 0
    if "#" in line:
        cube_rocks = [idx for idx, x in enumerate(line) if x == "#"] + [len(line)]
    else:
        cube_rocks = [len(line)]

    total_line_weight = 0
    for segments in cube_rocks:
        temp_line = line[base:segments]
        zeros = temp_line.count("O")
        line_weight = sum(len(line) - base - x for x in range(zeros))
        total_line_weight += line_weight
        base = segments + 1

    # print(total_line_weight)

    return total_line_weight


# PART 1
def part_1(data: list):
    g = Grid(data)
    return sum(get_score(g.get_column(col_idx)) for col_idx in range(g.width))


print(f"PART 1: {part_1(data)}")


# PART 2
def part_2(data: list):
    return None


print(f"PART 2: {part_2(data)}")
