"""https://adventofcode.com/2019/day/1"""

from aoc_util import read

# READ INPUT
data = read("./2019/inputs/1.txt")
# TEST INPUT
# data = read("./2019/inputs/1-test.txt")
# PARSE INPUT
data = data.strip().split("\n")
# PART 1

part_1_answer = sum(int(x) // 3 - 2 for x in data)
print(f"PART 1: {part_1_answer}")


# PART 2
def calc_fuel(weight):
    fuel = weight // 3 - 2
    if fuel > 6:
        return fuel + calc_fuel(fuel)
    return fuel


part_2_answer = sum(calc_fuel(int(x)) for x in data)
print(f"PART 2: {part_2_answer}")
