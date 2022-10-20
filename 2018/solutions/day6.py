"""https://adventofcode.com/2018/day/6"""

from helper import read
from collections import defaultdict
from string import ascii_letters as alphabet
# READ INPUT
data = read("./2018/inputs/6.txt").split('\n')
# TEST INPUT
data = read("./2018/inputs/6-test.txt").split('\n')
# PARSE INPUT

def distance_between_points(point_a,point_b)->int:
    ax,ay=point_a.split(', ')
    bx,by=point_b.split(', ')
    return abs(int(ax)-int(bx)) + abs(int(ay)-int(by))

# PART 1
grid = defaultdict(tuple)
for idx,d in enumerate(data):
    x,y = d.split(', ')
    grid[(int(x),int(y))] = (alphabet[idx],0)

bottom_y = max(grid,key=lambda i:i[1])[1]
top_y = min(grid,key=lambda i:i[1])[1]
bottom_x = max(grid,key=lambda i:i[0])[0]
top_x = min(grid,key=lambda i:i[0])[0]


for x in range(top_x,bottom_x+1):
    for y in range(top_y,bottom_y+1):
        # find closest hub
        for idx,h in enumerate(data):
            distance = distance_between_points(f"{x}, {y}",h)
            # if we haven't looked at this point yet, add it in
            if not grid[(x,y)]:
                grid[(x,y)] = (alphabet[idx],distance)
            # if the points are equal, we need to have it be a .
            # as more than 1 location is closest
            elif distance==grid[(x,y)][1]:
                grid[(x,y)] = (".",distance)
            # if it is less, this hub becomes the new distance as it is closer
            elif distance<grid[(x,y)][1]:
                grid[(x,y)] = (alphabet[idx],distance)




part_1_answer = None
print(f"PART 1: {part_1_answer}")

# PART 2

part_2_answer = None
print(f"PART 2: {part_2_answer}")
