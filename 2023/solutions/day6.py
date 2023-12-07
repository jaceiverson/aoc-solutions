"""https://adventofcode.com/2023/day/6"""

from aoc_util import read
from aoc_util.helper import mytime

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


def optimize(time: int, dist: int) -> int:
    races = 0
    to_check = list(range(time // 2, -1, -1))
    while calculate_distance(to_check[races], time - to_check[races]) > dist:
        races += 1
    if time % 2 == 0:
        return (races * 2) - 1
    return races * 2


@mytime
def part_1(data: list):
    time, dist = parse(data)
    total = 1
    for idx_, t in enumerate(time):
        v = 0
        for held_time in range(t + 1):
            if calculate_distance(held_time, time[idx_] - held_time) > dist[idx_]:
                v += 1
        total *= v
    return total


@mytime
def part_1_sorcery(data: list):
    time, dist = parse(data)
    total = 1
    for idx_, t in enumerate(time):
        v = sum(
            1
            for held_time in range(t + 1)
            if calculate_distance(held_time, time[idx_] - held_time) > dist[idx_]
        )
        total *= v
    return total


@mytime
def part_1_new(data: list):
    time, dist = parse(data)
    total = 1
    for t, d in zip(time, dist):
        total *= optimize(t, d)
    return total


# PART 1
print(f"PART 1: {part_1(data)}")  # 23458 ns
print(f"PART 1_NEW: {part_1_new(data)}")  # 18583 ns (20% faster)
print(f"PART 1_SORCERY: {part_1_sorcery(data)}")  # 25458 ns (8% slower) interesting


# PART 2
@mytime
def part_2(data: list):
    time, dist = parse(data)
    time = int("".join(str(x) for x in time))
    dist = int("".join(str(x) for x in dist))
    v = 0
    for held_time in range(time + 1):
        if calculate_distance(held_time, time - held_time) > dist:
            v += 1
    return v


@mytime
def part_2_sorcery(data: list):
    time, dist = parse(data)
    time = int("".join(str(x) for x in time))
    dist = int("".join(str(x) for x in dist))
    return sum(
        calculate_distance(held_time, time - held_time) > dist
        for held_time in range(time + 1)
    )


@mytime
def part_2_new(data: list):
    time, dist = parse(data)
    time = int("".join(str(x) for x in time))
    dist = int("".join(str(x) for x in dist))
    return optimize(time, dist)


print(f"PART 2: {part_2(data)}")  # 2691266875 ns
print(f"PART 2_NEW: {part_2_new(data)}")  # 1480963792 ns (45% faster)
print(f"PART 2_SORCERY: {part_2_sorcery(data)}")  # 2853478834 ns (6% slower)

"""
Added some of the changes that sorcery recommended. They 
ended up being slower than my original code and a little
harder to read as well. Even if they are more "pythonic" 
I prefer both solves I did to their solution.
"""
