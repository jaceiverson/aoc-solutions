"""https://adventofcode.com/2020/day/6"""

import pandas as pd


def six_a(answers):
    # separates groups
    answers = answers.split("\n\n")

    unique_answers = 0
    for x in answers:
        temp = []

        for y in x.replace("\n", ""):
            temp.append(y)

        temp = pd.Series(temp)
        unique_answers += len(temp.unique())

    return unique_answers


def six_b(answers):
    # separates groups
    answers = answers.split("\n\n")

    answer_count = 0
    for x in answers:

        common_answer = True
        new_list = x.split("\n")

        y = new_list[0]
        for z in y:
            for i in new_list:

                if z in i:
                    common_answer = True
                else:
                    common_answer = False
                    break

            if common_answer:
                answer_count += 1

    return answer_count


if __name__ == "__main__":
    with open("./2020/inputs/6.txt") as f:
        file = f.read()
    print(six_a(file))
    print(six_b(file))
