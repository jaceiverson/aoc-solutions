"""https://adventofcode.com/2015/day/9"""

from helper import read
from itertools import permutations

# READ INPUT
data = read("./2015/inputs/9.txt").strip().split("\n")
# TEST INPUT
# data = read("./2015/inputs/9-test.txt").strip().split("\n")
# PARSE INPUT

# PART 1
locations = set([x.split()[0] for x in data] + [x.split()[2] for x in data])
# total of all distances (not perfect, but it works)
min_distance = sum(map(int, [x.split()[-1] for x in data]))
best_route = None
for r in permutations(locations):
    distance = 0
    for idx, l in enumerate(r[:-1], 1):
        distance += int([x for x in data if l in x and r[idx] in x][0].split()[-1])
    if distance < min_distance:
        min_distance = distance
        best_route = r

part_1_answer = min_distance
print(f"PART 1: {part_1_answer}")

# PART 2
max_distance = 0
best_route = None
for r in permutations(locations):
    distance = 0
    for idx, l in enumerate(r[:-1], 1):
        distance += int([x for x in data if l in x and r[idx] in x][0].split()[-1])
    if distance > max_distance:
        max_distance = distance
        best_route = r
part_2_answer = max_distance
print(f"PART 2: {part_2_answer}")
