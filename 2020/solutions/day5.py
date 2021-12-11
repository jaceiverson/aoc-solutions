"""https://adventofcode.com/2020/day/5"""

from helper import read

# READ INPUT
data = read("./2020/inputs/5.txt")

import pandas as pd
import numpy as np


def five_a():
    with open("./2020/inputs/5.txt") as f:
        tickets = f.read()
    tickets = tickets.split("\n")
    row_num = []
    seat_num = []
    for x in tickets:
        if x != "":
            row_list = x[:7]
            seat_list = x[7:]

            row_num.append(row(row_list, 127, 0))
            seat_num.append(seat(seat_list, 7, 0))

    df = pd.DataFrame([tickets, row_num, seat_num])
    df = df.T
    df = df.dropna()
    df.columns = ["Ticket", "row_num", "seat_num"]
    df["id"] = (df["row_num"] * 8) + df["seat_num"]
    # to solve the problem
    # return df['id'].max()
    # for help on five_b
    return df


def five_b():
    df = five_a()
    range_ids = np.arange(df["id"].min(), df["id"].max(), 1)
    for x in range_ids:
        if x not in df["id"].values:
            return x


def row(letter_list, high, low):

    mid_point = high - ((high - low) / 2)

    if letter_list[0] == "F":
        # lower half
        if mid_point.is_integer():
            high = mid_point
        else:
            high = mid_point - 0.5
    elif letter_list[0] == "B":
        # back half
        if mid_point.is_integer():
            low = mid_point
        else:
            low = mid_point + 0.5

    if high == low:
        return high
    else:
        return row(letter_list[1:], high, low)


def seat(letter_list, high, low):

    mid_point = high - ((high - low) / 2)

    if letter_list[0] == "L":
        # lower half
        if mid_point.is_integer():
            high = mid_point
        else:
            high = mid_point - 0.5
    elif letter_list[0] == "R":
        # back half
        if mid_point.is_integer():
            low = mid_point
        else:
            low = mid_point + 0.5

    if high == low:
        return high
    else:
        return seat(letter_list[1:], high, low)


if __name__ == "__main__":
    print(five_a())
    print(five_b())
