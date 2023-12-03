"""https://adventofcode.com/2023/day/2"""

from aoc_util import read

# READ INPUT
data = read("./2023/inputs/2.txt").strip().split("\n")
# TEST INPUT
# data = read("./2023/inputs/2-test.txt").strip().split("\n")
# PARSE INPUT
COLORS = ["red", "green", "blue"]
LIMIT = [12, 13, 14]


def is_valid_pull(pull: str):
    data = pull.split(", ")
    for type_ in data:
        score, color = type_.split(" ")
        if int(score) > LIMIT[COLORS.index(color)]:
            return False
    return True


def process_line(line: str):
    # total reset for each game
    pull_results = []
    # parse the line
    game_id, results = line.split(": ")
    _, game_id = game_id.split(" ")
    pulls = results.split("; ")
    for p in pulls:
        pull_results.append(is_valid_pull(p))

    if all(pull_results):
        return int(game_id)

    return 0


def part_1(data):
    return sum(process_line(line) for line in data)


# PART 1
part_1_answer = part_1(data)
print(f"PART 1: {part_1_answer}")
# 231 not right


# PART 2
def is_valid_pull_part_2(p, maxes):
    pull_data = p.split(", ")
    for type_ in pull_data:
        score, color = type_.split(" ")
        if int(score) > maxes[COLORS.index(color)]:
            maxes[COLORS.index(color)] = int(score)
    return maxes


def process_line_part_2(line: str):
    # total reset for each game
    pull_results = []
    # parse the line
    game_id, results = line.split(": ")
    _, game_id = game_id.split(" ")
    pulls = results.split("; ")
    maxes = [0, 0, 0]
    for p in pulls:
        maxes = is_valid_pull_part_2(p, maxes)

    return maxes[0] * maxes[1] * maxes[2]


def part_2(data):
    total = 0
    for line in data:
        total += process_line_part_2(line)
    return total


part_2_answer = part_2(data)
print(f"PART 2: {part_2_answer}")
