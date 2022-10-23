"""https://adventofcode.com/2015/day/11"""

from helper import read
from string import ascii_lowercase as alphabet

# READ INPUT
data = read("./2015/inputs/11.txt").strip()
# TEST INPUT
# data = read("./2015/inputs/11-test.txt")
# PARSE INPUT

# FROM day 5
def check_double_letter(word: str) -> bool:
    return any(c == word[idx] for idx, c in enumerate(word[:-1], 1))


def check_pair(word: str) -> bool:
    # loop through and check each pair
    for idx, c in enumerate(word):
        main_pair = word[idx : idx + 2]
        for idx2, c2 in enumerate(word[idx + 2 :], idx + 2):
            compare_pair = word[idx2 : idx2 + 2]
            if main_pair == compare_pair:
                return True
    return False


# PART 1
# rule 1
def rule_1(pwd: str) -> bool:
    straight_of_3 = 1
    for idx, c in enumerate(pwd[:-1], 1):
        # check for a straight of 3
        if alphabet.index(c) + 1 == alphabet.index(pwd[idx]):
            straight_of_3 += 1
        else:
            straight_of_3 = 1
        if straight_of_3 == 3:
            return True
    return False


def rule_2(pwd: str) -> bool:
    return all(l not in pwd for l in ["i", "l", "o"])


def rule_3(pwd: str) -> bool:
    pairs = 0
    idx = 0
    while idx < len(pwd) - 1:
        letter = pwd[idx]
        next_letter = pwd[idx + 1]
        if letter == next_letter:
            pairs += 1
            idx += 1
        if pairs == 2:
            return True
        idx += 1
    return False


def check_password(pwd: str, breakdown: bool = False) -> bool:
    if breakdown:
        return rule_1(pwd), rule_2(pwd), rule_3(pwd)
    return all([rule_1(pwd), rule_2(pwd), rule_3(pwd)])


# some sort of recursive solution
def next_password(pwd: list, index: int = -1) -> str:
    letter = pwd[index]
    next_letter_idx = (alphabet.index(letter) + 1) % 26
    if next_letter_idx == 0:
        pwd[index] = "a"
        return next_password(pwd, index - 1)

    pwd[index] = alphabet[next_letter_idx]
    return "".join(pwd)


def remove_bad_letters(pwd):
    # rule 2
    change_idx = None
    for idx, c in enumerate(pwd):
        if c in ["i", "l", "o"]:
            change_idx = idx
            break
    if change_idx:
        pwd[idx] = alphabet[alphabet.index(c) + 1]
        # assign the rest of the letters 'a'
        for idx_2, c in enumerate(pwd[idx + 1 :], idx + 1):
            pwd[idx_2] = "a"

    return pwd


def part_1(pwd: str):
    while check_password(pwd) is False:
        # print(pwd)
        temp = list(pwd)
        temp = remove_bad_letters(temp)
        pwd = next_password(temp)
    return pwd


def test():
    assert check_password("hijklmmn", True) == (True, False, False)
    assert check_password("abbceffg", True) == (False, True, True)
    assert check_password("abbcegjk", True) == (False, True, False)
    assert check_password("abcdffaa", True) == (True, True, True)
    assert check_password("abcdffaa") == True
    assert check_password("ghjaabcc") == True
    assert check_password("ghjaaabc", True) == (True, True, False)
    assert part_1("abcdefgh") == "abcdffaa"
    assert part_1("ghijklmn") == "ghjaabcc"


# PART 1
part_1_answer = part_1(data)
print(f"PART 1: {part_1_answer}")

# PART 2
part_2_answer = part_1(next_password(list(part_1_answer)))
print(f"PART 2: {part_2_answer}")
