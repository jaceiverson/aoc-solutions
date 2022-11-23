"""https://adventofcode.com/2021/day/6"""

from helper import read
from collections import Counter

# READ INPUT
data = read("./2021/inputs/6.txt")
# TEST INPUT
# data = read("./2021/inputs/6-test.txt")
# PARSE INPUT
data = data.strip().split(",")
data = [int(x) for x in data]


def old_part_one():
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

    # PART 2
    # TODO come up with a more efficent solution
    # calculate the base (seed numbers) how many they will individually create
    # this can be done with % division?
    # then we can extrapilate how many of the ones that are created will create and so forth
    # the brute force is way too slow, even for the 5 seed numbers
    def offspring(start_value, years):
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


# Solved with the dictionary hint from reddit
def parse(data, generations):
    fish = Counter(data)
    for x in range(9):
        if fish.get(x) is None:
            fish[x] = 0

    for _ in range(generations):
        new_fish = fish[0]
        fish[0] = fish[1]
        fish[1] = fish[2]
        fish[2] = fish[3]
        fish[3] = fish[4]
        fish[4] = fish[5]
        fish[5] = fish[6]
        fish[6] = fish[7] + new_fish
        fish[7] = fish[8]
        fish[8] = new_fish

        # print(f"Generation {_}: {sum(fish.values())}")
    return sum(fish.values())


part_1_answer = parse(data, 80)
print(f"PART 1: {part_1_answer}")

part_2_answer = parse(data, 256)
print(f"PART 2: {part_2_answer}")
# TOW LOW -> 26984457539 (example,,, oops 26984457539)
