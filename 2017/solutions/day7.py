"""https://adventofcode.com/2017/day/7"""


from aoc_util import read
import re

# READ INPUT
data = read("./2017/inputs/7.txt").strip().split("\n")
# TEST INPUT
# data = read("./2017/inputs/7-test.txt").strip().split("\n")
# PARSE INPUT
def part_1(data):
    roots = [x.split(" (")[0] for x in data if "->" in x]
    branches = sum((x.split(" -> ")[1].split(", ") for x in data if "->" in x), [])
    return list(set(roots) - set(branches))[0]


# PART 1
part_1_answer = part_1(data)
print(f"PART 1: {part_1_answer}")

# PART 2

points = {x.split(" (")[0]: int(re.search(r"\((\d*)\)", x).groups()[0]) for x in data}
part_2_answer = None
print(f"PART 2: {part_2_answer}")
