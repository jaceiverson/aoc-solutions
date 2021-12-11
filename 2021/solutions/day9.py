"""https://adventofcode.com/2021/day/9"""

from helper import read

# READ INPUT
data = read("./2021/inputs/9.txt")
# TEST INPUT
#data = read("./2021/inputs/9-test.txt")
# PARSE INPUT
data = data.strip().split('\n')
# make ints
data = [[int(x) for x in y] for y in data]


class Tubes():
    def __init__(self,map) -> None:
        self.map = map
        self.cell = (0,0)
        self.low_points = {}
        self.h_lows = []
        self.v_lows = []

    def __str__(self):
        for row in self.map:
            print(row)

    def reset(self):
        self.cell = (0,0)
        self.low_points = {}
        self.h_lows = []
        self.v_lows = []

    def check_vertical(self):
        """
        TRUE = cell is a v low point
        FALSE = cell is not a v low point
        """
        r,c = self.cell
        val = self.map[r][c]
        # far left column
        if r==0:
            if self.map[r+1][c] > val:
                self.v_lows.append(self.cell)
                return True
        # far right column
        elif r==len(self.map)-1:
            if self.map[r-1][c] > val:
                self.v_lows.append(self.cell)
                return True
        # middle columns
        else:
            if self.map[r-1][c] > val < self.map[r+1][c]:
                self.v_lows.append(self.cell)
                return True
        # default is false
        return False

    def check_horizontal(self):
        """
        TRUE = cell is a h low point
        FALSE = cell is not a h low point
        """
        # get the row and col values
        r,c = self.cell
        val = self.map[r][c]
        # left edge
        if c == 0:
            # if cell to the right is >
            if self.map[r][c+1] > val:
                self.h_lows.append(self.cell)
                return self.check_vertical()
        # right edge
        elif c == len(self.map[r])-1:
            if self.map[r][c-1] > val:
                self.h_lows.append(self.cell)
                return self.check_vertical()
        # middles
        else:
            if self.map[r][c-1] > val < self.map[r][c+1]:
                self.h_lows.append(self.cell)
                return self.check_vertical()
        # default is False
        return False

    def _check_low_point(self):
        return self.check_horizontal()

    def low_point_sum(self):
        return sum(self.low_points.values()) + len(self.low_points.values())

    def low_point_output(self):
        print(f"{self.h_lows=}")
        print(f"{self.v_lows=}")
        print(f"{self.low_points=}")

    def scan_lowpoints(self):
        for r_idx,row in enumerate(self.map):
            for c_idx,val in enumerate(row):
                self.cell = (r_idx,c_idx)
                if self._check_low_point():
                    self.low_points[self.cell] = val
        return self.low_points

    def check_basins(self,cell,current_basin):
        r,c=cell
        # scan the 8 surrounding cells
        for row_offset in range(-1,2,1):
            for col_offset in range(-1,2,1):
                if abs(row_offset)!=abs(col_offset):
                    # if the offset is in bounds
                    if (0 <= r+row_offset < len(self.map)) and (0 <= c+col_offset < len(self.map[0])):
                        # if the number is not a 9 and not already in the list, scan that cell
                        if self.map[r+row_offset][c+col_offset] != 9 and (r+row_offset,c+col_offset) not in current_basin:
                            current_basin.append((r+row_offset,c+col_offset))
                            self.check_basins((r+row_offset,c+col_offset),current_basin)


        return current_basin

    def scan_basins(self):
        # get all the lowpoints
        # basin's ided by their low point
        self.basins = {key:[] for key in self.scan_lowpoints().keys()}
        for low_point in self.basins.keys():
                self.basins[low_point] = self.check_basins(low_point,[low_point])
        
        return self.basins

    def top_3_basins(self):
        basin1=0
        basin2=0
        basin3=0
        for key,value in self.basins.items():
            l = len(value)
            if l > basin1:
                basin1,basin2,basin3 = l,basin1,basin2
            elif l > basin2:
                basin2,basin3 = l,basin2
            elif l > basin3:
                basin3 = l

        return basin3*basin2*basin1
        
    def basins_output(self):
        print(f"{self.basins=}")

    def basin_length(self):
        for key,value in self.basins.items():
            print(f"{key}:{len(value)}")

# PART 1
path = Tubes(data)
low_points = path.scan_lowpoints()
# path.low_point_output()
part_1_answer = path.low_point_sum()
print(f"PART 1: {part_1_answer}")

# PART 2
path = Tubes(data)
basins = path.scan_basins()
# path.basin_length()
part_2_answer = path.top_3_basins()
print(f"PART 2: {part_2_answer}")
