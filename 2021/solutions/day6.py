"""https://adventofcode.com/2021/day/6"""

from helper import read

# READ INPUT
data = read("./2021/inputs/6.txt")
# TEST INPUT
data = read("./2021/inputs/6-test.txt")
# PARSE INPUT
data = data.strip().split(",")
data = [int(x) for x in data]
print(f"INITIAL STATE: {len(data)} fish")
# PART 1 - 80 generations - brute force
years = 80
for gen in range(1, years + 1):
    # check if any are 0
    zeros = data.count(0)
    # decrease by 1 (if < 0 back up to 6)
    data = [x - 1 if x - 1 >= 0 else 6 for x in data]
    # add in the new fish
    data = data + [8] * zeros
    # print(f"AFTER {gen} days: {len(data)} fish")

part_1_answer = len(data)
print(f"PART 1: {part_1_answer}")

# PART 2
# TODO come up with a more efficent solution
# calculate the base (seed numbers) how many they will individually create
# this can be done with % division?
# then we can extrapilate how many of the ones that are created will create and so forth
# the brute force is way too slow, even for the 5 seed numbers

def offspring(start_value,years):
    """
    Given a fish number (start_value) and the number of years left
    Calculates the direct offspring count (no grandfish) of that specific fish
    Returns int value of offspring
    """
    # first reproduction to even playing field
    # this is the + 1 we add back in at the end
    remaining_years = years - (start_value + 1)
    # every 7 generations another is created
    # except the first time (9 generations)
    return (remaining_years // 7) + 1 

offspring(8,8,False)

part_2_answer = len(data)
print(f"PART 2: {part_2_answer}")
