"""https://adventofcode.com/2021/day/21"""

from helper import read
from dataclasses import dataclass

# READ INPUT
data = read("./2021/inputs/21.txt")
# TEST INPUT
#data = read("./2021/inputs/21-test.txt")
# PARSE INPUT
p1,p2 = [int(x[-1]) for x in data.strip().split('\n')]

start_roll = 1
turn = 0
p1_score = 0
p2_score = 0
board_size = 10
die_size = 100

@dataclass
class Player:
    pos: int
    score: int = 0

def calc_scores(player_obj:Player,start_roll:int):
    current_roll_sum = (start_roll % 100)*3 + 3
    if (player_obj.pos + current_roll_sum) % board_size != 0:
        player_obj.pos = (player_obj.pos + current_roll_sum) % board_size
    else:
        player_obj.pos = board_size
    player_obj.score += player_obj.pos
    return player_obj

# PART 1
p1 = Player(p1)
p2 = Player(p2)

while max(p1.score,p2.score) < 1000:
    # player 1
    p1 = calc_scores(p1,start_roll)
    start_roll += 3
    turn += 1

    if max(p1.score,p2.score) >= 1000:
        break

    # player 2
    p2 = calc_scores(p2,start_roll)
    start_roll += 3
    turn += 1

part_1_answer = min(p1.score,p2.score) * (start_roll-1)
print(f"PART 1: {part_1_answer}")

# PART 2
part_2_answer = None
print(f"PART 2: {part_2_answer}")
