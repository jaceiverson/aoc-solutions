"""https://adventofcode.com/2018/day/3"""

from typing import overload
from aoc_util import read

# READ INPUT
data = read("./2018/inputs/3.txt")
# TEST INPUT
# data = read("./2018/inputs/3-test.txt")
# PARSE INPUT
data = data.strip().split("\n")


class Grid:
    def __init__(self) -> None:
        # will be 3D list
        self.grid = []
        # height
        self.h = 0
        # width
        self.w = 0
        # grid empty squares
        self.empty_squares = 0

    def show(self) -> None:
        """prints the grid"""
        for row in self.grid:
            print(row)

    def dims(self) -> tuple[int, int]:
        """returns the height (rows) and width (cols) of the grid"""
        return self.h, self.w

    def new_dims(self, new_dims: tuple[int, int]) -> None:
        """
        Accepts a tuple of dims (h,w) and
        will add rows/cols to fit new maximums
        """
        # unpack the elements
        nh, nw = new_dims
        ch, cw = self.dims()
        try:
            # calulate how many rows/cols to add
            rows_to_add = int(nh) - ch
            cols_to_add = int(nw) - cw
            # if those are above 0, we will add them in
            if rows_to_add > 0:
                self._add_rows(rows_to_add)
            if cols_to_add > 0:
                self._add_cols(cols_to_add)
        except TypeError:
            # if a type error is thrown, let them know we need to have ints
            raise TypeError("Dimensions need to be ints or able to cast as ints")

    def _add_rows(self, num_rows: int) -> None:
        """adds x rows to grid (all 0s to start)"""
        self.grid = self.grid + [[self.empty_squares] * self.dims()[1]] * num_rows
        # update the height
        self.h = len(self.grid)

    def _add_cols(self, num_cols: int) -> None:
        """adds x columns to grid (all 0s to start)"""
        for ridx, row in enumerate(self.grid):
            self.grid[ridx] = row + [self.empty_squares] * num_cols
        # update the width
        self.w = len(self.grid[0])

    def add_line(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """adds a line (increases value by one based on coordinates"""
        if x1 == x2:
            # vertical
            y1, y2 = min(y1, y2), max(y1, y2)
            for ridx, row in enumerate(self.grid[y1 : y2 + 1], y1):
                self.grid[ridx][x1] += 1
        elif y1 == y2:
            # horizontal
            x1, x2 = min(x1, x2), max(x1, x2)
            self.grid[y1] = [
                x + 1 if x1 <= id <= x2 else x for id, x in enumerate(self.grid[y1])
            ]
        else:
            # diagonal
            pass

    def count_overlap(self, overlap_num: int = 2):
        """
        returns how many elements in the grid > 0

        Same Solution using colelctions:
            from collections import Counter
            c = Counter(x for xs in vents.grid for x in xs)
            return sum(c[x] for x in c if x>1)
        """
        return len([y for x in self.grid for y in x if y >= overlap_num])


# PART 1
fabric = Grid()
fabric.new_dims((1000, 1000))
for line in data:
    _id, _, cords, size = line.split()
    x, y = [int(x) for x in cords.strip(":").split(",")]
    w, h = [int(x) for x in size.split("x")]
    # increase value for the given dimensions
    for row in range(x, x + w):
        for col in range(y, y + h):
            fabric.grid[col][row] += 1

part_1_answer = fabric.count_overlap()
print(f"PART 1: {part_1_answer}")
# TO HIGH -> 143513

# PART 2
def find_unique_fabric(fabric):
    for line in data:
        _id, _, cords, size = line.split()
        x, y = [int(x) for x in cords.strip(":").split(",")]
        w, h = [int(x) for x in size.split("x")]
        overlap_count = 0
        # increase value for the given dimensions
        for row in range(x, x + w):
            for col in range(y, y + h):
                if fabric.grid[col][row] > 1:
                    overlap_count += 1

        if overlap_count == 0:
            return _id


part_2_answer = find_unique_fabric(fabric)
print(f"PART 2: {part_2_answer}")
# TO HIGH -> 1222
