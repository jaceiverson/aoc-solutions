"""https://adventofcode.com/2022/day/5"""

from helper import read

# READ INPUT
data = read("./2022/inputs/5.txt").split("\n\n")
# TEST INPUT
# data = read("./2022/inputs/5-test.txt").split("\n\n")
# PARSE INPUT
stacks, instructions = data


def set_value(key, value, obj) -> dict:
    if obj.get(key):
        obj[key].append(value)
    else:
        obj[key] = [value]
    return obj


def get_start(cols: int = 9):
    s = {}
    for row in stacks.split("\n")[:-1]:
        for col in range(cols):
            if row[(col * 4) + 1].isalpha():
                s = set_value(col + 1, row[(col * 4) + 1], s)
    return s


def part_1(instructions):
    s = get_start()
    for i in instructions.strip().split("\n"):
        _, qty, _, location, _, destination = i.split()
        for _ in range(1, int(qty) + 1):
            s[int(destination)].insert(0, s[int(location)].pop(0))
    return s


def part_2(instructions):
    s = get_start()
    for i in instructions.strip().split("\n"):
        _, qty, _, location, _, destination = i.split()
        to_move = s[int(location)][: int(qty)].copy()
        for x in to_move:
            s[int(location)].remove(x)
        s[int(destination)] = to_move + s[int(destination)]
    return s


# PART 1
s = part_1(instructions)
part_1_answer = "".join(x[1][0] for x in sorted(s.items(), key=lambda x: x[0]))
print(f"PART 1: {part_1_answer}")


# PART 2
s2 = part_2(instructions)
part_2_answer = "".join(x[1][0] for x in sorted(s2.items(), key=lambda x: x[0]))
print(f"PART 2: {part_2_answer}")

# pretty happy this one took me just 22 minutes for both parts
