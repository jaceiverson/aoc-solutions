"""https://adventofcode.com/2016/day/4"""

from aoc_util import read
from collections import Counter
from string import ascii_lowercase as alphabet

# READ INPUT
data = read("./2016/inputs/4.txt").strip().split("\n")


# TEST INPUT
# data = read("./2016/inputs/4-test.txt").strip().split("\n")
# PARSE INPUT
def get_room_elements(room: str) -> tuple:
    name, check_sum = room.split("[")
    name = name.split("-")
    return (
        "".join(name[:-1]),
        int(name[-1]),
        check_sum[:-1],
    )


def is_valid_room(check_sum: str, char_count: list) -> bool:
    return check_sum == "".join([x[0] for x in char_count[:5]])


# PART 1
sector_id_sum = 0
for room in data:
    name, number, check_sum = get_room_elements(room)
    # get each element count
    char_count = list(Counter(name[::-1]).items())
    # sort alphabetically
    char_count.sort(key=lambda x: x[0])
    # sort by number
    char_count.sort(key=lambda x: x[1], reverse=True)

    if is_valid_room(check_sum, char_count):
        sector_id_sum += number

part_1_answer = sector_id_sum
print(f"PART 1: {part_1_answer}")


def rotate_letter(letter: str, room_id: int) -> str:
    if letter in alphabet:
        starting_index = alphabet.index(letter)
        return alphabet[(starting_index + room_id) % 26]
    return letter


def is_desired_room(room_name: str) -> bool:
    return "object" in room_name


# PART 2
for room in data:
    name, number, check_sum = get_room_elements(room)
    # get each element count
    char_count = list(Counter(name[::-1]).items())
    # sort alphabetically
    char_count.sort(key=lambda x: x[0])
    # sort by number
    char_count.sort(key=lambda x: x[1], reverse=True)

    if is_valid_room(check_sum, char_count):
        new_room = "".join([rotate_letter(x, number) for x in name])
        if is_desired_room(new_room):
            # print(f"{number=},{new_room=}")
            part_2_answer = number

print(f"PART 2: {part_2_answer}")
