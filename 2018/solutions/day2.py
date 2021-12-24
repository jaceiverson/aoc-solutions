"""https://adventofcode.com/2018/day/2"""

from helper import read
from collections import Counter

# READ INPUT
data = read("./2018/inputs/2.txt")
# TEST INPUT
# data = read("./2018/inputs/2-test.txt")
# PARSE INPUT
data = data.strip().split("\n")
# PART 1
twos = 0
threes = 0
for label in data:
    c = Counter(label)
    if 2 in c.values():
        twos += 1
    if 3 in c.values():
        threes += 1

part_1_answer = twos * threes
print(f"PART 1: {part_1_answer}")

# PART 2
def find_similar(data):
    for label in data:
        for comp_label in data:
            if label != comp_label:
                difference_count = 0
                for idx, letter in enumerate(label):
                    if letter != comp_label[idx]:
                        difference_count += 1
                        difference_index = idx
                    if difference_count > 2:
                        break

                if difference_count == 1:
                    same = label[:difference_index] + label[difference_index + 1 :]
                    return same
    return None


part_2_answer = find_similar(data)
print(f"PART 2: {part_2_answer}")
