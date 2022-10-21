"""https://adventofcode.com/2015/day/14"""

from helper import read

# READ INPUT
data = read("./2015/inputs/14.txt").strip().split("\n")
# TEST INPUT
# data = read("./2015/inputs/14-test.txt").strip().split("\n")
# PARSE INPUT


def distance(race_time, speed, move_time, rest_time) -> int:
    # period is the seconds a reindeer can move plus how long it must rest
    period = move_time + rest_time
    # full_periods is the count of periods that exist in the given race time
    full_periods = race_time // period
    # remaining_seconds is how many seconds are left over
    remaining_seconds = race_time - full_periods * period
    # remaining_move_seconds
    remaining_move_seconds = min(remaining_seconds, move_time)
    # addtional distance
    additional_distance = speed * remaining_move_seconds
    # total distance traveled
    return (full_periods * (speed * move_time)) + additional_distance


def get_all_distances(data, race_time):
    results = {}
    for line in data:
        parsed = line.split()
        name = parsed[0]
        speed = int(parsed[3])
        move_time = int(parsed[6])
        rest_time = int(parsed[-2])
        results[name] = distance(race_time, speed, move_time, rest_time)
    return results


# PART 1
race_time = 2503
p1_results = get_all_distances(data, race_time)
part_1_answer = max(p1_results.values())
print(f"PART 1: {part_1_answer}")
# TO HIGH -> 2720 -> forgot to subtract full_periods from race_time

# PART 2
points = {x.split()[0]: 0 for x in data}
# race_time = 1000
for race_second in range(1, race_time + 1):
    second_results = get_all_distances(data, race_second)
    winners = [
        k for k, v in second_results.items() if v == max(second_results.values())
    ]
    for w in winners:
        points[w] += 1
part_2_answer = max(points.values())
print(f"PART 2: {part_2_answer}")
