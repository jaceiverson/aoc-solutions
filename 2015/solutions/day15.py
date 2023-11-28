"""https://adventofcode.com/2015/day/15"""

from itertools import product
from aoc_util import read

# READ INPUT
data = read("./2015/inputs/15.txt").strip().split("\n")
# TEST INPUT
# data = read("./2015/inputs/15-test.txt").strip().split("\n")
# PARSE INPUT
ing = {}
for line in data:
    name, stats = line.split(": ")
    stats = {x.split()[0]: int(x.split()[1]) for x in stats.split(", ")}
    ing[name] = stats


def get_ing_score(ing_list, value) -> int:
    return product(
        max(i * value, 0) for name, i in ing_list.items() if name != "calories"
    )


def get_cookie_score(a, b, c, d):
    properties = []
    for i, values, multiplier in zip(ing.items(), [a, b, c, d]):
        for p, pvalue in values.items():
            pass


# PART 1
max_score = 0
values = None
for a in range(100):
    for b in range(100):
        for c in range(100):
            for d in range(100):
                if a + b + c + d == 100:
                    score = get_cookie_score(a, b, c, d)
                    if score > max_score:
                        max_score = score
                        values = (a, b, c, d)

part_1_answer = None
print(f"PART 1: {part_1_answer}")

# PART 2

part_2_answer = None
print(f"PART 2: {part_2_answer}")
