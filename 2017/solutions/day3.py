"""https://adventofcode.com/2017/day/3"""

from aoc_util import read
from math import sqrt, ceil

# READ INPUT
data = read("./2017/inputs/3.txt").strip()
# TEST INPUT
# data = read("./2017/inputs/3-test.txt")
# PARSE INPUT
grid = """
37  36  35  34  33  32  31
38  17  16  15  14  13  30
39  18   5   4   3  12  29
40  19   6   1   2  11  28
41  20   7   8   9  10  27
42  21  22  23  24  25  26
43  44  45  46  47  48  49
"""


# bottom right corner is odd numbers squared (1*1,3*3,5*5, ->)
def find_distance(n: int):
    base = ceil(sqrt(n))
    base = base if base % 2 != 0 else base + 1
    brc = base * base
    blc = brc - (base - 1)
    tlc = blc - (base - 1)
    trc = tlc - (base - 1)

    distance = 0
    if n >= blc:
        distance = abs(abs(brc - n) - base // 2)
    elif n >= tlc:
        distance = abs(abs(blc - n) - base // 2)
    elif n >= trc:
        distance = abs(abs(tlc - n) - base // 2)
    else:
        distance = abs(abs(trc - n) - base // 2)

    return distance + base // 2


# PART 1
part_1_answer = find_distance(int(data))
print(f"PART 1: {part_1_answer}")

# PART 2
grid = """
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
"""
"""
1 2 3 2 3 2 4 3 2 4 3 2 4 4 3 2 4 4 3 2 4 4 4 3 2 4 4 4 3 2 4 4 4 4 3 
"""


def sum_surrounding(cell, grid) -> int:
    total = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x != 0 and y != 0:
                total += grid


part_2_answer = None
print(f"PART 2: {part_2_answer}")
