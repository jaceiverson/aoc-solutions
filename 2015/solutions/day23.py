"""https://adventofcode.com/2015/day/23"""


from aoc_util import read

# READ INPUT
data = read("./2015/inputs/23.txt").strip().split("\n")
# TEST INPUT
# data = read("./2015/inputs/23-test.txt").strip().split("\n")
# PARSE INPUT

# PART 1
def run_registers(a: int, b: int) -> int:
    idx = 0
    while idx >= 0 and idx < len(data):
        line = data[idx]
        # print(f"{a=},{b=},{idx=},{line=}")
        if "inc" in line:
            _, register = line.split()
            if register == "a":
                a += 1
            else:
                b += 1
        elif "hlf" in line:
            _, register = line.split()
            if register == "a":
                a = a / 2
            else:
                b = b / 2
        elif "tpl" in line:
            _, register = line.split()
            if register == "a":
                a = a * 3
            else:
                b = b * 3
        elif "jmp" in line:
            _, inc = line.split(" ")
            if inc.startswith("+"):
                idx += int(inc[1:]) - 1
            elif inc.startswith("-"):
                idx -= int(inc[1:]) + 1
        elif "jie" in line:
            register, inc = line.split(", ")
            temp = a if register[-1] == "a" else b
            if int(temp % 2 == 0):
                if inc.startswith("+"):
                    idx += int(inc[1:]) - 1
                elif inc.startswith("-"):
                    idx -= int(inc[1:]) + 1
        elif "jio" in line:
            register, inc = line.split(", ")
            temp = a if register[-1] == "a" else b
            if int(temp == 1):
                if inc.startswith("+"):
                    idx += int(inc[1:]) - 1
                elif inc.startswith("-"):
                    idx -= int(inc[1:]) + 1
        idx += 1

    return b


part_1_answer = run_registers(0, 0)
print(f"PART 1: {part_1_answer}")

# PART 2

part_2_answer = run_registers(1, 0)
print(f"PART 2: {part_2_answer}")
