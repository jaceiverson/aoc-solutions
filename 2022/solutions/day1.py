"""https://adventofcode.com/2022/day/1"""

from helper import read

# READ INPUT
data = read("./2022/inputs/1.txt").strip().split("\n\n")
# TEST INPUT
# data = read("./2022/inputs/1-test.txt").strip().split("\n\n")
# PARSE INPUT

# PART 1
max_cal = 0
for elf in data:
    cal = sum(int(x) for x in elf.strip().split("\n"))
    if cal > max_cal:
        max_cal = cal

part_1_answer = max_cal
print(f"PART 1: {part_1_answer}")

# PART 2
# restructure to list comprehension
elf_cals = [sum(int(x) for x in elf.strip().split("\n")) for elf in data]
elf_cals.sort()

part_2_answer = sum(elf_cals[-3:])
print(f"PART 2: {part_2_answer}")
