"""https://adventofcode.com/2021/day/2"""

from read import read

route = read("./inputs/2.txt")
route = route.strip().split("\n")

# PART 1
horizontal = 0
depth = 0
for step in route:
    detail = step.split()
    if detail[0] == "forward":
        horizontal += int(detail[1])
    elif detail[0] == "up":
        depth -= int(detail[1])
    elif detail[0] == "down":
        depth += int(detail[1])

# answer
m = horizontal * depth

# PART 2
horizontal = 0
depth = 0
aim = 0
for step in route:
    detail = step.split()
    instruction, value = detail
    value = int(value)
    if instruction == "forward":
        horizontal += value
        depth += aim * value
    elif instruction == "up":
        aim -= value
    elif instruction == "down":
        aim += value

# answer
m = horizontal * depth
