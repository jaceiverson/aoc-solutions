"""https://adventofcode.com/2018/day/4"""

from pandas.tseries.offsets import MonthOffset
from helper import read
import datetime as dt
import pandas as pd

# READ INPUT
data = read("./2018/inputs/4.txt")
# TEST INPUT
# data = read("./2018/inputs/4-test.txt")
# PARSE INPUT
data = data.strip().split('\n')
log = {"DATE":[],"GUARD":[],"NOTE":[]}
for line in data:
    # LOG TIME
    str_date,log_detail = line.split('] ')
    log_date = dt.datetime.strptime(str_date[1:],"%Y-%m-%d %H:%M")
    log["DATE"].append(log_date)
    # if GUARD in log
    if "guard" in log_detail.lower():
        guard_id = ''.join(filter(lambda i: i.isdigit(), log_detail))
        log["NOTE"].append("start shift")
    elif "asleep" in log_detail.lower():
        log["NOTE"].append("asleep")
    elif "wakes" in log_detail.lower():
        log["NOTE"].append("awake")
    
    log["GUARD"].append(guard_id)

# CONVERT TO DF for simplicity?
df = pd.DataFrame(log)
df = df.sort_values('DATE')
df["TIME"] = (df['DATE'] - df["DATE"].shift())
df["MIN"] = df["TIME"].dt.components["minutes"]
df["NEW GUARD"] = None
# ADD in the correct guard (the log is messed up)
for idx,row in df.iterrows():
    if "start" in row["NOTE"]:
        current_guard = row["GUARD"]
    df.loc[idx,"NEW GUARD"] = current_guard
# MOVE the durration to the correct row (shift up one)
df["DURATION"] = df["MIN"].shift(-1)

# PART 1
# we will have a dict for count of mins slept
sleep_chart = {key:0 for key in range(60)}
# Find which guard has the largest duration
most_sleep_id = df.groupby("NEW GUARD").sum()["DURATION"].idxmax()
# Get the sleep/wake logs of just that guard
most_sleep_log = df.loc[(df["NEW GUARD"]==most_sleep_id) & (~df["NOTE"].str.contains("start"))]
# find which minutes were most slept
for idx,row in most_sleep_log.iterrows():
    if row["NOTE"] == "asleep":
        start_min = row["DATE"].minute
        for x in range(start_min,int(row["DURATION"])):
            sleep_chart[x] += 1

most_slept_min = [key for key,value in sleep_chart.items() if value == max(sleep_chart.values())][0]
part_1_answer = most_slept_min * int(most_sleep_id)
print(f"PART 1: {part_1_answer}")
# TO LOW -> 9980


# PART 2

part_2_answer = None
print(f"PART 2: {part_2_answer}")
