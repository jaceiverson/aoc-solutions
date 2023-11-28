"""https://adventofcode.com/2022/day/13"""

from aoc_util import read

# READ INPUT
data = read("./2022/inputs/13.txt").strip().split("\n\n")
# TEST INPUT
# data = read("./2022/inputs/13-test.txt").strip().split("\n\n")

# PARSE INPUT
def compare(left, right) -> bool:
    for l, r in zip(left, right):
        # integer check
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            elif r < l:
                return False
        else:
            if isinstance(l, list) and isinstance(r, list):
                temp_l, temp_r = l, r
            elif isinstance(l, list) and isinstance(r, int):
                temp_l, temp_r = l, [r]
            elif isinstance(l, int) and isinstance(r, list):
                temp_l, temp_r = [l], r

            inside_compare = compare(temp_l, temp_r)
            if inside_compare is not None:
                return inside_compare

    if len(left) < len(right):
        return True
    elif len(right) < len(left):
        return False


# PART 1
def part_1(data):
    good_values = []
    for idx, values in enumerate(data, 1):
        # print(idx)
        left, right = map(eval, values.split("\n"))
        if compare(left, right):
            good_values.append(idx)
    return sum(good_values)


# print(good_values)
part_1_answer = part_1(data)
print(f"PART 1: {part_1_answer}")
# TO HIGH -> 5778
# I had my recursion messed up. :)
# PART 2


def part_2(data: list, output: bool = False):
    # make the data one list
    temp_data = []
    for value in data:
        left, right = map(eval, value.split("\n"))
        temp_data.extend((left, right))
    temp_data.extend(([[2]], [[6]]))

    if output:
        for x in temp_data:
            print(x)
    # now we need to sort the values
    is_sorted = False
    loops = 0
    while not is_sorted:
        position = 0
        is_sorted = True
        while position < len(temp_data) - 1:
            # compare the first 2 elements
            left, right = temp_data[position], temp_data[position + 1]
            if not compare(left, right):
                is_sorted = False
                temp_data[position], temp_data[position + 1] = right, left

            position += 1

        loops += 1
    if output:
        print(f"{loops=}")
        for x in temp_data:
            print(x)
    return (temp_data.index([[6]]) + 1) * (temp_data.index([[2]]) + 1)


part_2_answer = part_2(data)
print(f"PART 2: {part_2_answer}")
