"""https://adventofcode.com/2025/day/2"""

from aoc_util import read
from rich import print

# MAIN INPUT
data = read("./2025/inputs/2.txt").strip().split(",")
# TEST INPUT
# data = read("./2025/inputs/2-test.txt").strip().split(",")
# EXAMPLE INPUT
# data = read("./2025/inputs/2-test-e.txt").strip().split("\n")
# PARSE INPUT


# PART 1
def part_1(data: list):
    invalid_ids = []
    for num_range in data:
        low_, high_ = map(int,str(num_range).split('-'))
        for current_num in range(low_,high_+1):
            num_str_len = len(str(current_num))
            half_point = int(num_str_len / 2)
            if num_str_len %2!=0:
                continue

            if str(current_num)[:half_point] == str(current_num)[half_point:]:
                invalid_ids.append( current_num)
    return sum(invalid_ids)


print(f"PART 1: {part_1(data)}")


# PART 2
def chunks(input_list: list, n: int = 5) -> list[list]:
    """
    params:
        l: takes in a list (or list like object)
        n: takes an int: default = 5 this is how big the smaller
            chunks will be
    returns:
        a list of lists with the smaller lists being size n
    """
    return [input_list[i : i + n] for i in range(0, len(input_list), n)]

def part_2(data: list):
    invalid_ids = []
    for num_range in data:
        low_, high_ = map(int,str(num_range).split('-'))
        for current_num in range(low_,high_+1):
            num_str_len = len(str(current_num))
            half_point = int(num_str_len / 2)
            # chunk in subsections
            for subsection_count in range(1,half_point+1):
                segmented_list = chunks(str(current_num),subsection_count)
                if len(set(segmented_list))==1 and current_num not in invalid_ids:
                    invalid_ids.append(current_num)
                    

    return sum(invalid_ids)



print(f"PART 2: {part_2(data)}")
