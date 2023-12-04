"""https://adventofcode.com/2023/day/4"""

from aoc_util import read

# READ INPUT
data = read("./2023/inputs/4.txt").strip().split("\n")
# TEST INPUT
# data = read("./2023/inputs/4-test-e.txt").strip().split("\n")
# PARSE INPUT


# PART 1
def part_1(data):
    sum_ = 0
    for line in data:
        card, nums = line.split(": ")
        nums, my_nums = nums.split(" | ")
        count_ = 0
        # print(card,nums,my_nums)
        for x in nums.split():
            if x in my_nums.split():
                if count_ > 0:
                    count_ = count_ * 2
                else:
                    count_ = 1
        sum_ += count_
    return sum_


print(f"PART 1: {part_1(data)}")


# PART 2
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


print(f"PART 2: {part_2(data)}")
