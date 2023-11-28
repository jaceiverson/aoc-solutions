"""https://adventofcode.com/2015/day/8"""

from aoc_util import read
import re

# READ INPUT
data = read("./2015/inputs/8.txt").strip().split("\n")
# TEST INPUT
data = read("./2015/inputs/8-test.txt").strip().split("\n")
# PARSE INPUT
def get_chars(line: str, output: bool = True) -> int:
    if output:
        print(re.escape(line))
    # replace the hexidecimal chars with a 1 (one character)
    line = re.sub(r"\\x[0-9a-f]{2}", "1", re.escape(line), re.IGNORECASE)
    # replace the slashes
    line = re.sub(r"\\\\", r"\\", line)
    if output:
        print(line)
    # get the charcater count
    return len(line) - 2


# PART 1
new_data = []
output = True
for line in data:
    characters = get_chars(line, output)
    # output
    if output:
        print(f"{characters=}")
        print(f"{len(line)}")
    new_data.append(characters)

code_characters = sum(len(x) for x in data)
part_1_answer = code_characters - sum(new_data)
print(f"PART 1: {part_1_answer}")
# TO HIGH -> 1477
# TO HIGH -> 1469 (changed to re.IGNORECASE)
# TO LOW -> 971 (changed \\ to have 1 character)
# NOT RIGHT -> 1320 (changed \\ to also have re.IGRNOECASE, not sure why this changed)
# NOT RIGHT -> 1438 (change the regex to r"\\" but still nothing)
# PART 2

part_2_answer = None
print(f"PART 2: {part_2_answer}")


def tests():
    test_data_from_reddit = {
        '"yrbajyndte\\rm"': 13,
        '"qsmzhnx\\""': 8,
        '"axoufpnbx\\ao\x61pfj\b""': 18,
        '"dz\\ztawzdjy"': 11,
        '"\dgazthrphbshdo\\vuqoiy\\"""': 23,
        '"dlnmptzt\\zahwpylc\\b\gmslrqysk""': 29,
        '"dwxuis\xa5wdkx\\z\admgnoddpgkt\\zs""': 29,
    }

    python_strings = {
        "\a": 2,
        "\b": 2,
        "\f": 2,
        "\n": 2,
        "\r": 2,
        "\t": 2,
        "\v": 2,
    }

    for l, v in test_data_from_reddit.items():
        print(f"{get_chars(l)=}\n{v=}")
        print(f"{re.escape(l)=}")
