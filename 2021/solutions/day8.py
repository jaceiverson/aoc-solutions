"""https://adventofcode.com/2021/day/8"""

from helper import read

# READ INPUT
data = read("./2021/inputs/8.txt")
# TEST INPUT
data = read("./2021/inputs/8-test.txt")
# PARSE INPUT
data = data.strip().split('\n')
# key -> count of signals
# value -> decimal number
COUNTS = {2:1,4:4,3:7,7:8}
# PART 1
part_1_answer = 0
for row in data:
    temp = row.split(" | ")[1]
    for word in temp.split():
        if len(word) in COUNTS.keys():
            part_1_answer += 1

print(f"PART 1: {part_1_answer}")

# PART 2

print(f"PART 2: {part_2_answer}")
