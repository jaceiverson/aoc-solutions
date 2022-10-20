"""https://adventofcode.com/2015/day/11"""

from helper import read
from string import ascii_lowercase as alphabet

# READ INPUT
data = read("./2015/inputs/11.txt")
# TEST INPUT
# data = read("./2015/inputs/11-test.txt")
# PARSE INPUT

# FROM day 5
def check_double_letter(word: str) -> bool:
    return any(c == word[idx] for idx, c in enumerate(word[:-1], 1))


def check_pair(word: str) -> bool:
    # loop through and check each pair
    for idx, c in enumerate(word):
        main_pair = word[idx : idx + 2]
        for idx2, c2 in enumerate(word[idx + 2 :], idx + 2):
            compare_pair = word[idx2 : idx2 + 2]
            if main_pair == compare_pair:
                return True
    return False


# PART 1

part_1_answer = None
print(f"PART 1: {part_1_answer}")

# PART 2

part_2_answer = None
print(f"PART 2: {part_2_answer}")
