import argparse


def create_file(day):
    """
    Will create a python file will all the lines of code I normally use
    1. Doc String with URL to today's challenge
    2. import statement to get the file reader
    3. code line to read the input
    4. add the part1 & part2 answer strings

    From the main directory run:
        $ python solutions/helper.py {day int to create}
    """
    file_text = (
        f'"""https://adventofcode.com/2021/day/{day}"""\n\n'
        f"from helper import read\n\n"
        "# READ INPUT\n"
        f'data = read("./inputs/{day}.txt")\n'
        "# TEST INPUT\n"
        f'# data = read("./inputs/{day}-test.txt")\n'
        "# PARSE INPUT\n\n"
        "# PART 1\n\n"
        'print(f"PART 1: {part_1_answer}")\n\n'
        "# PART 2\n\n"
        'print(f"PART 2: {part_2_answer}")\n'
    )

    with open(f"./solutions/day{day}.py", "a") as f:
        f.write(file_text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("day_number", type=int, help="Day to create file for.")
    args = parser.parse_args()
    create_file(args.day_number)
