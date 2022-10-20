"""https://adventofcode.com/2018/day/4"""


from helper import read
import datetime as dt
import re

# READ INPUT
data = read("./2018/inputs/4.txt")
# TEST INPUT
# data = read("./2018/inputs/4-test.txt")
# PARSE INPUT
data = data.strip().split("\n")

# ATTEMPT 1
def old_method():
    import pandas as pd

    log = {"DATE": [], "GUARD": [], "NOTE": []}
    for line in data:
        # LOG TIME
        str_date, log_detail = line.split("] ")
        log_date = dt.datetime.strptime(str_date[1:], "%Y-%m-%d %H:%M")
        log["DATE"].append(log_date)
        # if GUARD in log
        if "guard" in log_detail.lower():
            guard_id = "".join(filter(lambda i: i.isdigit(), log_detail))
            log["NOTE"].append("start shift")
        elif "asleep" in log_detail.lower():
            log["NOTE"].append("asleep")
        elif "wakes" in log_detail.lower():
            log["NOTE"].append("awake")

        log["GUARD"].append(guard_id)

    # CONVERT TO DF for simplicity?
    df = pd.DataFrame(log)
    df = df.sort_values("DATE")
    df["TIME"] = df["DATE"] - df["DATE"].shift()
    df["MIN"] = df["TIME"].dt.components["minutes"]
    df["NEW GUARD"] = None
    # ADD in the correct guard (the log is messed up)
    for idx, row in df.iterrows():
        if "start" in row["NOTE"]:
            current_guard = row["GUARD"]
        df.loc[idx, "NEW GUARD"] = current_guard
    # MOVE the durration to the correct row (shift up one)
    df["DURATION"] = df["MIN"].shift(-1)

    # PART 1
    # we will have a dict for count of mins slept
    sleep_chart = {key: 0 for key in range(60)}
    # Find which guard has the largest duration
    most_sleep_id = df.groupby("NEW GUARD").sum()["DURATION"].idxmax()
    # Get the sleep/wake logs of just that guard
    most_sleep_log = df.loc[
        (df["NEW GUARD"] == most_sleep_id) & (~df["NOTE"].str.contains("start"))
    ]
    # find which minutes were most slept
    for idx, row in most_sleep_log.iterrows():
        if row["NOTE"] == "asleep":
            start_min = row["DATE"].minute
            for x in range(start_min, int(row["DURATION"])):
                sleep_chart[x] += 1

    most_slept_min = [
        key for key, value in sleep_chart.items() if value == max(sleep_chart.values())
    ][0]
    part_1_answer = most_slept_min * int(most_sleep_id)


# ATTEMPT 2
def new(data):
    """create a list of tuples from string, convert dates to dt.datetimes"""
    log_pattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (.*)"
    guard_number_pattern = r"#(\d*) (\D*)$"
    data.sort()
    log = []
    for d in data:
        if line_item := re.search(log_pattern, d):
            date = dt.datetime.strptime(line_item.groups()[0], "%Y-%m-%d %H:%M")
            msg = line_item.groups()[1]
            if guard := re.search(guard_number_pattern, msg):
                guard, msg = guard.groups()

            log.append((date, guard, msg))

    # sort values - defaults to sort by first element in tuple (date)
    log.sort()

    # create a dictionary for each guard,
    # values = {x:0 for x in range(60)} or a dictionary from 0 to 59 to indicate minutes
    sleepy = {guard[1]: {x: 0 for x in range(60)} for guard in log if guard[1]}

    # calculate the time asleep
    sleep_start = None
    sleep_end = None
    for l in log:
        # live_guard
        if l[1] is not None:
            active_guard = l[1]
        # falls alseep
        if l[2] == "falls asleep":
            sleep_start = l[0].minute
        # wakes up
        elif l[2] == "wakes up":
            sleep_end = l[0].minute
            # this is where my issue was. I was checking again
            # rather than when 'wake up' happens, trigger the calculations
            # save results
            for sleepy_time in range(sleep_start, sleep_end):
                sleepy[active_guard][sleepy_time] += 1
            sleep_start = None
            sleep_end = None

    # max total miniutes slept
    most_sleep = 0
    # guard who slept the most
    max_guard = None
    # of the guard, the minute
    minute_max = 0
    idx_max = 0
    for guard, sleep_log in sleepy.items():
        # print(f"{guard}: {sum(sleep_log.values())}")
        if sum(sleep_log.values()) > most_sleep:
            most_sleep = sum(sleep_log.values())
            max_guard = guard
            idx_max = 0
            for minute, sleep in sleep_log.items():
                if sleep >= minute_max:
                    minute_max = sleep
                    idx_max = minute

    return int(max_guard) * idx_max, sleepy


# ATTEMPT 3
def reddit(data):
    """
    Thanks to reddit, I was able to get the correct answer,
    then investigate my code to find where the issue was
    https://www.reddit.com/r/adventofcode/comments/a2xef8/comment/eb1w7xy/?utm_source=share&utm_medium=web2x&context=3
    """
    import collections
    import dateutil

    guards = collections.defaultdict(list)
    times = collections.defaultdict(int)

    for line in sorted(data):
        time, action = line.split("] ")

        time = dateutil.parser.parse(time[1:])

        if action.startswith("Guard"):
            guard = int(action.split()[1][1:])
        elif action == "falls asleep":
            start = time
        elif action == "wakes up":
            end = time
            guards[guard].append((start.minute, end.minute))
            times[guard] += (end - start).seconds

    (guard, time) = max(times.items(), key=lambda i: i[1])
    (minute, count) = max(
        [
            (minute, sum(1 for start, end in guards[guard] if start <= minute < end))
            for minute in range(60)
        ],
        key=lambda i: i[1],
    )

    print("part 1:", guard * minute)

    (guard, minute, count) = max(
        [
            (
                guard,
                minute,
                sum(1 for start, end in guards[guard] if start <= minute < end),
            )
            for minute in range(60)
            for guard in guards
        ],
        key=lambda i: i[2],
    )

    print("part 2:", guard * minute)


part_1_answer, sleep_chart = new(data)
print(f"PART 1: {part_1_answer}")
# TO LOW -> 9980
# TO LOW -> 9481
# TO LOW -> 2980
# TO LOW -> 5960
# INCORRECT -> 13662
# INCORRECT -> 9773
# CORRECT -> 21956

# PART 2
def part_2(data):
    min_most_slept = None
    times_asleep_max = 0
    guard_in_question = None
    for guard, sleep_log in sleep_chart.items():
        for minute, times_asleep in sleep_log.items():
            if times_asleep > times_asleep_max:
                times_asleep_max = times_asleep
                min_most_slept = minute
                guard_in_question = guard

    return int(guard_in_question) * min_most_slept


part_2_answer = part_2(data)
print(f"PART 2: {part_2_answer}")
