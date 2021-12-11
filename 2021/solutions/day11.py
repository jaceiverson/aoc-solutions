"""https://adventofcode.com/2021/day/11"""

from helper import read

import copy

# READ INPUT
data = read("./2021/inputs/11.txt")
# TEST INPUT
# data = read("./2021/inputs/11-test.txt")
# PARSE INPUT
data = data.strip().split("\n")
data = [[int(x) for x in y] for y in data]


class Oct:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.flashes = 0

    def set_grid(self, grid):
        self.grid = grid

    def show(self):
        for row in self.grid:
            print(row)

    def reset_flash_count(self):
        self.flashes = 0

    def zero_check(self):
        """Will return True if all are 0"""
        for row in self.grid:
            for col in row:
                if col != 0:
                    return False
        return True

    def process(self, step):
        # print(step)
        # self.show()
        self.increase_1()
        self.reset_flashed_grid()

    def find_sync(self):
        counter = 0
        while not self.zero_check():
            self.process(counter)
            counter += 1

        return counter

    def increase_1(self):
        # increase all ints by 1 - GOOD
        for r_idx, row in enumerate(self.grid):
            for c_idx, col in enumerate(row):
                if self.grid[r_idx][c_idx] < 10:
                    self.grid[r_idx][c_idx] += 1
                    if self.grid[r_idx][c_idx] > 9:
                        self.flashes += 1
                        self.increase_neighbors(r_idx, c_idx)

    def increase_neighbors(self, row, col):
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                # not self
                if not (row_offset == 0 and col_offset == 0):
                    # not out of bounds
                    if (0 <= row + row_offset < len(self.grid)) and (
                        0 <= col + col_offset < len(self.grid[0])
                    ):
                        # if the cell is below 10 increase it
                        if self.grid[row + row_offset][col + col_offset] < 10:
                            # increase neighbors
                            self.grid[row + row_offset][col + col_offset] += 1
                            # will flash if cell checking is > 9
                            if self.grid[row + row_offset][col + col_offset] > 9:
                                self.flashes += 1
                                self.increase_neighbors(
                                    row + row_offset, col + col_offset
                                )

    def reset_flashed_grid(self):
        for r_idx, row in enumerate(self.grid):
            for c_idx, col in enumerate(row):
                if self.grid[r_idx][c_idx] > 9:
                    self.grid[r_idx][c_idx] = 0


# PART 1
octi = Oct(copy.deepcopy(data))
gen = 100
# process generations
[octi.process(step) for step in range(gen)]
part_1_answer = octi.flashes
print(f"PART 1: {part_1_answer}")
octi.show()

# PART 2
octi.reset_flash_count()
octi.set_grid(copy.deepcopy(data))
part_2_answer = octi.find_sync()
print(f"PART 2: {part_2_answer}")
octi.show()
