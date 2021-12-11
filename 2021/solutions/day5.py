"""https://adventofcode.com/2021/day/5"""

from helper import read

data = read("./2021/inputs/5.txt")

# testing file
data = read("./2021/inputs/5-test.txt")

data = data.strip().split("\n")


class Grid:
    def __init__(self) -> None:
        # will be 3D list
        self.grid = []
        # height
        self.h = 0
        # width
        self.w = 0

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
        self.grid = self.grid + [[0] * self.dims()[1]] * num_rows
        # update the height
        self.h = len(self.grid)

    def _add_cols(self, num_cols: int) -> None:
        """adds x columns to grid (all 0s to start)"""
        for ridx, row in enumerate(self.grid):
            self.grid[ridx] = row + [0] * num_cols
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
vents = Grid()
# loop through instructions to get the coordinates
for i in data:
    # parse the string, get the int coordinates
    x, y = i.split(" -> ")
    x1, y1 = x.split(",")
    x2, y2 = y.split(",")
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    # check to make sure the grid is big enough
    w = max(x1, x2)
    h = max(y1, y2)
    # if it isn't, .new_dims will add rows/cols to the grid
    vents.new_dims((h + 1, w + 1))
    # once we know it is big enough, add the line
    vents.add_line(x1, y1, x2, y2)

# vents.show()
part_1_answer = vents.count_overlap()
print(f"PART 1: {part_1_answer}")
# to high 4461
# i am counting the score correctly, but the large grid isn't being generated correctly
# I can get the correct score with the small grid
# tried 4460 just to check ;)

# PART 2
