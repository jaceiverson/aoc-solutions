"""https://adventofcode.com/2022/day/6"""

from aoc_util import read

# READ INPUT
data = read("./2022/inputs/6.txt").strip()
# TEST INPUT
# data = read("./2022/inputs/6-test.txt").strip().split("\n")
# PARSE INPUT
def find_start_character(
    data: str,
    consecutive_unique: int,
    output: bool = False,
) -> int:
    sequence_found = False
    idx = consecutive_unique
    while not sequence_found:
        d = data[idx - consecutive_unique : idx]
        if len(set(d)) == len(d):
            sequence_found = True
            if output:
                print(idx)
                print(d)
            return idx
        idx += 1


# PART 1
part_1_answer = find_start_character(data, 4)
print(f"PART 1: {part_1_answer}")

# PART 2
part_2_answer = find_start_character(data, 14)
print(f"PART 2: {part_2_answer}")

# a little disapointed this one was so slow,
# I forgot about sets for a while and was trying to do the comparison myself. oops
# fun problem
