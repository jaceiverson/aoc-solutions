"""https://adventofcode.com/2020/day/4"""

import pandas as pd
import re


def four_a():
    with open("./2020/inputs/4.txt", "r") as f:
        passports = f.read()

    passports = passports.replace("\n", " ").split("  ")
    df = pd.DataFrame(columns=["iyr", "hgt", "byr", "cid", "pid", "eyr", "hcl", "ecl"])
    req = ["iyr", "hgt", "byr", "pid", "eyr", "hcl", "ecl"]
    # clean indivdual
    for x in passports:
        temp = pd.DataFrame(x.split(" "))
        temp = temp[0].str.split(":", expand=True).T
        temp.columns = temp.iloc[0]
        temp = temp.drop(0)

        df = df.append(temp)

    # want to know all non NA values for the req columns
    return df[req].dropna()


def four_b():
    # requirements
    byr_min = 1920
    byr_max = 2002
    iyr_min = 2010
    iyr_max = 2020
    eyr_min = 2020
    eyr_max = 2030
    h_cm_max = 193
    h_cm_min = 150
    h_in_max = 76
    h_in_min = 59
    # color have '#' followed by 6 valid digits
    # re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', str)
    e_color_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    # p_num=re.search(r'\d{0,9}',str)

    df = four_a()
    df[["byr", "iyr", "eyr"]] = df[["byr", "iyr", "eyr"]].astype(int)

    df = df.loc[(df["byr"] >= byr_min) & (df["byr"] <= byr_max)]
    df = df.loc[(df["iyr"] >= iyr_min) & (df["iyr"] <= iyr_max)]
    df = df.loc[(df["eyr"] >= eyr_min) & (df["eyr"] <= eyr_max)]
    cm = df.loc[df["hgt"].str.contains("cm")]
    inch = df.loc[df["hgt"].str.contains("in")]
    cm = cm.loc[
        (cm["hgt"].str.split("c", expand=True)[0].astype(int) >= h_cm_min)
        & (cm["hgt"].str.split("c", expand=True)[0].astype(int) <= h_cm_max)
    ]
    inch = inch.loc[
        (inch["hgt"].str.split("i", expand=True)[0].astype(int) >= h_in_min)
        & (inch["hgt"].str.split("i", expand=True)[0].astype(int) <= h_in_max)
    ]
    df = cm.append(inch)
    df["color_valid"] = df["hcl"].apply(
        lambda x: re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", x)
    )
    df = df.dropna(subset=["color_valid"])

    df = df.loc[df["ecl"].isin(e_color_list)]

    # pid
    df = df.loc[df["pid"].str.len() == 9]
    df["pid_valid"] = df["pid"].apply(lambda x: re.search(r"^\d{0,9}$", x))
    df = df.dropna(subset=["pid_valid"])

    return df


if __name__ == "__main__":
    print(four_a())
    print(four_b())
