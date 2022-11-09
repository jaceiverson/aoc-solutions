"""https://adventofcode.com/2017/day/1"""


from helper import read

# READ INPUT
data = read("./2017/inputs/1.txt").strip()
# TEST INPUT
# data = read("./2017/inputs/1-test.txt").strip()
# data = "123425"
# PARSE INPUT

# PART 1
numbers = []
for idx, n in enumerate(data, 1):
    # check the last element
    if idx == len(data):
        if n == data[0]:
            numbers.append(int(n))
        break
    # we need to leave before this one

    elif n == data[idx]:
        numbers.append(int(n))


part_1_answer = sum(numbers)
print(f"PART 1: {part_1_answer}")
# wrong answer -> 1216 (right for someone else)
# 1223 I forgot to strip the string and it was causing it to not add the last digit

# PART 2
numbers = []
offset = len(data) // 2
for idx, n in enumerate(data):
    next_element = idx + offset
    if n == data[next_element % len(data)]:
        numbers.append(int(n))

part_2_answer = sum(numbers)
print(f"PART 2: {part_2_answer}")
