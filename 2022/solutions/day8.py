"""https://adventofcode.com/2022/day/8"""


from aoc_util import read

# READ INPUT
data = read("./2022/inputs/8.txt").strip().split("\n")
# TEST INPUT
# data = read("./2022/inputs/8-test.txt").strip().split("\n")
# PARSE INPUT
trees = [[int(y) for y in x] for x in data]
trees_seen = (len(trees) * 2 + len(trees[0]) * 2) - 4
# PART 1
for r_idx, row in enumerate(trees):
    for c_idx, value in enumerate(row):
        if r_idx not in [0, len(trees) - 1] and c_idx not in [0, len(row) - 1]:
            col = [x[c_idx] for x in trees]
            # print(row, col, r_idx, c_idx, value)
            # check left to see if you can see this tree
            if all(x < value for x in row[:c_idx]):
                # print("SEE L")
                trees_seen += 1
            # check right
            elif all(x < value for x in row[c_idx + 1 :]):
                # print("SEE R")
                trees_seen += 1
            # check above
            elif all(x < value for x in col[:r_idx]):
                # print("SEE U")
                trees_seen += 1
            # check below
            elif all(x < value for x in col[r_idx + 1 :]):
                # print("SEE D")
                trees_seen += 1


part_1_answer = trees_seen
print(f"PART 1: {part_1_answer}")


# PART 2
def see(sight_line: list, reverse: bool = False):
    if False not in sight_line:
        return len(sight_line)
    if reverse:
        return sight_line[::-1].index(False) + 1
    return sight_line.index(False) + 1


max_ss = 0
max_ss_position = (0, 0)
for r_idx, row in enumerate(trees):
    for c_idx, value in enumerate(row):
        if r_idx not in [0, len(trees) - 1] and c_idx not in [0, len(row) - 1]:
            col = [x[c_idx] for x in trees]
            left = [x < value for x in row[:c_idx]]
            right = [x < value for x in row[c_idx + 1 :]]
            up = [x < value for x in col[:r_idx]]
            down = [x < value for x in col[r_idx + 1 :]]

            temp_ss = see(left, True) * see(right) * see(up, True) * see(down)
            # print(f"{r_idx=},{c_idx=},{temp_ss=}")
            if temp_ss > max_ss:
                max_ss = temp_ss
                max_ss_position = (r_idx, c_idx)


part_2_answer = max_ss
print(f"PART 2: {part_2_answer}")
