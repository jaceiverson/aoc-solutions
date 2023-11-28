"""https://adventofcode.com/2015/day/5"""

from aoc_util import read, chunks

# READ INPUT
data = read("./2015/inputs/5.txt").strip().split("\n")
# TEST INPUT
# data = read("./2015/inputs/5-test.txt")
# PARSE INPUT

# Part 1 RULES
def check_nice(word: str):
    return check_vowel(word) and check_double_letter(word) and check_bad_strs(word)


def check_vowel(word: str) -> bool:
    return len([x for x in word if x in "aeiou"]) >= 3


def check_double_letter(word: str) -> bool:
    return any(c == word[idx] for idx, c in enumerate(word[:-1], 1))


def check_bad_strs(word: str) -> bool:
    return all(b not in word for b in ["ab", "cd", "pq", "xy"])


part_1_answer = sum(check_nice(d) for d in data)
print(f"PART 1: {part_1_answer}")


# PART 2 Rules
def check_nice_2(word: str) -> bool:
    return check_pair(word) and check_sandwhich_letter(word)


def check_pair(word: str) -> bool:
    # loop through and check each pair
    for idx, c in enumerate(word):
        main_pair = word[idx : idx + 2]
        for idx2, c2 in enumerate(word[idx + 2 :], idx + 2):
            compare_pair = word[idx2 : idx2 + 2]
            if main_pair == compare_pair:
                return True
    return False


def check_sandwhich_letter(word: str) -> bool:
    return any(c == word[idx] for idx, c in enumerate(word[:-2], 2))


part_2_answer = sum(check_nice_2(word) for word in data)
print(f"PART 2: {part_2_answer}")
