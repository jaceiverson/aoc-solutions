"""https://adventofcode.com/2023/day/11"""


from aoc_util import read
from aoc_util.grid import Grid
import itertools

# MAIN INPUT
data = read("./2023/inputs/11.txt").strip().split("\n")
# TEST INPUT
# data = read("./2023/inputs/11-test.txt").strip().split("\n")
# EXAMPLE INPUT
data = read("./2023/inputs/11-test-e.txt").strip().split("\n")
# PARSE INPUT


def get_empty_rows(g: Grid):
    # empty rows
    return [idx_ for idx_, x in enumerate(g.rows) if "#" not in x]


def get_empty_cols(g: Grid):
    # empty _columns
    return [idx_ for idx_ in range(g.width) if "#" not in g.get_column(idx_)]


def add_empty_space(g: Grid) -> Grid:
    # empty rows
    empty_rows = get_empty_rows(g)
    # empty _columns
    empty_columns = get_empty_cols(g)

    print(f"{empty_columns=}")
    print(f"{empty_rows=}")
    for idx_r, r in enumerate(empty_rows):
        g.add_row("." * g.width, r + idx_r)

    for idx_c, c in enumerate(empty_columns):
        g.add_column("." * g.height, c + idx_c)

    return g


# PART 1
def part_1(data: list):
    g = Grid(data)
    g = add_empty_space(g)
    numbers = list(g.search_grid(lambda x: x == "#"))
    combos = list(itertools.combinations([list(x.keys())[0] for x in numbers], 2))
    return sum(g.manhattan_distance(c[0], c[1]) for c in combos)


print(f"PART 1: {part_1(data)}")


def expanses_crossed(a, b, row_expanse, col_expanse, expanse_size=10):
    rows_crossed = set(range(a[0], b[0] + 1)).intersection(set(row_expanse))
    cols_crossed = set(range(a[1], b[1] + 1)).intersection(set(col_expanse))
    return (expanse_size - 1) * len(rows_crossed), (expanse_size - 1) * len(
        cols_crossed
    )


# PART 2
def part_2(data: list):
    """
    essentially you will calculate when your manhattan distance passes through an empty row/column
    for each empty row/column you will add 1_000_000 instead of 1
    so I think you would actually or could actually just add 999_999
    """
    g = Grid(data)
    row_expanse = get_empty_rows(g)
    col_expanse = get_empty_cols(g)
    numbers = list(g.search_grid(lambda x: x == "#"))
    combos = list(itertools.combinations([list(x.keys())[0] for x in numbers], 2))
    sum_ = 0
    for c in combos:
        base_distance = g.manhattan_distance(c[0], c[1])
        expansion = expanses_crossed(c[0], c[1], row_expanse, col_expanse)
        base_distance += expansion[0]
        base_distance += expansion[1]
        sum_ += base_distance

    return sum_


print(f"PART 2: {part_2(data)}")
