"""https://adventofcode.com/2016/day/5"""


from aoc_util import read
from hashlib import md5

# READ INPUT
data = read("./2016/inputs/5.txt").strip()
# TEST INPUT
# data = read("./2016/inputs/5-test.txt").strip()
# PARSE INPUT

# PART 1
password = ""
counter = 0
while len(password) < 8:
    base = data + str(counter)
    _hash = md5(base.encode()).hexdigest()
    if _hash[:5] == "00000":
        password += _hash[5]
    counter += 1

part_1_answer = password
print(f"PART 1: {part_1_answer}")

# PART 2
password = [None] * 8
counter = 0
while not all(password):
    base = data + str(counter)
    _hash = md5(base.encode()).hexdigest()
    if (
        _hash[:5] == "00000"
        and _hash[5].isdigit()
        and 0 <= int(_hash[5]) < 8
        and password[int(_hash[5])] is None
    ):
        password[int(_hash[5])] = _hash[6]
    counter += 1

part_2_answer = "".join(password)
print(f"PART 2: {part_2_answer}")
