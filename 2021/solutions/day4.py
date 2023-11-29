"""https://adventofcode.com/2021/day/4"""

from aoc_util import read


def clean_board(path):
    # make boards
    bingo = read(path)
    bingo = bingo.strip().split("\n\n")
    order = bingo[0].split(",")
    boards = [x.strip().split("\n") for x in bingo[1:]]
    for idx, b in enumerate(boards):
        for ridx, row in enumerate(b):
            boards[idx][ridx] = row.strip().split()
    return order, boards


def check_bingo(numbers: list, board: list) -> bool:
    """checks if a bingo was acheived"""
    # check vertial
    for col in range(5):
        col_values = [x[col] for x in board]
        if set(col_values).issubset(numbers):
            return True, f"v{col}"
    # check horizontal
    for ridx, row in enumerate(board):
        if set(row).issubset(numbers):
            return True, f"r{ridx}"
    return False, None


def get_score(numbers: list, board: list) -> int:
    """gets the score of all non-called numbers on a board"""
    return sum(int(col) for row in board for col in row if col not in numbers)


def print_board(board):
    for row in board:
        print(row)


# PART 1
def find_winning_score(order, boards):
    for oidx in range(1, len(order)):
        # set the list of called numbers
        current_list = order[:oidx]
        # if we have called 5 numbers
        # cannot have bingo without 5 numbers
        if oidx > 4:
            # we will loop over all the boards to see if anyone has bingo
            for bidx, indv_board in enumerate(boards):
                # check to see if each board has a bingo
                bingo, bingo_pattern = check_bingo(current_list, indv_board)
                if bingo:
                    # if so, we will calculate the winning score and break
                    score = get_score(current_list, indv_board)
                    last_num = order[oidx - 1]
                    print(f"{last_num=},{oidx=},{bidx=},{bingo_pattern=},{score=}")
                    return score * int(last_num)


# test input
# order,boards = clean_board('./inputs/4-test.txt')

order, boards = clean_board("./inputs/4.txt")

# answer
part_1_answer = find_winning_score(order, boards)
print(f"PART 1: {part_1_answer}")

# to low: 870
# i was forgetting to multiply the score by the last number called


# PART 2
def find_last_winning_score(order, boards):
    winning_boards = {}

    for oidx in range(len(order)):
        # set the list of called numbers
        current_list = order[:oidx]
        # if we have called 5 numbers
        # cannot have bingo without 5 numbers
        if oidx > 4:
            # we will loop over all the boards to see if anyone has bingo
            for bidx, indv_board in enumerate(boards):
                if bidx not in winning_boards.keys():
                    # check to see if each board has a bingo
                    bingo, bingo_pattern = check_bingo(current_list, indv_board)
                    if bingo:
                        # if so, we will calculate the winning score and break
                        score = get_score(current_list, indv_board)
                        last_num = order[oidx - 1]
                        print(f"{last_num=},{oidx=},{bidx=},{bingo_pattern=},{score=}")
                        winning_boards[bidx] = {
                            "last_num": int(last_num),
                            "pattern": bingo_pattern,
                            "score": score,
                            "rank": len(winning_boards.keys()),
                        }

                    if len(winning_boards.keys()) == len(boards):
                        return winning_boards

    return winning_boards


# test input
# order,boards = clean_board('./inputs/4-test.txt')

order, boards = clean_board("./inputs/4.txt")
board_results = find_last_winning_score(order, boards)
loser = board_results[list(board_results.keys())[-1]]
# asnwer
part_2_answer = loser["last_num"] * loser["score"]
print(f"PART 2: {part_2_answer}")

# to low: 22200
# i forgot to remove the bidx when it was marked as a winner
# now it saves the index to a dictionary and skips if it is already a winner
