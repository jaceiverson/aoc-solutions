"""https://adventofcode.com/2022/day/10"""


from helper import read

# READ INPUT
data = read("./2022/inputs/10.txt").strip().split("\n")
# TEST INPUT
data = read("./2022/inputs/10-test.txt").strip().split("\n")
# PARSE INPUT

# PART 1
SIGNALS = (20, 60, 100, 140, 180, 220)
values = {}
cycles = 0
_x_ = 1
for step in data:
    temp_x = 0
    if "addx" in step:
        cycles += 1
        temp_x = int(step.split()[1])

    # before ending the cycle, check to see if it is an important one
    if cycles in SIGNALS and not values.get(cycles):
        values[cycles] = cycles * _x_

    cycles += 1

    # before ending the cycle, check to see if it is an important one
    if cycles in SIGNALS and not values.get(cycles):
        values[cycles] = cycles * _x_

    _x_ += temp_x
    # print(f"{cycles=},{temp_x=},{_x_=}")

part_1_answer = sum(values.values())
print(f"PART 1: {part_1_answer}")

# PART 2
CRT = [[] for _ in range(6)]
cycles = 0
_x_ = 1
data_position = 0
advance = True

while data_position < len(data):
    # start the cycle
    cycles += 1

    # draw CRT at the start of each cycle
    crt_position = cycles - 1
    point = "#" if _x_ - 1 <= crt_position % 40 <= _x_ + 1 else "."
    CRT[crt_position // 40].append(point)

    # get the step we need to do
    step = data[data_position]

    if not advance:
        _x_ += temp_x
        temp_x = 0
        advance = True

    elif "addx" in step:
        temp_x = int(step.split()[1])
        advance = False

    if advance:
        data_position += 1


# OUTPUT for PART 2
part_2_answer = "\n".join(
    "".join("#" if column == "#" else " " for column in row) for row in CRT
)
print(f"PART 2:\n{part_2_answer}")
