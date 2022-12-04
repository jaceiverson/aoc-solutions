"""https://adventofcode.com/2022/day/3"""

from helper import read, chunks
from string import ascii_lowercase as lower_a
from string import ascii_uppercase as upper_a

# READ INPUT
data = read("./2022/inputs/3.txt").strip().split("\n")
# TEST INPUT
# data = read("./2022/inputs/3-test.txt")
# PARSE INPUT

# PART 1
v = 0
for x in data:
    a, b = x[: len(x) // 2], x[len(x) // 2 :]
    letter = set(a) & set(b)
    l = list(letter)[0]
    if l in lower_a:
        v += range(26)[lower_a.index(l)] + 1
    else:
        v += range(27, 53)[upper_a.index(l)]
part_1_answer = v
print(f"PART 1: {part_1_answer}")

# PART 2
v = 0
for x in chunks(data, 3):
    a, b, c = x
    l = list(set(a) & set(b) & set(c))[0]
    if l in lower_a:
        v += range(26)[lower_a.index(l)] + 1
    else:
        v += range(27, 53)[upper_a.index(l)]
part_2_answer = v
print(f"PART 2: {part_2_answer}")
