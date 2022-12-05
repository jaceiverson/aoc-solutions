"""https://adventofcode.com/2016/day/10"""

from helper import read
import math

# READ INPUT
data = read("./2016/inputs/10.txt").strip().split("\n")
# TEST INPUT
# data = read("./2016/inputs/10-test.txt").strip().split("\n")
# PARSE INPUT


def give_value(key: str, value: str, bots: dict) -> dict:
    if bots.get(int(key)):
        bots[int(key)].extend([int(value)])
    else:
        bots[int(key)] = [int(value)]
    return bots


def make_bots():
    assignments = [x for x in data if x.startswith("value")]
    distributions = [x for x in data if x.startswith("bot")]
    # Assign the bots to their values
    bots = {}
    for line in assignments:
        _, value, _, _, _, bot = line.split()
        bots = give_value(bot, value, bots)
    return bots, distributions


def part_1(bots, distributions):
    output = {}
    # Distribute the values
    sixty_one_and_seventeen = False
    while not sixty_one_and_seventeen:
        possible_bots = [x[0] for x in bots.items() if len(x[1]) == 2]
        for bot in possible_bots:
            possible_instructions = [
                x for x in distributions if f"bot {bot} gives" in x
            ]
            for line in possible_instructions:
                # bot 127 gives low to output 1 and high to bot 180
                (
                    _,
                    _,
                    _,
                    _,
                    _,
                    low_desitnation,
                    low_id,
                    _,
                    _,
                    _,
                    high_desgination,
                    high_id,
                ) = line.split()

                values = bots[bot]
                min_, max_ = sorted(values)
                if max_ == 61 and min_ == 17:
                    print(f"{line=}")
                    sixty_one_and_seventeen = True
                    magic_bot = bot
                if low_desitnation == "output":
                    output = give_value(low_id, min_, output)
                else:
                    bots = give_value(low_id, min_, bots)
                if high_desgination == "output":
                    output = give_value(high_id, max_, output)
                else:
                    bots = give_value(high_id, max_, bots)

                bots[int(bot)] = []
    return magic_bot


def part_2(bots, distributions):
    output = {}
    while (not output.get(0)) or (not output.get(1)) or (not output.get(2)):
        possible_bots = [x[0] for x in bots.items() if len(x[1]) == 2]
        for bot in possible_bots:
            possible_instructions = [
                x for x in distributions if f"bot {bot} gives" in x
            ]
            for line in possible_instructions:
                # bot 127 gives low to output 1 and high to bot 180
                (
                    _,
                    _,
                    _,
                    _,
                    _,
                    low_desitnation,
                    low_id,
                    _,
                    _,
                    _,
                    high_desgination,
                    high_id,
                ) = line.split()
                min_, max_ = sorted(bots[bot])
                if low_desitnation == "output":
                    output = give_value(low_id, min_, output)
                else:
                    bots = give_value(low_id, min_, bots)
                if high_desgination == "output":
                    output = give_value(high_id, max_, output)
                else:
                    bots = give_value(high_id, max_, bots)

                bots[int(bot)] = []
        # print(f"{output=}")
    return output


# PART 1
bots, dist = make_bots()
part_1_answer = part_1(bots, dist)
print(f"PART 1: {part_1_answer}")
# PART 2
bots, dist = make_bots()
output = part_2(bots, dist)
part_2_answer = math.prod(v[0] for k, v in output.items() if k in [0, 1, 2])
print(f"PART 2: {part_2_answer}")
