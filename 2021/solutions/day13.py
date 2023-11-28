"""https://adventofcode.com/2021/day/13"""

from aoc_util import read

# READ INPUT
data = read("./2021/inputs/13.txt")
# TEST INPUT
data = read("./2021/inputs/13-test.txt")
# PARSE INPUT
map, instructions = data.strip().split("\n\n")
map = map.split("\n")
instructions = instructions.split("\n")


class Paper:
    def __init__(self, map) -> None:
        # map is the creation instructions
        self.creation = map
        # grid is the actual cords
        self.grid = []
        self.height = 0
        self.width = 0
        # self.__make_grid()

    def _make_grid(self) -> None:
        for step in self.creation:
            x, y = [int(x) for x in step.split(",")]
            # check to see if we need to make grid bigger
            self.new_dims((x, y))
            print(f"{x=},{y=}")
            # self.show()
            # add the value in
            # y is the row to change
            # x is the column
            self.grid[y][x] = "#"

    def show(self) -> None:
        """prints the grid"""
        for row in self.grid:
            print(row)

    def dims(self) -> tuple[int, int]:
        """returns the height (rows) and width (cols) of the grid"""
        return self.width, self.height

    def new_dims(self, new_dims: tuple[int, int]) -> None:
        """
        Accepts a tuple of dims (w,h) or (x,y) and
        will add rows/cols to fit new maximums
        """
        # unpack the elements
        nw, nh = new_dims
        cw, ch = self.dims()
        try:
            # calulate how many rows/cols to add
            rows_to_add = int(nh) - ch
            cols_to_add = int(nw) - cw
            # if those are above 0, we will add them in
            if rows_to_add > 0:
                self._add_rows(rows_to_add + 1)
            if cols_to_add > 0:
                self._add_cols(cols_to_add + 1)

        except TypeError:
            # if a type error is thrown, let them know we need to have ints
            raise TypeError("Dimensions need to be ints or able to cast as ints")

    def _add_rows(self, num_rows: int) -> None:
        """adds x rows to grid (all '.'s to start)"""
        [self.grid.append(["."] * self.width) for x in range(num_rows)]
        # update the height
        self.height = len(self.grid)

    def _add_cols(self, num_cols: int) -> None:
        """adds x columns to grid (all '.'s to start)"""
        for ridx, row in enumerate(self.grid):
            self.grid[ridx] = row + ["."] * num_cols
        # update the width
        self.width = len(self.grid[0])


p = Paper(map)
p._make_grid()
# PART 1

print(f"PART 1: {part_1_answer}")

# PART 2

print(f"PART 2: {part_2_answer}")
