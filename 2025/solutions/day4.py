"""https://adventofcode.com/2025/day/4"""

from aoc_util import read
from aoc_util.grid import Grid
from rich import print

# MAIN INPUT
data = read("./2025/inputs/4.txt").strip().split("\n")
# TEST INPUT
# data = read("./2025/inputs/4-test.txt").strip().split("\n")
# EXAMPLE INPUT
# data = read("./2025/inputs/4-test-e.txt").strip().split("\n")
# PARSE INPUT

# PART 1
def part_1(data: list):
    grid = Grid(data)
    # grid.show()
    accessable_points = 0
    for y in range(grid.height):
        for x in range(grid.width):
            point_surroundings = grid.scan_surroundings((x,y))
            if len([i for i in point_surroundings.values() if i=='@'])<4 and grid.get((x,y))=='@':
                # print((x,y))
                # print(point_surroundings)
                accessable_points += 1
    return accessable_points


print(f"PART 1: {part_1(data)}")


# PART 2
def part_2(data: list):

    grid = Grid(data)
    # grid.show()
    accessable_points = 0
    depth = 1
    can_go_deeper_into_paper = True
    while can_go_deeper_into_paper:
        new_grid = Grid(grid.rows)
        accessable_points_grew = False
        for y in range(grid.height):
            for x in range(grid.width):
                point_surroundings = grid.scan_surroundings((x,y))
                if len([i for i in point_surroundings.values() if i=='@'])<4 and grid.get((x,y))=='@':
                    # print((x,y))
                    # print(point_surroundings)
                    accessable_points += 1
                    temp_row = [i for i in new_grid.rows[y]]
                    temp_row[x] = '.'
                    new_grid.rows[y] = ''.join(temp_row)
                    accessable_points_grew = True

        if not accessable_points_grew:
            can_go_deeper_into_paper = False
        depth += 1
        # new_grid.show()
        grid = new_grid

    print(depth)
    return accessable_points


print(f"PART 2: {part_2(data)}")
