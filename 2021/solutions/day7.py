"""https://adventofcode.com/2021/day/7"""

from helper import read
import statistics as s

# READ INPUT
data = read("./2021/inputs/7.txt")
# TEST INPUT
data = read("./2021/inputs/7-test.txt")
# PARSE INPUT
data = data.split(",")
data = [int(x) for x in data]

# PART 1
# median solution -> works for the test case ()
m = s.median(data)
fuel = [abs(x - m) for x in data]
part_1_answer = sum(fuel)
print(f"PART 1: {part_1_answer}")

# PART 2
# more expensive each move


# attempt 1 use the mean
mean = round(s.mean(data))
fuel2 = [abs(x - mean) for x in data]
fuel2 = [(x * (x + 1)) / 2 for x in fuel2]
part_2_answer = sum(fuel2)
print(f"PART 2: {part_2_answer}")

# to high -> 104149135
