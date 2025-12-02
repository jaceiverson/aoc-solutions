"""https://adventofcode.com/2025/day/1"""

from aoc_util import read
from rich import print

# MAIN INPUT
data = read("./2025/inputs/1.txt").strip().split("\n")
# TEST INPUT
# data = read("./2025/inputs/1-test.txt").strip().split("\n")
# EXAMPLE INPUT
# data = read("./2025/inputs/1-test-b.txt").strip().split("\n")
# PARSE INPUT


# PART 1
def part_1(data: list):
    zeros = 0
    current = 50
    for inst in data:
        dir_,num_ = inst[0],int(inst[1:])
        if dir_ == 'L':
            current = (current - num_) % 100
        else:
            current = (current + num_) % 100

        if current ==0:
            zeros += 1

    return zeros


print(f"PART 1: {part_1(data)}")


# PART 2
def get_new_current(dir_:str,current_:int,num_:int) -> tuple[int,int]:
    if dir_ == 'L':
        return (current_ - num_) % 100, abs((current_ - num_) // 100) 
    else:
        return (current_ + num_) % 100, abs((current_ + num_) // 100)


def part_2(data: list):
    zeros_passes = 0
    current = 50
    for inst in data:
        # print(f"{zeros_passes=}")
        # print(f"{current=}")
        # print(f"{inst=}")
        dir_,num_ = inst[0],int(inst[1:])
        current, temp_zeros = get_new_current(dir_,current,num_)
        zeros_passes += temp_zeros
    return zeros_passes


print(f"PART 2: {part_2(data)}")
# 2604 - LOW (forgot about numbers > 100)
# 4647 - LOW (did modular and remainder division still low)
# 7209 - HIGH (removed the check on current != 0)
# 8095 - HIGH (made sure to check again if I landed on 0 after passing it)
# 6913 - INCORRECT
