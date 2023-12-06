"""https://adventofcode.com/2023/day/6"""

from aoc_util import read

# MAIN INPUT
data = read("./2023/inputs/6.txt").strip().split("\n")


# TEST INPUT
# data = read("./2023/inputs/6-test.txt").strip().split("\n")
# EXAMPLE INPUT
# data = read("./2023/inputs/6-test-e.txt").strip().split("\n")
# PARSE INPUT
def parse(data):
    time, dist = data
    _, time = time.split(": ")
    time = list(map(int, time.split()))
    _, dist = dist.split(": ")
    dist = list(map(int, dist.split()))
    return time, dist


def calculate_distance(time_held: int, time_left: int) -> int:
    return time_held * time_left


def part_1(data: list):
    time, dist = parse(data)
    total = 1
    for idx_, t in enumerate(time):
        v = 0
        for held_time in range(t + 1):
            if calculate_distance(held_time, time[idx_] - held_time) > dist[idx_]:
                v += 1
        total *= v
        # print(f"{v=}")
        # print(f"{t=}")

    return total


# PART 1
print(f"PART 1: {part_1(data)}")


# PART 2
def part_2(data: list):
    time, dist = parse(data)
    time = int("".join(str(x) for x in time))
    dist = int("".join(str(x) for x in dist))
    v = 0
    for held_time in range(time + 1):
        if calculate_distance(held_time, time - held_time) > dist:
            v += 1
    return v


print(f"PART 2: {part_2(data)}")
