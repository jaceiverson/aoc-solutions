"""https://adventofcode.com/2023/day/1"""

from aoc_util import read

# READ INPUT
data = read("./2023/inputs/1.txt").strip().split("\n")
# TEST INPUT
# data = read("./2023/inputs/1-test-b.txt").strip().split("\n")
# PARSE INPUT


# PART 1
def part_1(data):
    y = 0
    for x in data:
        f, s = None, None
        for letter in x:
            if letter.isnumeric() and f is None:
                f = int(letter)

        for letter in x[::-1]:
            if letter.isnumeric() and s is None:
                s = int(letter)

        if f is None and s is None:
            print("BROKEN")

        if f is None:
            f = s
        if s is None:
            s = f

        # print(f"{f}{s}")
        y += int(f"{f}{s}")
    return y


# PART 2
def part_2(data):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    nums_short = ["one", "two", "thr", "fou", "fiv", "six", "sev", "eig", "nin"]
    z = 0
    for x in data:
        #  print(x)
        letter_numbers = []
        number_numbers = []
        # check for all the letter number indexes
        for num_idx, num in enumerate(nums):
            if num in x:
                for l_idx, letter in enumerate(x[:-2]):
                    if x[l_idx : l_idx + 3] == nums_short[num_idx]:
                        letter_numbers.append(l_idx)

        # check for al the number number indexes
        for l_idx, letter in enumerate(x):
            if letter.isnumeric():
                number_numbers.append(l_idx)

        first_number = min(letter_numbers + number_numbers)
        last_number = max(letter_numbers + number_numbers)

        if first_number in letter_numbers:
            first_num = nums_short.index(x[first_number : first_number + 3]) + 1
        else:
            first_num = x[first_number]
        if last_number in letter_numbers:
            # if x.count(x[last_number:last_number+3]):
            #     print(x)
            #     last_num = nums_short.index(x[last_number:last_number+3],nums_short.index(x[last_number:last_number+3])+1) + 1
            # else:
            last_num = nums_short.index(x[last_number : last_number + 3]) + 1
        else:
            last_num = x[last_number]

        # print(f"{first_num}{last_num}")
        z += int(f"{first_num}{last_num}")

    return z


print(f"PART 1: {part_1(data)}")
print(f"PART 2: {part_2(data)}")

# bad: 53864
# bad: 54057 changed letter numbers to look up
# bad: 54067 change letter numbers to look up from nums short
# good: 53855 changed the letter lookup from [:-3] to [:-2] (I wasn't checking all the way to the end..oops

#### BAD CODE that I tried to get the answer with or was trying to debug:


def get_first_number(seq: str):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    nums_short = ["one", "two", "thr", "fou", "fiv", "six", "sev", "eig", "nin"]
    # check letter numbers
    letter_numbers = []

    for num_idx, num in enumerate(nums):
        if num in seq:
            for l_idx, letter in enumerate(x[:-2]):
                if seq[l_idx : l_idx + 3] == nums_short[num_idx]:
                    letter_numbers.append(l_idx)

    for l_idx, l in enumerate(seq):
        if l.isnumeric() and l_idx < min(letter_numbers):
            return int(l)

    return nums[min(letter_numbers)]


def get_last_number(seq: str):
    letter_numbers = get_letter_numbers(seq)
    for l_idx, l in enumerate(seq):
        if l.isnumeric() and l_idx < min(letter_numbers):
            return int(l)

    return min(letter_numbers) + 1


def get_letter_numbers(seq: str):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    nums_short = ["one", "two", "thr", "fou", "fiv", "six", "sev", "eig", "nin"]
    # check letter numbers
    letter_numbers = []

    for num_idx, num in enumerate(nums):
        if num in seq:
            for l_idx, letter in enumerate(x[:-3]):
                if seq[l_idx : l_idx + 3] == nums_short[num_idx]:
                    letter_numbers.append(l_idx)
    return letter_numbers


def part_2_first_try(data):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    z = 0
    for x in data:
        print(x)
        f, s = None, None
        written_nums = {}
        for num_idx, num in enumerate(nums, 1):
            if num in x:
                written_nums[num] = {"idx": x.index(num), "value": num_idx}

        print(written_nums)

        for letter in x:
            if f is None:
                if x.index(letter) in [x["idx"] for x in written_nums.values()]:
                    f = [
                        n_f["value"]
                        for n_f in written_nums.values()
                        if n_f["idx"] == x.index(letter)
                    ][0]
                if letter.isnumeric():
                    f = int(letter)

        for letter in x[::-1]:
            if s is None:
                if x.index(letter) in [x["idx"] for x in written_nums.values()]:
                    s = [
                        n_s["value"]
                        for n_s in written_nums.values()
                        if n_s["idx"] == x.index(letter)
                    ][0]
            if letter.isnumeric():
                s = int(letter)

        if f is None and s is None:
            print("BROKEN")

        if f is None:
            f = s
        if s is None:
            s = f

        print(f"{f}{s}")
        z += int(f"{f}{s}")
    return z
