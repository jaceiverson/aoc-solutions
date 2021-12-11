"""https://adventofcode.com/2020/day/2"""

import numpy as np
import pandas as pd


def two_a(df):
    """
    Probably a better way to do this one.
    :return:
    """
    df[["min", "max"]] = df[0].str.split("-", expand=True)
    df["letter"] = df[1].str.split(":", expand=True)[0]
    # df['letter_c']=df[2],df['letter'].apply(lambda x,y : x.str.count(y))
    df["letter_c"] = None
    for index, rows in df.iterrows():
        df["letter_c"][index] = rows[2].count(rows["letter"])
    cond = [(df["letter_c"] >= df["min"]) & (df["letter_c"] <= df["max"])]

    values = ["Pass"]
    df["good"] = np.select(cond, values)

    return df["good"].value_counts()["Pass"]


def two_b(df):
    """
    Again, I think there is a better way to do it, but it is done.
    :return:
    """
    df["first"] = df[0].str.split("-", expand=True)[0].astype(int)
    df["second"] = df[0].str.split("-", expand=True)[1].astype(int)
    df["char"] = df[1].str.split(":", expand=True)[0]
    # df['char_pos']=[pos for pos, char in enumerate(df[2]) if char == df['char']]
    df["first_match"] = None
    df["second_match"] = None

    for index, rows in df.iterrows():
        df["first_match"][index] = rows[2][rows["first"] - 1] == rows["char"]
        df["second_match"][index] = rows[2][rows["second"] - 1] == rows["char"]

    cond = [(df["first_match"] != df["second_match"])]
    value = ["Pass"]
    df["good"] = np.select(cond, value)

    return df["good"].value_counts()["Pass"]


if __name__ == "__main__":
    # read in file
    df = pd.read_csv("./2020/inputs/2.txt", sep=" ", header=None)
    print(two_a(df))
    print(two_b(df))
