"""https://adventofcode.com/2015/day/2"""

from helper import read

# READ INPUT
data = read("./2015/inputs/2.txt").strip().split("\n")
# TEST INPUT
# data = read("./2015/inputs/2-test.txt")
# PARSE INPUT
def determine_wrapping_paper(dimensions):
    l, w, h = map(int, dimensions.split("x"))
    dims = [l, w, h]
    dims.remove(max(l, w, h))
    return 2 * l * w + 2 * l * h + 2 * w * h + (dims[0] * dims[1])


def determine_ribbon_size(dimensions):
    l, w, h = map(int, dimensions.split("x"))
    dims = [l, w, h]
    dims.remove(max(l, w, h))
    return l * w * h + 2 * dims[0] + 2 * dims[1]


# PART 1
part_1_answer = sum(determine_wrapping_paper(x) for x in data)
print(f"PART 1: {part_1_answer}")

# PART 2
part_2_answer = sum(determine_ribbon_size(x) for x in data)
print(f"PART 2: {part_2_answer}")
