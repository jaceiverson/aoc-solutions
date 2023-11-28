"""https://adventofcode.com/2016/day/3"""

from aoc_util import read

# READ INPUT
data = read("./2016/inputs/3.txt").strip().split("\n")
# TEST INPUT
# data = read("./2016/inputs/3-test.txt").strip().split("\n")
# PARSE INPUT

# PART 1
def is_triangle(sides: str) -> bool:
    a, b, c = map(int, sides.strip().split())
    return a + b > c and a + c > b and b + c > a


part_1_answer = sum(is_triangle(t) for t in data)
print(f"PART 1: {part_1_answer}")

# PART 2
def part_2(data):
    triangles = 0
    for idx in range(len(data) // 3):
        row1 = data[idx * 3].split()
        row2 = data[idx * 3 + 1].split()
        row3 = data[idx * 3 + 2].split()
        col1 = [row1[0], row2[0], row3[0]]
        col2 = [row1[1], row2[1], row3[1]]
        col3 = [row1[2], row2[2], row3[2]]
        for c in [col1, col2, col3]:
            if t := is_triangle(" ".join(c)):
                triangles += t
    return triangles


part_2_answer = part_2(data)
print(f"PART 2: {part_2_answer}")
