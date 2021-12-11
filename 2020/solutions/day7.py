"""https://adventofcode.com/2020/day/7"""

# TODO -> part 2

import pandas as pd
import re
from dataclasses import dataclass

global total_bags


def remove_digit(ini_string):
    return "".join([i for i in ini_string if not i.isdigit()])


def extract_digit(ini_string):
    return "".join([i for i in ini_string if i.isdigit()])


def remove_spaces_periods_bags(base_string):
    return (
        re.sub("\s+", " ", base_string)
        .replace(".", "")
        .replace(" bags", "")
        .replace(" bag", "")
    )


def clean(d):
    return remove_spaces_periods_bags(remove_digit(d).strip()).split(", ")


def seven_a():
    with open("./2020/inputs/7.txt") as f:
        rules = f.read()

    r = rules.split(".\n")
    r = [x.split(" bags contain ") for x in r]

    start_bag = "shiny gold"
    all_bags_list = []

    def find_bags(bag):
        contents = [row[0] for row in r if row != [""] and bag in row[1]]
        if contents:
            all_bags_list.append(contents)
            for indv_bag in contents:
                find_bags(indv_bag)

    find_bags(start_bag)
    return len(set([y for x in all_bags_list for y in x]))


# TODO
@dataclass
class Bag:
    color: str
    bags_inside: dict


def seven_b():
    global total_bags
    with open("./files/seven_a.txt") as f:
        rules = f.read()

    r = rules.split(".\n")
    # split the rule into parent and children
    r = [x.split(" bags contain ") for x in r]
    # add the number of bags in the bag
    for row in r:
        row.append(row[1].count(",") + 1)

    start_bag = "shiny gold"
    all_bags = []

    class BagChain:
        def __init__(self, rules, start) -> None:
            self.r = rules
            self.start_bag = start
            self.total_bags = 0

        def find_internal_bag_count(self, bag):
            return [row for row in self.r if row != [""] and bag in row[0]][0][2]

        def find_sub_bags(self, bag):
            return [row for row in self.r if row != [""] and bag in row[0]][0][1]

        def find_total_bags(self, bag, q):
            self.total_bags += self.find_internal_bag_count(bag) * q

        def process(self, bag=None, q=1):
            if bag is None:
                bag = self.start_bag

            # set the total
            self.find_total_bags(bag, q)

            sub_bags = self.find_sub_bags(bag)
            sub_bag_q = extract_digit(sub_bags)
            for b, count in zip(sub_bags, sub_bag_q):
                quantity = 1
                self.process(b, q * count)

    def find_total_bags(bag, quantity=1, total=0):

        contents = [row for row in r if row != [""] and bag in row[0]][0]
        print(f"{bag}, {quantity=}, {total=}")
        internal_bags_count = contents[2]
        total += internal_bags_count * quantity

        if contents[1] != "no other bags":

            bag_counts = extract_digit(contents[1])

            for idx, sub_bag in enumerate(clean(contents[1])):
                print(f"{bag_counts=},{idx=},{sub_bag=}")
                number = bag_counts[idx]
                bag_type = sub_bag
                all_bags.append(contents)

                find_total_bags(bag_type, quantity + int(number), total)

        return total

    find_total_bags(start_bag)
