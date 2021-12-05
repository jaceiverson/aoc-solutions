"""https://adventofcode.com/2021/day/1"""

from read import read

sonar = read("./inputs/1.txt")
sonar = sonar.strip().split("\n")
sonar = [int(x) for x in sonar]

# PART 1
increase = 0
decrease = 0
no_change = 0
for idx, tick in enumerate(sonar[1:]):
    if tick > sonar[idx]:
        increase += 1
    elif tick < sonar[idx]:
        decrease += 1
    else:
        no_change += 1

# answer
part_1_answer = increase
part_1_answer

# PART 2
increase = 0
decrease = 0
no_change = 0
for idx, tick in enumerate(sonar[:-3]):
    first_group = sonar[idx : idx + 3]
    second_group = sonar[idx + 1 : idx + 4]
    if sum(first_group) < sum(second_group):
        increase += 1
    elif sum(first_group) > sum(second_group):
        decrease += 1
    else:
        no_change += 1

# answer
part_2_answer = increase
part_2_answer
