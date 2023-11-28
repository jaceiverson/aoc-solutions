"""https://adventofcode.com/2015/day/19"""

from aoc_util import read

# READ INPUT
data = read("./2015/inputs/19.txt")
# TEST INPUT
# data = read("./2015/inputs/19-test.txt").strip()
# PARSE INPUT
replacements, base = data.strip().split("\n\n")
replacements = replacements.split("\n")


def find_possible_molecules(rules, base):
    options = []
    for r in rules:
        print(r)
        start, new = r.split(" => ")
        for idx, letter in enumerate(base):
            if len(start) == 1 and letter == start:
                temp = list(base)
                temp[idx] = new
                options.append("".join(temp))
            elif len(start) == 2 and base[idx : idx + 2] == start:
                temp = list(base)
                temp[idx : idx + 2] = new
                options.append("".join(temp))
    return set(options)


# PART 1
part_1_answer = find_possible_molecules(replacements, base)
print(f"PART 1: {len(part_1_answer)}")
# TO HIGH -> 615 I had the index setting incorrect


# PART 2
part_2_answer = None
print(f"PART 2: {part_2_answer}")
