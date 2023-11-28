"""https://adventofcode.com/2017/day/6"""


from aoc_util import read

# READ INPUT
data = read("./2017/inputs/6.txt").strip()
# TEST INPUT
# data = read("./2017/inputs/6-test.txt").strip()
# PARSE INPUT
data = list(map(int, data.split()))

# PART 1
states = []
steps = 0
while data not in states:
    # add the current data
    states.append(data.copy())
    # find max and index of data
    max_value = max(data)
    starting_point = data.index(max_value)

    data[starting_point] = 0
    for x in range(1, max_value + 1):
        data[(starting_point + x) % len(data)] += 1

    # increment steps
    steps += 1

part_1_answer = steps
print(f"PART 1: {part_1_answer}")

# PART 2
part_2_answer = steps - states.index(data)
print(f"PART 2: {part_2_answer}")
