"""https://adventofcode.com/2019/day/6"""

from aoc_util import read

# READ INPUT
data = read("./2019/inputs/6.txt")
# TEST INPUT
# data = read("./2019/inputs/6-test.txt")
# PARSE INPUT
data = data.strip().split("\n")

# PART 1
# key -> child, val -> parent
planets = {x.split(")")[1]: x.split(")")[0] for x in data}


# find indirects
def orbits(point, map, count=0):
    parent = map.get(point)
    if parent:
        count += 1
        return orbits(parent, map, count)
    return count


orbit_counts = sum(orbits(x, planets) for x in planets)
part_1_answer = orbit_counts
print(f"PART 1: {part_1_answer}")


# PART 2
def path(point, map, path_list=None):
    parent = map.get(point)
    if parent:
        if path_list:
            path_list += [parent]
        else:
            path_list = [point, parent]
        return path(parent, map, path_list)
    return path_list


# first common element
# https://stackoverflow.com/questions/16118621/first-common-element-from-two-lists#16118633
def get_first_common_element(x, y):
    """
    Fetches first element from x that is common for both lists
        or return None if no such an element is found.
    """
    for i in x:
        if i in y:
            return i
    return None


you_path = path("YOU", planets)
san_path = path("SAN", planets)
common_orbit = get_first_common_element(you_path, san_path)
part_2_answer = len(you_path[1 : you_path.index(common_orbit)]) + len(
    san_path[1 : san_path.index(common_orbit)]
)
print(f"PART 2: {part_2_answer}")
