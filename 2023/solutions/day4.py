"""https://adventofcode.com/2023/day/4"""

from aoc_util import read
from aoc_util.helper import avgtime
from rich import print

# READ INPUT
data = read("./2023/inputs/4.txt").strip().split("\n")
# TEST INPUT
# data = read("./2023/inputs/4-test-e.txt").strip().split("\n")
# PARSE INPUT


# PART 1
@avgtime(run_times=100, return_times=True)
def part_1(data):
    sum_ = 0
    # each card is a line
    for line in data:
        card, nums = line.split(": ")
        nums, my_nums = nums.split(" | ")
        count_ = 0
        for x in nums.split():
            if x in my_nums.split():
                if count_ > 0:
                    count_ = count_ * 2
                else:
                    count_ = 1
        sum_ += count_
    return sum_


@avgtime(run_times=100, return_times=True)
def part_1_sets(data):
    new_sum = 0
    # each card is a line
    for line in data:
        card, nums = line.split(": ")
        nums, my_nums = nums.split(" | ")
        new_count = len(set(nums.split()).intersection(set(my_nums.split())))
        if new_count > 0:
            new_sum += 2 ** (new_count - 1)
    return new_sum


@avgtime(run_times=100)
def part_1_one_liner(data):
    return sum(
        2
        ** (
            len(
                set(line.split(": ")[1].split(" | ")[0].split()).intersection(
                    set(line.split(": ")[1].split(" | ")[1].split())
                )
            )
            - 1
        )
        for line in data
        if len(
            set(line.split(": ")[1].split(" | ")[0].split()).intersection(
                set(line.split(": ")[1].split(" | ")[1].split())
            )
        )
        > 0
    )


@avgtime(run_times=100)
def part_1_gpt_(data):
    return sum(
        2
        ** (
            len(
                set(line.split(": ")[1].split(" | ")[0].split())
                & set(line.split(": ")[1].split(" | ")[1].split())
            )
            - 1
        )
        for line in data
        if len(
            set(line.split(": ")[1].split(" | ")[0].split())
            & set(line.split(": ")[1].split(" | ")[1].split())
        )
        > 0
    )


p1, p1t = part_1(data)
p1_avg_time = sum(p1t) / len(p1t)
p1s, p1st = part_1_sets(data)
set_avg_time = sum(p1st) / len(p1st)
print(f"PART 1: {p1}")
print(f"PART 1: {p1s}")
print(
    f"PART 1 -> Sets are {p1_avg_time/set_avg_time:.4f} times faster "
    f"and {p1_avg_time-set_avg_time:.0f} total ns faster\n"
)
# PART 1 -> Sets are 2.2796 times faster and 688552 total ns faster
# print(f"PART 1: {part_1_one_liner(data)}")
# print(f"PART 1: {part_1_gpt_(data)}")


# PART 2
@avgtime(run_times=100, return_times=True)
def part_2(data):
    score_cards = [1 for x in data]
    for line_idx, line in enumerate(data):
        card, nums = line.split(": ")
        nums, my_nums = nums.split(" | ")
        count_ = 0
        # print(card,nums,my_nums)
        for x in nums.split():
            if x in my_nums.split():
                count_ += 1

        # increment next cards
        for y in range(1, count_ + 1):
            score_cards[y + line_idx] += score_cards[line_idx]

    return sum(score_cards)


@avgtime(run_times=100, return_times=True)
def part_2_sets(data):
    score_cards = [1 for x in data]
    for line_idx, line in enumerate(data):
        card, nums = line.split(": ")
        nums, my_nums = nums.split(" | ")
        count_ = len(set(nums.split()) & (set(my_nums.split())))

        # increment next cards
        for y in range(1, count_ + 1):
            score_cards[y + line_idx] += score_cards[line_idx]

    return sum(score_cards)


p2, p2t = part_2(data)
p2_avg_time = sum(p2t) / len(p2t)
p2s, p2st = part_2_sets(data)
set_avg_time_2 = sum(p2st) / len(p2st)
print(f"PART 2: {p2}")
print(f"PART 2: {p2s}")
print(
    f"PART 2 -> Sets are {p2_avg_time/set_avg_time_2:.4f} times faster "
    f"and {p2_avg_time-set_avg_time_2:.0f} total ns faster"
)
# PART 2 -> Sets are 2.2181 times faster and 703242 total ns faster
