"""https://adventofcode.com/2023/day/10"""

from aoc_util import read
from aoc_util.grid import Grid

# MAIN INPUT
data = read("./2023/inputs/10.txt").strip().split("\n")
# TEST INPUT
# data = read("./2023/inputs/10-test.txt").strip().split("\n")
# EXAMPLE INPUT
# data = read("./2023/inputs/10-test-e.txt").strip().split("\n")
# PARSE INPUT
g = Grid(data)
valid_moves_from_center = {
    "J": [(1, 0), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, -1), (-1, 0)],
    "|": [(0, 1), (0, -1)],
    "-": [(1, 0), (-1, 0)],
}


def get_next_position(last: tuple, current: tuple, grid: Grid) -> tuple:
    symbol = grid.get(current)
    came_from = current[0] - last[0], current[1] - last[1]
    next_move = {
        "UP": (current[0], current[1] - 1),
        "DOWN": (current[0], current[1] + 1),
        "LEFT": (current[0] - 1, current[1]),
        "RIGHT": (current[0] + 1, current[1]),
    }
    if came_from == (0, -1):  # from bottom
        if symbol == "7":  # move to the left
            return next_move["LEFT"]
        elif symbol == "F":  # move to the right
            return next_move["RIGHT"]
        elif symbol == "|":  # move up, continue
            return next_move["UP"]
    if came_from == (0, 1):  # from top
        if symbol == "L":  # move to the right
            return next_move["RIGHT"]
        elif symbol == "J":  # move to the left
            return next_move["LEFT"]
        elif symbol == "|":  # move down, continue
            return next_move["DOWN"]
    elif came_from == (-1, 0):  # from right - moving left?
        if symbol == "L":  # move up
            return next_move["UP"]
        elif symbol == "F":  # move down
            return next_move["DOWN"]
        elif symbol == "-":  # move left, continue
            return next_move["LEFT"]
    elif came_from == (1, 0):  # from left - moving right
        if symbol == "J":  # move up
            return next_move["UP"]
        if symbol == "7":  # move down
            return next_move["DOWN"]
        elif symbol == "-":  # move right, continue
            return next_move["RIGHT"]
    else:
        print("BROKEN")


# PART 1
def part_1(data: list):
    g = Grid(data)
    # find starting cell
    start = g.search_grid(lambda x: x == "S")
    start = list([x for x in start][0].keys())[0]

    index_ = 1
    returned_to_start = False
    visited = {start: "S"}
    surr = g.scan_surroundings(start, check_diagnals=False)
    starting_paths = []
    for k, v in surr.items():
        if k in valid_moves_from_center.get(v, []):
            starting_paths.append(k)

    current = starting_paths[0][0] + start[0], starting_paths[0][1] + start[1]
    last = start

    while not returned_to_start:
        # add the current location
        visited[current] = g.get(current)
        # get the next location
        next_ = get_next_position(last, current, g)
        # print(f"Traveling to: {g.get(next_)} @ {next_}")
        if g.get(next_) == "S":
            returned_to_start = True
        last = current
        current = next_
        index_ += 1

    return visited


print(f"PART 1: {len(part_1(data))//2}")


# PART 2
def part_2(data: list):
    loop = part_1(data)
    return None


print(f"PART 2: {part_2(data)}")
