"""https://adventofcode.com/2022/day/9"""

from aoc_util import read

# READ INPUT
data = read("./2022/inputs/9.txt").strip().split("\n")
# TEST INPUT
# data = read("./2022/inputs/9-test.txt").strip().split("\n")
# PARSE INPUT


def move_head(step: str, output: bool = False):
    if output:
        print(step)
    direction, distance = step.split()
    if direction == "R":
        return 0, int(distance)
    elif direction == "L":
        return 0, int(distance) * -1
    elif direction == "U":
        return int(distance), 0
    elif direction == "D":
        return int(distance) * -1, 0
    else:
        raise TypeError("BAD DIRECTION")


def move_tail(hx, hy, tx, ty, history: list, append: bool = True):
    _x, _y = abs(hx - tx), abs(hy - ty)
    temp_t_x, temp_t_y = tx, ty
    if _x > 1 or _y > 1:
        # now we need to determine how to move it
        if _x == _y:
            temp_t_x = (hx + tx) / 2
            temp_t_y = (hy + ty) / 2
        elif _x > _y:
            temp_t_y = hy
            temp_t_x = hx - 1 if hx > tx else hx + 1
        elif _y > _x:
            temp_t_x = hx
            temp_t_y = hy - 1 if hy > ty else hy + 1

    if append and (temp_t_x, temp_t_y) not in tail_history:
        history.append((int(temp_t_x), int(temp_t_y)))

    # tx, ty = temp_t_x, temp_t_y
    return int(temp_t_x), int(temp_t_y)


hx, hy = 0, 0
tx, ty = 0, 0

tail_history = []

for s in data:
    # move head
    y, x = move_head(s)
    for _ in range(abs(x)):
        # horizontal movement
        hx += 1 if x > 0 else -1
        # adjust for tail
        tx, ty = move_tail(hx, hy, tx, ty, tail_history)
        # print(f"{hx=},{hy=},{tx=},{ty=}")
    for _ in range(abs(y)):
        # vertical movement
        hy += 1 if y > 0 else -1
        # adjust for tail
        tx, ty = move_tail(hx, hy, tx, ty, tail_history)
        # print(f"{hx=},{hy=},{tx=},{ty=}")

# PART 1

part_1_answer = len(tail_history)
print(f"PART 1: {part_1_answer}")

# PART 2
snake = [[0, 0] for _ in range(10)]
last_node_history = []
for s in data:
    # move head
    y, x = move_head(s)

    for _ in range(abs(x)):
        # horizontal movement
        # move head node
        snake[0][0] += 1 if x > 0 else -1
        # adjust for tail for each element
        for idx, node in enumerate(snake[1:], 1):
            # print(idx)
            snake[idx][0], snake[idx][1] = move_tail(
                snake[idx - 1][0],
                snake[idx - 1][1],
                snake[idx][0],
                snake[idx][1],
                [],
                False,
            )
            if idx == 9 and (snake[9][0], snake[9][1]) not in last_node_history:
                last_node_history.append((snake[9][0], snake[9][1]))
        # print(snake)
    for _ in range(abs(y)):
        # vertical movement
        # move head node
        snake[0][1] += 1 if y > 0 else -1
        # adjust for tail
        for idx, node in enumerate(snake[1:], 1):
            snake[idx][0], snake[idx][1] = move_tail(
                snake[idx - 1][0],
                snake[idx - 1][1],
                snake[idx][0],
                snake[idx][1],
                [],
                False,
            )
        if idx == 9 and (snake[9][0], snake[9][1]) not in last_node_history:
            last_node_history.append((snake[9][0], snake[9][1]))

# print(snake)
part_2_answer = len(last_node_history)
print(f"PART 2: {part_2_answer}")
