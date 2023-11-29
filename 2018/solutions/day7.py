"""https://adventofcode.com/2018/day/7"""

from aoc_util import read
from rich import print

# READ INPUT
data = read("./2018/inputs/7.txt").strip().split("\n")


# TEST INPUT
# data = read("./2018/inputs/7-test.txt").strip().split("\n")
# PARSE INPUT
class Node:
    def __init__(self, name: str):
        self.name: str = name
        self.waits_for: list = []
        self.allows_for: list = []

    @property
    def time(self):
        return ord(self.name) - 4

    def __str__(self):
        return (
            f"{self.name=}\nWaits for: {self.waits_for}\nAllows for: {self.allows_for}"
        )

    def __repr__(self):
        return f"Node: {self.name}"

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name


def parse_input(data: list):
    nodes: dict[str, Node] = {}
    for d in data:
        allows, waits = d.split(" must be finished before step ")
        allows, waits = allows[-1], waits[0]
        if nodes.get(allows) is None:
            nodes[allows] = Node(allows)

        if nodes.get(waits) is None:
            nodes[waits] = Node(waits)

        nodes[waits].waits_for.append(allows)
        nodes[allows].allows_for.append(waits)
        nodes[allows].allows_for.sort()

    return nodes


def traverse_path(node: Node, executed=None, queue=None, idx=0):
    if executed is None:
        executed = []

    if queue is None:
        queue = []

    # execute node if dependencies are met
    if set(node.waits_for).issubset(set(executed)):
        executed.append(node.name)
        # add values to queue and sort
        queue.extend(node.allows_for)
        queue = sorted(list(set(queue)))

        if node.name in queue:
            queue.remove(node.name)

        if queue:
            traverse_path(nodes[queue[0]], executed, queue)
        return executed
    else:
        traverse_path(nodes[queue[idx + 1]], executed, queue, idx + 1)


nodes = parse_input(data)
starting_nodes = sorted([x for x in nodes.values() if x.waits_for == []])

final = traverse_path(
    starting_nodes[0], executed=None, queue=[x.name for x in starting_nodes[1:]]
)
# check queue

# 1) start with root
# 2) add dependencies to queue in alphabetic order
# 3) execute first dependency
# 4) add those dependencies to queue in alphabetic order

# PART 1
part_1_answer = "".join(final)
print(f"PART 1: {part_1_answer}")

# PART 2
WORKERS = 2


def traverse_path_part_2(node, executed=None, queue=None, idx=0):
    if executed is None:
        executed = []

    if queue is None:
        queue = []


nodes = parse_input(data)
starting_nodes = sorted([x for x in nodes.values() if x.waits_for == []])

final = traverse_path_part_2(
    starting_nodes[0], executed=None, queue=[x.name for x in starting_nodes[1:]]
)

part_2_answer = final
print(f"PART 2: {part_2_answer}")
