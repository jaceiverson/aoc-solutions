"""Help create files and pull input for AOC"""
from argparse import ArgumentParser
from pathlib import Path
from datetime import date

# load in the cookie session
from os import environ
from dotenv import load_dotenv

# HTTP Requests
from requests import get
from requests.models import HTTPError

load_dotenv()


def get_input(day: int, year: int) -> None:
    """
    Uses your session cookie (to get your specific login) to pull your
    Puzzle Inputs. You can find session cookie
    in the developer portal of your browswer.

    For Chrome "Application" > "Storage" > "Cookies" >
    Find the session and retreave the value.

    Accepts a day, saves the input if it doesn't exist already
    Will create "./inputs" folder if it doesn't exist

    Note:
        This does not create the test input (from the question),
        you will have to create that file yourself
    """
    file_path = Path(f"./{year}/inputs/{day}.txt")
    # if the folder doesn't exists, create it
    if not file_path.parent.exists():
        file_path.parent.mkdir(parents=True)
    # if the file doesn't exists, create it and save the request data
    if not file_path.exists():
        # HTML request
        r = get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies={"session": environ["COOKIE_SESSION"]},
        )
        # save file if status 200
        if r.status_code == 200:
            with open(file_path, "w") as f:
                f.write(r.text)
            print(f"INPUT SAVED: {file_path}")
        else:
            raise HTTPError(
                f"Did not get status 200. STATUS: {r.status_code}, "
                "verify session cookie is correct"
            )
    else:
        print(f"{file_path} already exists. Will not overwrite")


def create_file(day: int, year: int) -> None:
    """
    Will create a python file will all the lines of code I normally use
    Also will create the "./solutions" directory if it doesn't exists

    What is included in the Python File Template:
    1. Doc String with URL to today's challenge
    2. import statement to get the file reader
    3. code line to read the input
    4. part1 & part2 answer print statements

    TO RUN from the main directory in terminal:
        $ python solutions/helper.py {day int to create}
    """
    file_text = (
        f'"""https://adventofcode.com/{year}/day/{day}"""\n\n'
        "from helper import read\n\n"
        "# READ INPUT\n"
        f'data = read("./{year}/inputs/{day}.txt")\n'
        "# TEST INPUT\n"
        f'# data = read("./{year}/inputs/{day}-test.txt")\n'
        "# PARSE INPUT\n\n"
        "# PART 1\n\n"
        "part_1_answer = None\n"
        'print(f"PART 1: {part_1_answer}")\n\n'
        "# PART 2\n\n"
        "part_2_answer = None\n"
        'print(f"PART 2: {part_2_answer}")\n'
    )

    # creates the python file in solutions
    file_path = Path(f"./{year}/solutions/day{day}.py")
    if not file_path.parent.exists():
        file_path.parent.mkdir(parents=True)
    if not file_path.exists():
        with open(file_path, "a") as f:
            f.write(file_text)
        print(f"TEMPLATE CREATED: {file_path}")
    else:
        print(f"{file_path} already exists. Will not overwrite")


def newday():
    today = date.today().day
    year = date.today().year
    parser = ArgumentParser(description="Create AOC Python Files from template.")
    parser.add_argument(
        "-d",
        "--day",
        nargs="?",
        default=today,
        type=int,
        help="Defaults to today's date (day), can change to any day (1-25)",
    )
    parser.add_argument(
        "-y",
        "--year",
        nargs="?",
        default=year,
        type=int,
        help="Defaults to this year, can change to any previous year (2015-).",
    )
    parser.add_argument(
        "-i",
        "--input",
        nargs="?",
        default=False,
        const=True,
        type=bool,
        help="If tagged retrives the selected day's input. Requires session cookie as env variable.",
    )
    args = parser.parse_args()
    # CHECK VALUES to make sure they are in range
    if args.day not in range(1, 26):
        raise ValueError(f"Day needs to be in range (1-25)")
    if args.year not in range(2015, year + 1):
        raise ValueError(f"Year needs to be in range {range(2015,year+1)}")

    print(args)
    print("CREATING PYTHON FILE")
    create_file(args.day, args.year)
    if args.input:
        print("CREATING INPUT FILE")
        get_input(args.day, args.year)
    print("PROCESS COMPLETE")


if __name__ == "__main__":
    newday()
