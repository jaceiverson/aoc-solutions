"""https://adventofcode.com/2022/day/7"""

from dataclasses import dataclass
from aoc_util import read


# READ INPUT
data = read("./2022/inputs/7.txt").strip().split("\n")
# TEST INPUT
data = read("./2022/inputs/7-test.txt").strip().split("\n")
# PARSE INPUT
@dataclass
class Folder:
    name: str
    parent: None
    files: list
    size: int = 0


@dataclass
class File:
    name: str
    size: int = 0


files = {}
# PART 1
current_location = None
for line in data:
    # this is a command
    if "$" in line:
        if "cd" in line:
            _, _, directory = line.split()
            if directory == "..":
                current_location = files[current_location].parent
            else:
                if files.get(directory) is None:
                    files[directory] = Folder(directory, current_location, [])
                current_location = directory
    elif "dir" in line:
        _, new_dir = line.split()
        files[new_dir] = Folder(new_dir, current_location, [])
        files[current_location].files.append(files[new_dir])
    else:
        size, name = line.split()
        files[current_location].files.append(File(name, int(size)))
        files[current_location].size += int(size)


part_1_answer = None
print(f"PART 1: {part_1_answer}")

# PART 2

part_2_answer = None
print(f"PART 2: {part_2_answer}")
