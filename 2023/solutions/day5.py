"""https://adventofcode.com/2023/day/5"""

from aoc_util import read
from aoc_util.helper import chunks
from rich import print

# READ INPUT
data = read("./2023/inputs/5.txt").strip().split("\n\n")
# TEST INPUT
# data = read("./2023/inputs/5-test-e.txt").strip().split("\n\n")
#  data = read("./2023/inputs/5-test.txt").strip().split("\n\n")
# PARSE INPUT


def parse_sub_classes(sub_data):
    configs = sub_data.split(":\n")[1].split("\n")
    map_ = {}
    for a in configs:
        a = list(map(int, a.split()))

        for a_ in range(a[2]):
            map_[a_ + a[1]] = a[0] + a_
    return map_


def parse_sub_classes_better(sub_data):
    configs = sub_data.split(":\n")[1].split("\n")
    map_ = {}
    for a in configs:
        a = list(map(int, a.split()))
        map_[(a[1], a[1] + a[2] - 1)] = a[0] - a[1]
    # print(map_)
    return map_


def get_map(data: list):
    seeds, soil, fert, water, light, temp, hum, location = data
    seeds = list(map(int, seeds.split(": ")[1].split()))
    return seeds, [parse_sub_classes_better(x) for x in data[1:]]


def progress(position: int, step: dict):
    for k, v in step.items():
        if position >= k[0] and position <= k[1]:
            return position + v
    return position


def seed_path(seed: int, mapping: dict):
    position = seed
    for step in mapping:
        # print(f"{idx_} -> {position}")
        position = progress(position, step)
    return position


# PART 1
def part_1(data: list):
    start_seeds, map_ = get_map(data)
    seed_final_placement = [seed_path(seed, map_) for seed in start_seeds]
    # print(seed_final_placement)
    return min(seed_final_placement)


print(f"PART 1: {part_1(data)}")


# PART 2
def get_seed_ranges(seeds: list):
    new_ranges = []
    # start and range for each seed
    for s, r in chunks(seeds, 2):
        new_ranges += list(range(s, s + r))
    return new_ranges


def part_2(data: list):
    start_seeds, map_ = get_map(data)
    print(get_seed_ranges(start_seeds))
    seed_final_placement = [
        seed_path(seed, map_) for seed in get_seed_ranges(start_seeds)
    ]
    # print(seed_final_placement)
    return min(seed_final_placement)


# print(f"PART 2: {part_2(data)}")
"""
Part 2 brute force doesn't work, but what if we tried to solve it backwords? 

Start with the lowest value in the last section (location) and see if we can work backwords? 

ok clever idea, but I dont' think this will work
"""


def lowest_possible_start(d: dict):
    min(k[0] + v for k, v in d.items())


def part_2_backwords(data: list):
    start_seeds, map_ = get_map(data)
    map_[-1].values()


"""
Part 2 looping over the instructions and maping all positions instead of looping through positions and mapping that way?
"""


def de_dupe_s(s: list):
    s = [x for x in s if x[0] is not None]
    s.sort()
    new_s = []
    idx_ = 0
    while idx_ < len(s):
        if idx_ == len(s) - 1:
            new_s.append(s[idx_])
        # next element overlaps
        elif s[idx_][1] >= s[idx_ + 1][0] - 1:
            # overlaps partially or is continuous
            if s[idx_][1] < s[idx_ + 1][1]:
                new_s.append([s[idx_][0], s[idx_ + 1][1]])
            # overlaps completely
            elif s[idx_][1] >= s[idx_ + 1][1]:
                new_s.append(s[idx_])
            idx_ += 1
        elif s[idx_] == s[idx_ + 1]:
            new_s.append(s[idx_])
            idx_ += 1
        else:
            new_s.append(s[idx_])
        idx_ += 1

    return new_s


def output(n: int):
    print(f"{n[0]:,d}, {n[1]:,d}")


def part_2_reverse(data: list):
    start_seeds, map_ = get_map(data)
    print(map_)
    # reformat the seeds into groups of 2 and
    # change the second value from the range to the actual value
    s = chunks(start_seeds, 2)
    s = [[x[0], x[0] + x[1] - 1] for x in s]
    s = de_dupe_s(s)
    # [output(x) for x in s]
    print(s)

    # loop through the mapping steps instead of the seeds
    # loops through the steps seed -> soil -> fert -> water -> etc.
    for step_idx, step in enumerate(map_):
        print(step_idx)
        # loops through the ranges in teh step
        # k is the range k[0] lower and k[1] upper
        # v is the value it gets changed to
        # for each step, there are values that are mapped, that only need to be considered next step
        new_values = []
        for k, v in step.items():
            # remove any duplicate or overlapping seed ranges
            s = de_dupe_s(s)

            for sg in s:  # sg = seed_group
                s_min = sg[0]
                s_max = sg[1]
                if k[1] < s_min or k[0] > s_max:
                    # nothing happens
                    pass
                elif k[0] < s_min:
                    if s_max > k[1] >= s_min:
                        # the map found values on the bottom end
                        # need to change s[0] to now be k[1] for future checks
                        sg[0] = k[1] + 1
                        new_values.append(
                            [s_min + v, k[1] + v]
                        )  # need to have a new list for these so the same rule isn't applied again
                    elif k[1] >= sg[1]:
                        # everything in this seed group is now just +=v
                        new_values.append([sg[0] + v, sg[1] + v])
                        sg[0] = None
                        sg[1] = None
                elif k[0] >= s_min:
                    if k[1] >= s_max:
                        # the map found values on the top end
                        # need to change s[0] to now be k[1] for future checks
                        sg[1] = k[0] - 1
                        new_values.append([k[0] + v, s_max + v])
                    elif k[1] < s_max:
                        # the map found values in the middle
                        # move the bounds for sg and create 3 new groups
                        # one for the bottom (stays in s)
                        # of the the middle (moves on to new seeds)
                        # one for the top (stays in s)
                        sg[1] = k[0] - 1  # change base (lower) - not range, not changed
                        s.append(
                            [k[1] + 1, s_max]
                        )  # add (upper) - not in range,not changed
                        new_values.append(
                            [k[0] + v, k[1] + v]
                        )  # add (mid) - in range, changed by v

        if new_values:
            s += new_values

        s = de_dupe_s(s)
        print(s)

    return min(sum(s, []))


print(f"PART 2: {part_2_reverse(data)}")
# TO LOW: 6_295_169
# TO HIGH: 276_864_123
# TO HIGH: 1_037_813_664
# Removed de-dup function: 651_227_070
