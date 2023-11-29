"""https://adventofcode.com/2015/day/12"""

from aoc_util import read
import re
import json
from collections import Counter

# READ INPUT
data = read("./2015/inputs/12.txt").strip()
# TEST INPUT
data = '{"d":"red","e":[1,2,3,4],"f":5}'
# PARSE INPUT

# PART 1
digits = re.findall(r"-?\d+", data)
part_1_answer = sum(int(x) for x in digits) if digits else 0
print(f"PART 1: {part_1_answer}")

# PART 2
new_data = {}
while 0:
    if isinstance(data, dict):
        for key, value in data.items():
            if "red":
                pass
    break


# https://stackoverflow.com/questions/43752962/how-to-iterate-through-a-nested-dict
def get_all_keys(d):
    for key, value in d.items():
        yield key
        if isinstance(value, dict):
            yield from get_all_keys(value)


non_red_data = re.sub(r"{.*\"red\".*}", "", data)
part_2_answer = None
print(f"PART 2: {part_2_answer}")
