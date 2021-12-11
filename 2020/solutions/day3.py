"""https://adventofcode.com/2020/day/3"""

import math
import numpy as np


def three_a(right_steps=3, down_steps=1):
    with open("./2020/inputs/3.txt", "r") as f:
        route = f.read()
    route = route.split("\n")
    tree_count = 0
    right_count = 0

    for y in range(0, len(route), down_steps):
        if route[y] == "":
            break
        else:
            # we need to go 3 times as far right as we do down
            slope = route[y] * (math.ceil(len(route) / len(route[y]))) * right_steps

            if slope[right_count] == "#":
                tree_count += 1

            right_count += right_steps

    print("Right: ", right_steps, " Down: ", down_steps)
    print(tree_count)
    return tree_count


def three_b():
    one = (1, 1)
    two = (3, 1)
    three = (5, 1)
    four = (7, 1)
    five = (1, 2)

    tests = [one, two, three, four, five]
    results = []
    for x in tests:
        results.append(three_a(x[0], x[1]))

    return np.product(np.array(results))


if __name__ == "__main__":
    # three a reads the file in
    print(three_a())
    print(three_b())
