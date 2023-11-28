"""https://adventofcode.com/2016/day/8"""


import itertools
from aoc_util import read

# READ INPUT
data = read("./2016/inputs/8.txt").strip().split("\n")
# TEST INPUT
# data = read("./2016/inputs/8-test.txt").strip().split("\n")
# PARSE INPUT
# grid is 50 columns and 6 rows
# test grid is 7 columns and 3 rows


def show_grid(grid: list) -> None:
    for x in grid:
        print(x)
    print("\n")


def show_grid_word(grid: list) -> None:
    print("\n".join("".join(str(x) if x == 1 else " " for x in row) for row in grid))


def sum_grid(grid: list) -> None:
    return sum(y for x in grid for y in x)


def make_grid(row: int, col: int) -> list:
    row_object = [0 for _ in range(col)]
    return [row_object.copy() for _ in range(row)]


def make_rectangle(row: int, col: int, grid: list) -> list:
    for r, c in itertools.product(range(row), range(col)):
        grid[r][c] = 1
    return grid


def rotate_row(row: int, offset: int, grid: list) -> list:
    grid[row] = (
        grid[row][-offset % len(grid[row]) :]
        + grid[row][: -offset % len(grid[row])].copy()
    )
    return grid


def rotate_col(col: int, offset: int, grid: list) -> list:
    column_values = [x[col] for x in grid]
    column_values = (
        column_values[-offset % len(column_values) :]
        + column_values[: -offset % len(column_values)]
    )
    for idx, row in enumerate(grid):
        grid[idx][col] = column_values[idx]
    return grid


# PART 1
def test():
    g = make_grid(3, 7)
    make_rectangle(2, 3, g)
    rotate_row(1, -4, g)
    rotate_col(1, 4, g)


grid = make_grid(6, 50)
for instruction in data:
    if "rect" in instruction:
        _, dimensions = instruction.split(" ")
        c, r = map(int, dimensions.split("x"))
        grid = make_rectangle(r, c, grid)
    elif "row" in instruction:
        _rotate, _row, y, _by, offset = instruction.split()
        r = int(y.split("=")[1])
        grid = rotate_row(r, int(offset), grid)
    elif "column" in instruction:
        _rotate, _col, x, _by, offset = instruction.split()
        c = int(x.split("=")[1])
        grid = rotate_col(c, int(offset), grid)

    # show_grid(grid)

part_1_answer = sum_grid(grid)
print(f"PART 1: {part_1_answer}")

# PART 2
# have to read this one with your eyes :) there are some cool ways to parse this,
# but I just looked at the text
part_2_answer = show_grid_word(grid)
# print(f"PART 2: {part_2_answer}")
