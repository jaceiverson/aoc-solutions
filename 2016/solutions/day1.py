"""https://adventofcode.com/2016/day/1"""

from aoc_util import read

# READ INPUT
data = read("./2016/inputs/1.txt").strip().split(", ")
# TEST INPUT
# data = read("./2016/inputs/1-test2.txt").strip().split(", ")
# PARSE INPUT

# PART 1
def part_1(data):
    location = [0, 0]
    current_direction = 0
    directions = ["n", "e", "s", "w"]
    for x in data:
        direction, distance = x[0], x[1:]
        if direction == "R":
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction - 1) % 4

        # move
        if directions[current_direction] == "n":
            location[1] += int(distance)
        elif directions[current_direction] == "e":
            location[0] += int(distance)
        elif directions[current_direction] == "s":
            location[1] -= int(distance)
        elif directions[current_direction] == "w":
            location[0] -= int(distance)

    return sum(abs(x) for x in location)


def check_in_list(locations: list, point: list):
    return point in locations


part_1_answer = part_1(data)
print(f"PART 1: {part_1_answer}")

# PART 2
def part_2(data):
    locations = [[0, 0]]
    current_direction = 0
    directions = ["n", "e", "s", "w"]
    for instruction in data:
        direction, distance = instruction[0], instruction[1:]
        if direction == "R":
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction - 1) % 4

        # move
        new_location = locations[-1].copy()
        if directions[current_direction] == "n":
            new_location[1] += int(distance)
        elif directions[current_direction] == "e":
            new_location[0] += int(distance)
        elif directions[current_direction] == "s":
            new_location[1] -= int(distance)
        elif directions[current_direction] == "w":
            new_location[0] -= int(distance)

        # add each loation we pass
        # this is the locations that move up and down n/s
        if locations[-1][0] == new_location[0]:
            x = new_location[0]
            y_offset = -1 if new_location[1] < locations[-1][1] else 1
            for y in range(
                locations[-1][1] + y_offset, new_location[1] + y_offset, y_offset
            ):
                if check_in_list(locations, [x, y]):
                    locations.append([x, y])
                    return locations
                locations.append([x, y])
        # this is the locations that move side to side e/w
        if locations[-1][1] == new_location[1]:
            y = new_location[1]
            x_offset = -1 if new_location[0] < locations[-1][0] else 1
            for x in range(
                locations[-1][0] + x_offset, new_location[0] + x_offset, x_offset
            ):
                if check_in_list(locations, [x, y]):
                    locations.append([x, y])
                    return locations
                locations.append([x, y])


part_2_locations = part_2(data)
part_2_answer = sum(abs(x) for x in part_2_locations[-1])
print(f"PART 2: {part_2_answer}")
# INCORRECT -> 4
# TO HIGH -> 156
# INCORRECT -> 37
