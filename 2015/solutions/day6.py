"""https://adventofcode.com/2015/day/6"""

from aoc_util import read

# READ INPUT
data = read("./2015/inputs/6.txt").strip().split("\n")
# TEST INPUT
# data = ["turn on 499,499 through 500,500", "toggle 0,0 through 999,999"]
# PARSE INPUT


def parse_line(line: str) -> list:
    c1, c2 = line.split(" through ")
    i, c1 = c1.replace("turn ", "").split(" ")
    x1, y1 = map(int, c1.split(","))
    x2, y2 = map(int, c2.split(","))
    return i, x1, y1, x2, y2


def lights(grid: dict, x: int, y: int, action: str):
    if (x, y) not in grid.keys():
        grid[(x, y)] = 0
    if action == "on":
        grid[(x, y)] = 1
    elif action == "off":
        grid[(x, y)] = 0
    elif action == "toggle":
        grid[(x, y)] = 0 if grid[(x, y)] == 1 else 1
    return grid


def bright_lights(grid: dict, x: int, y: int, action: str):
    if (x, y) not in grid.keys():
        grid[(x, y)] = 0
    if action == "on":
        grid[(x, y)] += 1
    elif action == "off":
        grid[(x, y)] = max(0, grid[(x, y)] - 1)
    elif action == "toggle":
        grid[(x, y)] += 2
    return grid


grid = {}


# PART 1 - takes a while
def part_1(grid, data):
    for instruction in data:
        i, x1, y1, x2, y2 = parse_line(instruction)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid = lights(grid, x, y, i)

    return sum(grid.values())


print(f"PART 1: {part_1(data)}")


# PART 2 -> slow
def part_2(grid, data):
    for instruction in data:
        i, x1, y1, x2, y2 = parse_line(instruction)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid = bright_lights(grid, x, y, i)

    return sum(grid.values())


print(f"PART 2: {part_2(grid, data)}")
