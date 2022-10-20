"""https://adventofcode.com/2015/day/4"""

from helper import mytime
import hashlib

data = "iwrupvqb"
test_data = "abcdef"  # 609043
test_data_too = "pqrstuv"  # 1048970


# PART 1
# brute force
@mytime
def part_1(input_str: str, iterations: int = 10_000_000) -> str:
    for num in range(iterations):
        result = hashlib.md5((input_str + str(num)).encode())
        if result.hexdigest().startswith("00000"):
            return num


part_1_answer = part_1(data)
print(f"PART 1: {part_1_answer}")

# PART 2
@mytime
def part_2(input_str: str, iterations: int = 10_000_000) -> str:
    for num in range(iterations):
        result = hashlib.md5((input_str + str(num)).encode())
        if result.hexdigest().startswith("000000"):
            return num


part_2_answer = part_2(data)
print(f"PART 2: {part_2_answer}")
