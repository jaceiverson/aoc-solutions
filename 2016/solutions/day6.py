"""https://adventofcode.com/2016/day/6"""

from helper import read

# READ INPUT
data = read("./2016/inputs/6.txt").strip().split("\n")
# TEST INPUT
# data = read("./2016/inputs/6-test.txt").strip().split("\n")
# PARSE INPUT
results = {k: {} for k in range(len(data[0]))}
for line in data:
    for idx, letter in enumerate(line):
        if results[idx].get(letter):
            results[idx][letter] += 1
        else:
            results[idx][letter] = 1

# PART 1
part_1_answer = "".join(
    sorted(results[r].items(), key=lambda x: x[1], reverse=True)[0][0] for r in results
)
print(f"PART 1: {part_1_answer}")

# PART 2
part_2_answer = "".join(
    sorted(results[r].items(), key=lambda x: x[1])[0][0] for r in results
)
print(f"PART 2: {part_2_answer}")
