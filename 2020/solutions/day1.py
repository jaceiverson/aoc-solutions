"""https://adventofcode.com/2020/day/1"""

from aoc_util import read

import pandas as pd


def one_a(df):
    for x in df[0]:
        for y in df[0]:
            if x != y:
                if x + y == 2020:
                    return x * y, (x, y)


def one_b(df):
    for x in df[0]:
        for y in df[0]:
            for z in df[0]:
                if x != y and x != z:
                    if x + y + z == 2020:
                        return x * y * z, (x, y, z)


if __name__ == "__main__":
    # read file in
    df = pd.read_csv("./2020/inputs/1.txt", sep=" ", header=None)
    print(one_a(df))
    print(one_b(df))
