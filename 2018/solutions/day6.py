"""https://adventofcode.com/2018/day/6"""

from aoc_util import read
from collections import defaultdict
from string import ascii_letters as alphabet
from rich import print

# READ INPUT
data = read("./2018/inputs/6.txt").split("\n")
# TEST INPUT
# data = read("./2018/inputs/6-test.txt").split("\n")
# PARSE INPUT


def distance_between_points(point_a: str, point_b: str) -> int:
    ax, ay = point_a.split(", ")
    bx, by = point_b.split(", ")
    return abs(int(ax) - int(bx)) + abs(int(ay) - int(by))


def set_up_grid(data):
    max_x = None
    max_y = None
    min_x = None
    min_y = None
    for idx, d in enumerate(data):
        x, y = d.split(", ")
        if not max_x or int(x) > max_x:
            max_x = int(x)
        if not max_y or int(y) > max_y:
            max_y = int(y)
        if not min_x or int(x) < min_x:
            min_x = int(x)
        if not min_y or int(y) < min_y:
            min_y = int(y)

    # create our grid
    row = ["."] * (max_x + min_x + 1)
    grid = [row.copy() for _ in range(max_y + min_y)]

    for idx, d in enumerate(data):
        x, y = map(int, d.split(", "))
        grid[y][x] = idx

    return grid


# PART 1
def part_1(data: list):
    grid = defaultdict(tuple)
    for idx, d in enumerate(data):
        x, y = d.split(", ")
        grid[(int(x), int(y))] = (alphabet[idx], 0)

    bottom_y = max(grid, key=lambda i: i[1])[1]
    top_y = min(grid, key=lambda i: i[1])[1]
    bottom_x = max(grid, key=lambda i: i[0])[0]
    top_x = min(grid, key=lambda i: i[0])[0]

    for x in range(top_x, bottom_x + 1):
        for y in range(top_y, bottom_y + 1):
            # find closest hub
            for idx, h in enumerate(data):
                distance = distance_between_points(f"{x}, {y}", h)
                # if we haven't looked at this point yet, add it in
                if not grid[(x, y)]:
                    grid[(x, y)] = (alphabet[idx], distance)
                # if the points are equal, we need to have it be a .
                # as more than 1 location is closest
                elif distance == grid[(x, y)][1]:
                    grid[(x, y)] = (".", distance)
                # if it is less, this hub becomes the new distance as it is closer
                elif distance < grid[(x, y)][1]:
                    grid[(x, y)] = (alphabet[idx], distance)


# PART 1 Take 2 - Nov 2023
def part_1_take_2(data: list):
    grid = set_up_grid(data)

    class ClosestHub:
        def __init__(self):
            self.hub: str = None
            self.distance: int = None

        def __str__(self):
            return f"{self.hub=} | {self.distance}"

        def __repr__(self):
            return self.__str__()

    # loop through the grid
    for idx, x in enumerate(grid):
        for idy, y in enumerate(x):
            if f"{x}, {y}" not in data:
                # find closest hub
                closest_hub = ClosestHub()

                for hub_id, h in enumerate(data):
                    distance = distance_between_points(f"{idx}, {idy}", h)
                    if closest_hub.hub is None or distance < closest_hub.distance:
                        closest_hub.hub = hub_id
                        closest_hub.distance = distance
                    elif distance == closest_hub.distance:
                        closest_hub.hub = ""

                grid[idx][idy] = f"{closest_hub.hub}."

    grid

    # edges
    edges = {
        y
        for idx, x in enumerate(grid)
        for idy, y in enumerate(x)
        if idx in [0, len(grid) - 1] or idy in [0, len(grid[0]) - 1]
    }

    final_counts = {}
    for x in grid:
        for y in x:
            if f"{x}, {y}" not in data:
                if final_counts.get(y) is None:
                    final_counts[y] = 1
                else:
                    final_counts[y] += 1

    final_counts
    return {k: v for k, v in final_counts.items() if k not in edges}


def is_within_threshold(point, max_distance, data):
    current_sum = 0
    for h in data:
        distance = distance_between_points(point, h)
        current_sum += distance
        if distance >= max_distance:
            return False
    return current_sum < max_distance


def part_2(data):
    grid = set_up_grid(data)
    close_to_all = 0
    for idx, x in enumerate(grid):
        for idy, y in enumerate(x):
            if is_within_threshold(f"{idx}, {idy}", 10000, data):
                grid[idx][idy] = "#"
                close_to_all += 1
    # print(grid)
    return close_to_all


part_1_answer = max(part_1_take_2(data).values())
print(f"PART 1: {part_1_answer}")

# PART 2
part_2_answer = part_2(data)
print(f"PART 2: {part_2_answer}")
