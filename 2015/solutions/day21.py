"""https://adventofcode.com/2015/day/21"""

from dataclasses import dataclass
from aoc_util import read, mytime
import json

# READ INPUT
data = read("./2015/inputs/21.txt").strip().split("\n")
# TEST INPUT
# data = read("./2015/inputs/21-test.txt")
# PARSE INPUT
b_hp, b_damage, b_armor = [int(x.split(": ")[1]) for x in data]
with open("./2015/inputs/21-store.json") as f:
    store = json.load(f)


@dataclass
class Player:
    hp: int
    damage: int
    armor: int


def user_win_combat(user: Player, boss: Player):
    boss_damage = max(user.damage - boss.armor, 1)
    user_damage = max(boss.damage - user.armor, 1)
    boss_rounds = boss.hp / boss_damage
    user_rounds = user.hp / user_damage
    return boss_rounds <= user_rounds


def simple_user_win(user, boss):
    if user.hp == boss.hp:
        return user.damage + user.armor >= boss.damage + boss.armor
    return user_win_combat(user, boss)


@mytime
def part_1(me, boss, combat=user_win_combat, output: bool = False):
    min_gold = 100000000
    # WEAPONS (have to pick 1)
    for weapon, stats in store["weapons"].items():
        g_cost, w_damage, w_armor = stats
        # ARMOR (optional max 1)
        for armor, a_stats in store["armor"].items():
            a_cost, a_damange, a_armor = a_stats
            # RINGS (optional max 2)
            for ring1, r1_stats in store["rings"].items():
                r1_cost, r1_damage, r1_armor = r1_stats
                for ring2, r2_stats in store["rings"].items():
                    if ring1 != ring2:
                        r2_cost, r2_damage, r2_armor = r2_stats
                        me.armor = w_armor + a_armor + r1_armor + r2_armor
                        me.damage = w_damage + a_damange + r1_damage + r2_damage
                        gold = a_cost + g_cost + r1_cost + r2_cost
                        if combat(me, boss) and gold < min_gold:
                            min_gold = gold
                            if output:
                                print(
                                    f"{gold=},{weapon=},{armor=},{ring1=},{ring2=},{me=}"
                                )
    return min_gold


@mytime
def part_2(me, boss, combat=user_win_combat, output=False):
    max_gold = 0
    # WEAPONS (have to pick 1)
    for weapon, stats in store["weapons"].items():
        g_cost, w_damage, w_armor = stats
        # ARMOR (optional max 1)
        for armor, a_stats in store["armor"].items():
            a_cost, a_damange, a_armor = a_stats
            # RINGS (optional max 2)
            for ring1, r1_stats in store["rings"].items():
                r1_cost, r1_damage, r1_armor = r1_stats
                for ring2, r2_stats in store["rings"].items():
                    if ring1 != ring2:
                        r2_cost, r2_damage, r2_armor = r2_stats
                        me.armor = w_armor + a_armor + r1_armor + r2_armor
                        me.damage = w_damage + a_damange + r1_damage + r2_damage
                        gold = a_cost + g_cost + r1_cost + r2_cost
                        if not combat(me, boss) and gold > max_gold:
                            max_gold = gold
                            if output:
                                print(
                                    f"{gold=},{weapon=},{armor=},{ring1=},{ring2=},{me=}"
                                )
    return max_gold


"""
This is a brute force solution.
We could also attempt to clean up the solution by finding all combinations
To win, my combined stats need to be >= the boss's combined stats
To lose, my combined stats need to be < the boss's combine stats 
"""

# PLAYERS
# starting stats
me = Player(100, 0, 0)
# actual boss
boss = Player(b_hp, b_damage, b_armor)


# PART 1
part_1_answer = part_1(me, boss)
print(f"PART 1: {part_1_answer}")
# INCORRECT -> 93


# PART 2
part_2_answer = part_2(me, boss)
print(f"PART 2: {part_2_answer}")

# TIMEs
time_it = False
if time_it:
    p1_1 = part_1(me, boss)
    p1_2 = part_1(me, boss, simple_user_win)

    p2_1 = part_2(me, boss)
    p2_2 = part_2(me, boss, simple_user_win)
"""
    part_1 :    2629916 ns
    part_1 :    2026292 ns
    part_2 :    2514417 ns
    part_2 :    1890917 ns
"""
