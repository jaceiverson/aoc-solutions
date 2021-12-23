"""https://adventofcode.com/2019/day/2"""

from helper import read

# READ INPUT
base_data = read("./2019/inputs/2.txt")
# TEST INPUT
# data = read("./2019/inputs/2-test.txt")
# PARSE INPUT
data = [int(x) for x in base_data.strip().split(",")]

# PART 1
# replace position 1 with the value 12 and replace position 2 with the value 2
data[1] = 12
data[2] = 2
counter = 0
while True:
    spot = counter * 4
    subsection = data[spot : spot + 4]
    # addition
    if subsection[0] == 1:
        data[subsection[3]] = data[subsection[1]] + data[subsection[2]]
    # multiplication
    elif subsection[0] == 2:
        data[subsection[3]] = data[subsection[1]] * data[subsection[2]]
    # break the process
    elif subsection[0] == 99:
        break
    counter += 1

part_1_answer = data[0]
print(f"PART 1: {part_1_answer}")
# TO LOW -> 250703
# forgot to change positions 1 & 2 as instructions said

# PART 2
# noun = pos 1, verb = pos 2
desired_output = 19690720
outputs = {}
for noun in range(100):
    for verb in range(100):
        # reset memory
        data = read("./2019/inputs/2.txt")
        data = [int(x) for x in data.strip().split(",")]
        if data == base_data:
            data[1] = noun
            data[2] = verb
            counter = 0
            while True:
                spot = counter * 4
                subsection = data[spot : spot + 4]
                # addition
                if subsection[0] == 1:
                    data[subsection[3]] = data[subsection[1]] + data[subsection[2]]
                # multiplication
                elif subsection[0] == 2:
                    data[subsection[3]] = data[subsection[1]] * data[subsection[2]]
                # break the process
                elif subsection[0] == 99:
                    break
                counter += 1

        else:
            print("NOT EQUAL, NOT RESET")

        outputs[f"{noun}-{verb}"] = data[0]

        if data[0] == desired_output:
            print(f"{noun=},{verb=},{data[0]=}")
            part_2_answer = 100 * noun + verb
            break


print(f"PART 2: {part_2_answer}")
# TO HIGH -> 980100 (99*99*100) oops
# TO HIGH -> 108800 (64*17*100)
# CORRECT -> 6417 (I read the instructions wrong, it is 100*noun+verb, I was doing multiplication before)
