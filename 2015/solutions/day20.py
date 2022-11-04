"""https://adventofcode.com/2015/day/20"""

from helper import read

# READ INPUT
data = read("./2015/inputs/20.txt").strip()
# TEST INPUT
# data = read("./2015/inputs/20-test.txt")
# PARSE INPUT
def calculate_presents(house_number: int) -> int:
    return sum(
        house * 10 for house in range(1, house_number + 1) if house_number % house == 0
    )


present_count = int(data)

# Brute force
def visit_houses(present_count: int):
    house = 0
    presents = 0
    while presents <= present_count:
        house += 1
        presents = calculate_presents(house)
        # print(f"{house=},{presents=},{presents/house}")
    return house, presents


# PART 1
present_goal = int(data)
part_1_answer, presents = visit_houses(present_goal)
print(f"PART 1: {part_1_answer}")

# PART 2

part_2_answer = None
print(f"PART 2: {part_2_answer}")
