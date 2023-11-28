"""https://adventofcode.com/2019/day/3"""

from aoc_util import read

# READ INPUT
data = read("./2019/inputs/3.txt")
# TEST INPUT
# data = read("./2019/inputs/3-test.txt")
# PARSE INPUT
line_1, line_2 = data.strip().split("\n")
line_1 = line_1.split(",")
line_2 = line_2.split(",")

# PART 1
def get_line_points(p1, p2):
    """given 2 points, returns list of tuples of all points between"""
    p1_x, p1_y = p1
    p2_x, p2_y = p2

    step_direction = 1

    if p1_x == p2_x:
        # returns range of y points

        if p1_y > p2_y:
            # if p1 is > we are going negative, need to step down
            step_direction = -1

        points = [
            (p1_x, y_point)
            for y_point in range(p1_y, p2_y + step_direction, step_direction)
        ]
        # remove first element (we already have that)
        points.pop(0)

    elif p1_y == p2_y:
        # returns range of x points

        if p1_x > p2_x:
            # if p1 is > we are going negative, need to step down
            step_direction = -1

        points = [
            (x_point, p1_y)
            for x_point in range(p1_x, p2_x + step_direction, step_direction)
        ]
        # remove first element (we already have that)
        points.pop(0)

    if points:
        return points

    return None


def get_lines(instructions):
    line_points = [(0, 0)]
    y, x = 0, 0
    for step in instructions:
        direction = step[0]
        distance = int(step[1:])
        if direction == "R":
            x += distance
        elif direction == "L":
            x -= distance
        elif direction == "U":
            y += distance
        elif direction == "D":
            y -= distance
        line_points += get_line_points(line_points[-1], (x, y))
    return line_points


def get_points(instructions):
    line_points = [(0, 0)]
    y, x = 0, 0
    for step in instructions:
        direction = step[0]
        distance = int(step[1:])
        if direction == "R":
            x += distance
        elif direction == "L":
            x -= distance
        elif direction == "U":
            y += distance
        elif direction == "D":
            y -= distance
        line_points.append((x, y))
    return line_points


# get entire lines (all points)
l1 = get_lines(line_1)
l2 = get_lines(line_2)

# sets work to find similarities
same_set = set(l1) & set(l2)
# remove the starting point
same_set.remove((0, 0))

# our answer is the lowest combined sum (abs) of the x,y points
part_1_answer = min(abs(x[0]) + abs(x[1]) for x in same_set)
print(f"PART 1: {part_1_answer}")

# PART 2
# count steps
def count_steps(points, merge_point):
    steps_to_merge = 0
    for step in points[1:]:
        steps_to_merge += 1
        if step == merge_point:
            return steps_to_merge


# we will track each merging point's step count, then find the min (our answer)
step_counts = {}
for point in same_set:
    step_counts[point] = {"L1": count_steps(l1, point), "L2": count_steps(l2, point)}

part_2_answer = min(x["L1"] + x["L2"] for x in step_counts.values())
print(f"PART 2: {part_2_answer}")

# TO HIGH -> 1,180,009
# TO LOW -> 9236 (was I off by one?) no 9237 is still too low
# I was off by 2 because I started my index on 1,
# and was adding +1 after checking if I reached the point
