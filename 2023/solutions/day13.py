"""https://adventofcode.com/2023/day/13"""

from aoc_util import read
from aoc_util.grid import Grid
from rich import print

# MAIN INPUT
data = read("./2023/inputs/13.txt").strip().split("\n\n")
# TEST INPUT
# data = read("./2023/inputs/13-test.txt").strip().split("\n\n")
# EXAMPLE INPUT
data = read("./2023/inputs/13-test-e.txt").strip().split("\n\n")
# PARSE INPUT


def scan_outword(lines: list, lower_idx: int, upper_idx: int):
    if lower_idx - 1 < 0 or upper_idx + 1 > len(lines) - 1:
        return True
    if lines[lower_idx - 1] == lines[upper_idx + 1]:
        return scan_outword(lines, lower_idx - 1, upper_idx + 1)
    else:
        return False


def find_reflection_point(g: Grid):
    # check rows
    for r_idx, row in enumerate(g.rows[:-1]):
        if row == g.rows[r_idx + 1]:
            if scan_outword(g.rows, r_idx, r_idx + 1):
                return (r_idx + 1) * 100
    # check columns
    for c_idx in range(g.width - 1):
        if g.get_column(c_idx) == g.get_column(c_idx + 1):
            if scan_outword(
                [g.get_column(c) for c in range(g.width)], c_idx, c_idx + 1
            ):
                return c_idx + 1

    return 0


# PART 1
def part_1(data: list):
    grids = [Grid(x.split("\n")) for x in data]
    return sum(find_reflection_point(g) for g in grids)


print(f"PART 1: {part_1(data)}")
# TOO LOW - I am getting a lot of broken reflections, something is off

# PART 2
SWITCHEROO = {"#": ".", ".": "#"}


def part_2_work(g: Grid):
    for row_idx, row in enumerate(g.rows):
        for char_idx, char in enumerate(row):
            # switch one character at at time
            temp_row = list(row)
            temp_row[char_idx] = SWITCHEROO[char]
            g.rows[row_idx] = "".join(temp_row)

            # look for reflection point
            if value := find_reflection_point(g) > 0:
                return value

            # change it back if there isn't one
            g.rows[row_idx] = row


def part_2(data: list):
    grids = [Grid(x.split("\n")) for x in data]
    return sum(part_2_work(g) for g in grids)


print(f"PART 2: {part_2(data)}")
