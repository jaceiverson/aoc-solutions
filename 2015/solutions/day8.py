"""https://adventofcode.com/2015/day/8"""

from helper import read
import re

# READ INPUT
data = read("./2015/inputs/8.txt").strip().split("\n")
# TEST INPUT
data = read("./2015/inputs/8-test.txt").strip().split("\n")
# PARSE INPUT

# PART 1
new_data = []
for line in data:
    # replace the hexidecimal chars with a 1 (one character)
    line = re.sub(r"\\x[0-9a-f]{2}", "1", line, re.IGNORECASE)
    # replace the slashes
    line = re.sub(r"\\", "", line)
    # get the charcater count
    characters = len(line.strip('"'))
    #
    new_data.append(characters)

code_characters = sum(len(x) for x in data)
part_1_answer = code_characters - sum(new_data)
print(f"PART 1: {part_1_answer}")
# TO HIGH -> 1477
# TO HIGH -> 1469 (changed to re.IGNORECASE)


# PART 2

part_2_answer = None
print(f"PART 2: {part_2_answer}")
