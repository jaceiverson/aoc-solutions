"""https://adventofcode.com/2018/day/5"""

from helper import read
from collections import Counter

# READ INPUT
data = read("./2018/inputs/5.txt")
# TEST INPUT
# data = read("./2018/inputs/5-test.txt")
# PARSE INPUT
data = data.strip()


def cause_reactions(data):
    idx = 0
    while True:
        first, second = data[idx : idx + 2]
        # this statement finds characters that are the same case
        if (first.islower() and second.islower()) or (
            first.isupper() and second.isupper()
        ):
            idx += 1
        # this means the cases are different
        # lets convert them both to lower and check if they are the same
        elif first.lower() != second.lower():
            idx += 1
        # if we reach this block, the cases are different, and the letters match
        else:
            data = data.replace(first + second, "", 1)
            idx -= 1
            idx = max(idx, 0)

        if idx >= len(data) - 1:
            return data


# PART 1
part_1_answer = len(cause_reactions(data.strip()))
print(f"PART 1: {part_1_answer}")

# PART 2
# data = read("./2018/inputs/5.txt").strip()
c = Counter(data.lower())
min_length = len(data)
magic_letter = None
for letter in c:
    reactions = cause_reactions(data.replace(letter, "").replace(letter.upper(), ""))
    if len(reactions) < min_length:
        min_length = len(reactions)
        magic_letter = letter

part_2_answer = min_length

print(f"PART 2: {magic_letter}:{part_2_answer}")

# TO HIGH -> 11276
