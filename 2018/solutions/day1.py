"""https://adventofcode.com/2018/day/1"""

from helper import read

# READ INPUT
data = read("./2018/inputs/1.txt")
# TEST INPUT
# data = read("./2018/inputs/1-test.txt")
# PARSE INPUT
data = data.strip().split("\n")
# PART 1
freq = 0
freq_list = []
part_2_answer = None
for op in data:
    opperator = op[0]
    num = int(op[1:])
    if opperator == "+":
        freq += num
    elif opperator == "-":
        freq -= num

part_1_answer = freq
print(f"PART 1: {part_1_answer}")

# PART 2
# works, but is slow
def repeat_freq(freq_list=None, freq=0):
    if freq_list is None:
        freq_list = []
    for op in data:
        opperator = op[0]
        num = int(op[1:])
        if opperator == "+":
            freq += num
        elif opperator == "-":
            freq -= num
        if freq in freq_list:
            return freq
        freq_list.append(freq)
    return repeat_freq(freq_list, freq)


part_2_answer = repeat_freq()
print(f"PART 2: {part_2_answer}")
