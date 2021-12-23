"""https://adventofcode.com/2019/day/4"""

from helper import read
import re

# READ INPUT
data = read("./2019/inputs/4.txt")
# TEST INPUT
# data = read("./2019/inputs/4-test.txt")
# PARSE INPUT
start,stop = data.strip().split('-')
start,stop = int(start),int(stop)

# PART 1
possible_solutions = []
adjacent_nums = r'((\w)\2)+'
for num in range(start,stop+1):
    zero, one, two, three, four, five = [int(x) for x in list(str(num))]
    # check increasing numbers & at least 2 adjacent
    if zero <= one <= two <= three <= four <= five and bool(re.search(adjacent_nums,str(num))):
        possible_solutions.append(num)
    
part_1_answer = len(possible_solutions)
print(f"PART 1: {part_1_answer}")

# PART 2 -> TODO
possible_solutions_two = []
exactly_2_adjacent_nums = r'(\d)(?!\1)(\d)\2(?!\2)\d'
for num in range(start,stop+1):
    zero, one, two, three, four, five = [int(x) for x in list(str(num))]
    # check increasing numbers & at least 2 adjacent
    if zero <= one <= two <= three <= four <= five and bool(re.search(exactly_2_adjacent_nums,str(num))):
        possible_solutions_two.append(num)

part_2_answer = len(possible_solutions_two)
print(f"PART 2: {part_2_answer}")
# TOO LOW -> 724