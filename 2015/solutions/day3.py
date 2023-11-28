"""https://adventofcode.com/2015/day/3"""


from aoc_util import read

# READ INPUT
data = read("./2015/inputs/3.txt").strip()
# TEST INPUT
# data = read("./2015/inputs/3-test.txt")
# PARSE INPUT


def increment(house):
    if house == "<":
        return -1, 0
    elif house == ">":
        return 1, 0
    elif house == "^":
        return 0, 1
    elif house == "v":
        return 0, -1


def update_house_map(house_map, x, y):
    # check if the key is in the dictionary
    if (x, y) in house_map:
        house_map[(x, y)] += 1
    else:
        house_map[(x, y)] = 1
    return house_map


# PART 1
house_map = {(0, 0): 1}
x, y = 0, 0
for house in data:
    temp_x, temp_y = increment(house)
    x += temp_x
    y += temp_y
    house_map = update_house_map(house_map, x, y)

part_1_answer = len(house_map)
print(f"PART 1: {part_1_answer}")

# PART 2
house_map = {(0, 0): 2}
# santa's position
x, y = 0, 0
# robo-santa's position
x_b, y_b = 0, 0
for idx, house in enumerate(data):
    temp_x, temp_y = increment(house)
    if idx % 2 == 0:
        x += temp_x
        y += temp_y
        house_map = update_house_map(house_map, x, y)
    else:
        x_b += temp_x
        y_b += temp_y
        house_map = update_house_map(house_map, x_b, y_b)

part_2_answer = len(house_map)
print(f"PART 2: {part_2_answer}")
