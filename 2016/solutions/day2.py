"""https://adventofcode.com/2016/day/2"""

from aoc_util import read

# READ INPUT
data = read("./2016/inputs/2.txt").strip().split("\n")
# TEST INPUT
# data = read("./2016/inputs/2-test.txt").strip().split("\n")
# PARSE INPUT
KEYPAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
KEYPAD_2 = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None],
]


# PART 1
def parse_code(code_list: list, position: list, keypad: list):
    CODE = ""
    for instruction in code_list:
        for letter in instruction:
            if letter in ["U", "D"]:
                if letter == "U":
                    temp_0 = max(position[0] - 1, 0)
                elif letter == "D":
                    temp_0 = min(position[0] + 1, len(keypad) - 1)
                if keypad[temp_0][position[1]] is not None:
                    position[0] = temp_0
            if letter in ["L", "R"]:
                if letter == "L":
                    temp_1 = max(position[1] - 1, 0)
                elif letter == "R":
                    temp_1 = min(position[1] + 1, len(keypad[position[1]]) - 1)
                if keypad[position[0]][temp_1] is not None:
                    position[1] = temp_1

        x, y = position
        CODE += str(keypad[x][y])
    return CODE


starting_position = [1, 1]
part_1_answer = parse_code(data, starting_position, KEYPAD)
print(f"PART 1: {part_1_answer}")

# PART 2
part_2_start = [2, 0]
part_2_answer = parse_code(data, part_2_start, KEYPAD_2)
print(f"PART 2: {part_2_answer}")
