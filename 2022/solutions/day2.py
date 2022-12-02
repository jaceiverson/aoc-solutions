"""https://adventofcode.com/2022/day/2"""

from helper import read

# READ INPUT
data = read("./2022/inputs/2.txt").strip().split("\n")
# TEST INPUT
# data = read("./2022/inputs/2-test.txt").strip().split("\n")
# PARSE INPUT

m = {"A": 1, "B": 2, "C": 3, "Y": 1, "X": 2, "Z": 3}
score = {
    "AY": 8,
    "AX": 4,
    "AZ": 3,
    "BY": 5,
    "BX": 1,
    "BZ": 9,
    "CY": 2,
    "CX": 7,
    "CZ": 6,
}
# PART 1
total = 0
for x in data:
    elf, me = x.split()
    total += score[elf + me]


part_1_answer = total
print(f"PART 1: {part_1_answer}")

# PART 2
score = {
    "AY": 4,
    "AX": 3,
    "AZ": 8,
    "BY": 5,
    "BX": 1,
    "BZ": 9,
    "CY": 6,
    "CX": 2,
    "CZ": 7,
}
total = 0
for x in data:
    elf, me = x.split()
    total += score[elf + me]
part_2_answer = total
print(f"PART 2: {part_2_answer}")

# I really like this solution
# https://www.reddit.com/r/adventofcode/comments/zac2v2/comment/iyl7r5n/?utm_source=share&utm_medium=web2x&context=3
