"""https://adventofcode.com/2021/day/7"""

from aoc_util import read
import statistics as s

# READ INPUT
data = read("./2021/inputs/7.txt").strip()
# TEST INPUT
data = read("./2021/inputs/7-test.txt").strip()
# PARSE INPUT
data = list(map(int, data.split(",")))

# PART 1
# median solution -> works for the test case ()
m = s.median(data)
fuel = [abs(x - m) for x in data]
part_1_answer = sum(fuel)
print(f"PART 1: {part_1_answer}")

# PART 2
# more expensive each move


# attempt 1 use the mean
"""
1 -> 1
2 -> 3
3 -> 6 
4 -> 10
5 -> 15
6 -> 21
"""
my_min = 100_000_000_000_000
for idx, m in enumerate(range(min(data), max(data))):
    fuel2 = [abs(x - m) for x in data]
    fuel2 = [(x * (x + 1)) / 2 for x in fuel2]
    if sum(fuel2) < my_min:
        my_min = sum(fuel2)
        top_idx = idx

part_2_answer = my_min
print(f"PART 2: {part_2_answer}")

# to high -> 104149135
# 104149135
# 104149091
