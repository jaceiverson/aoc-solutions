"""https://adventofcode.com/2017/day/2"""

from aoc_util import read

# READ INPUT
data = read("./2017/inputs/2.txt").strip().split("\n")
# TEST INPUT
# data = read("./2017/inputs/2-test.txt").strip().split("\n")
# PARSE INPUT

# PART 1
checksum = []
for row in data:
    r = list(map(int, row.split()))
    checksum.append(max(r) - min(r))

part_1_answer = sum(checksum)
print(f"PART 1: {part_1_answer}")


# PART 2
def find_divisible(row: list) -> int:
    for x in r:
        for y in r:
            if x != y:
                result = max(x, y) / min(x, y)
                if result.is_integer():
                    return result
    return None


checksum = []
for row in data:
    r = list(map(int, row.split()))
    checksum.append(find_divisible(r))


part_2_answer = sum(checksum)
print(f"PART 2: {part_2_answer}")
