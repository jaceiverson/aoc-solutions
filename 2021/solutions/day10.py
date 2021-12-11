"""https://adventofcode.com/2021/day/10"""

from helper import read
from statistics import median

# READ INPUT
data = read("./2021/inputs/10.txt")
# TEST INPUT
# data = read("./2021/inputs/10-test.txt")
# PARSE INPUT
data = data.strip().split("\n")

POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETION_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}
CHUNKS = {"(": ")", "[": "]", "{": "}", "<": ">"}
OPEN = ["(", "[", "{", "<"]
CLOSE = [")", "]", "}", ">"]

errors = {}
auto_complete = {}
for idx, row in enumerate(data):
    input = []
    incomplete = True
    for c_idx, col in enumerate(row):
        if col in OPEN:
            input.append(col)
        elif col in CLOSE:
            # make sure it was a valid close
            # if the index of this value, and the most recent open
            # are the same, it is a valid close
            if CLOSE.index(col) == OPEN.index(input[-1]):
                # remove that as it as found its close
                input.pop()
            else:
                errors[idx] = {
                    "ROW": row,
                    "INDEX": c_idx,
                    "ERROR": f"Expected {CLOSE[OPEN.index(input[-1])]}, found {col}",
                    "SCORE": POINTS[col],
                }
                incomplete = False
                # get out of the internal loop (row is corrupt)
                break
    if incomplete:
        auto_complete[idx] = [CHUNKS[x] for x in input[::-1]]
"""
for key,value in errors.items():
    print(f"{key=}:{value=}")
"""
part_1_answer = sum(errors[x]["SCORE"] for x in errors)
print(f"PART 1: {part_1_answer}")

# GET AUTO COMPLETE
scores = []
for row, chars in auto_complete.items():
    row_score = 0
    for c in chars:
        row_score = row_score * 5
        row_score += COMPLETION_POINTS[c]
    scores.append(row_score)

part_2_answer = median(scores)
print(f"PART 2: {part_2_answer}")
