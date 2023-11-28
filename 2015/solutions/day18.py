"""https://adventofcode.com/2015/day/18"""

from aoc_util import read

# READ INPUT
data = read("./2015/inputs/18.txt").strip()
# TEST INPUT
# data = read("./2015/inputs/18-test.txt").strip()
# data = read("./2015/inputs/18-test-pt2.txt").strip()
# PARSE INPUT
grid = [list(x) for x in data.split("\n")]


def count_lights(grid) -> int:
    lights = 0
    for r in grid:
        for c in r:
            if c == "#":
                lights += 1
    return lights


def check_neighbors(grid, cell_row, cell_col):
    neighbors_on = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (x == 0 == y):
                n_row = x + cell_row
                n_col = y + cell_col
                if (
                    0 <= n_row < len(grid)
                    and 0 <= n_col < len(grid[0])
                    and grid[n_row][n_col] == "#"
                ):
                    neighbors_on += 1
    return neighbors_on


def generation(grid: list, broken_corners: bool) -> list:
    update_steps = []
    for ridx, row in enumerate(grid):
        update_steps.append([])
        for cidx, cell in enumerate(row):
            # turned on
            if (
                broken_corners
                and ridx in [0, len(grid) - 1]
                and cidx in [0, len(row) - 1]
            ):
                update_steps[ridx].append("#")
            elif cell == "#":
                if check_neighbors(grid, ridx, cidx) in [2, 3]:
                    update_steps[ridx].append(cell)
                else:
                    update_steps[ridx].append(".")
            elif check_neighbors(grid, ridx, cidx) == 3:
                update_steps[ridx].append("#")
            else:
                update_steps[ridx].append(".")

    return update_steps


def many_generations(grid, generation_count: int = 1000, broken_corners: bool = False):
    for _ in range(generation_count):
        grid = generation(grid, broken_corners)
    return grid


# PART 1
part_1_answer = count_lights(many_generations(grid, 100))
print(f"PART 1: {part_1_answer}")

# PART 2
part_2_answer = count_lights(many_generations(grid, 100, True))
print(f"PART 2: {part_2_answer}")
