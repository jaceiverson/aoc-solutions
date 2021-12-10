"""https://adventofcode.com/2021/day/9"""

from helper import read

# READ INPUT
data = read("./2021/inputs/9.txt")
# TEST INPUT
# data = read("./2021/inputs/9-test.txt")
# PARSE INPUT
data = data.strip().split('\n')
# make ints
data = [[int(x) for x in y] for y in data]


class Tubes():
    def __init__(self,map) -> None:
        self.map = map
        self.cell = (0,0)
    def check_vertical(self,r,c):
        pass
    def check_horizontal(self,r,c):
        val = self.map[r][c]
        # left edge
        if c == 0:
            if self.map[r][c+1] > val:
                # check vertically
                pass
        # right edge
        elif c == len(self.map[r])-1:
            if self.map[r][c-1] > val:
                # check vertically
                pass
        # middles
        else:
            if self.map[r][c-1] > val < self.map[r][c+1]:
                # check vertically
                pass
    def scan(self):
        for r_idx,row in enumerate(self.map):
            for c_idx,val in enumerate(row):
                self.check_horizontal(r_idx,c_idx)
# PART 1
# horizontal min check
h_mins = {x:[] for x in range(len(data))}
for r_idx,row in enumerate(data):
    for c_idx,val in enumerate(row):
        # left edge
        if c_idx == 0:
            if data[r_idx][c_idx+1] > val:
                # check vertically
                pass
        # right edge
        elif c_idx == len(row)-1:
            if data[r_idx][c_idx-1] > val:
                # check vertically
                pass
        # middles
        else:
            if data[r_idx][c_idx-1] > val < data[r_idx][c_idx+1]:
                # check vertically
                pass

# vertial min check
print(f"PART 1: {part_1_answer}")

# PART 2

print(f"PART 2: {part_2_answer}")
