"""https://adventofcode.com/2021/day/12"""

from helper import read

# READ INPUT
data = read("./2021/inputs/12.txt")
# TEST INPUT
data = read("./2021/inputs/12-test.txt")
# PARSE INPUT
data = data.strip().split("\n")


C = {}
for node in data:
    start, end = node.split("-")
    if C.get(start):
        C[start].append(end)
    else:
        C[start] = [end]
    if C.get(end):
        C[end].append(start)
    else:
        C[end] = [start]

"""
LOGIC

if starting cave is capital, going to a lower cave is one way
if the lower cave has no children, cannot path that way

leave from start, finish with end

"""
# https://topaz.github.io/paste/#XQAAAQAqAwAAAAAAAAAyGUj/TuRfOI7nwo+gbNPmE8BAa64yJre1LXowmkvToIIzGJwTLCwJ9fWHR92o9Pr7IoNBSXMfZdes5kjMoCgiBdmtAPxECRLmCC7dQl5tIwFkKbAkt0itH5L6wgfDy83JzAdaNjh68Ip4ccx8gPeib0SymvtKDyCPuK3JDtbPYYxe4E37DUHSBJSXeUgSjJqlhLMBmDn0MByD9I3+fIv31Q2lFWOc75Zl0CHnTi0IzmJ5AupkjcOIXLjQWE7yCRg69lA7PicQZUYoxfIOBQzVQN0UBx3yOZ2vK38G89AhJOnwtP3CtV5HOU9lI14c+vZ+F7bOkkqR+bwgj2J4w0d/xtoidFjdnj4v9fMeN0eFo+h6YFzAZ3rRbDHXdzN8JownTCCVtwdKz53jCYj/JsqkAA==
def countPaths(currentCave, noEntry):
    if currentCave == "end":
        # we have arrived at the end of the cave
        return 1
    paths = C.get(currentCave)[:]
    paths = [path for path in paths if path not in noEntry]

    # there is no valid path
    if not paths:
        return 0
    # if keep track of the caves we can't enter
    if currentCave[0] != currentCave[0].upper():
        noEntry = noEntry + [currentCave]

    print("Current Cave:", currentCave)
    print("Paths:", paths)
    print("Do not Enter:", noEntry)
    return sum(countPaths(path, noEntry) for path in paths)


print(countPaths("start", []))


def path(path_options, current_path):
    current_cave = current_path[-1]
    # get rid of lower case already in path
    current_options = [
        x
        for x in path_options[current_cave]
        if x.lower not in current_path and "end" not in current_path
    ]

    for selection in current_options:
        current_path.append(selection)
        if selection in path_options:
            path(path_options, current_path)

    return current_path


p = path(C, ["start"])

# PART 1

print(f"PART 1: {part_1_answer}")

# PART 2

print(f"PART 2: {part_2_answer}")
