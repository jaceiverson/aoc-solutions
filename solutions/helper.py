import argparse

def read(path):
    with open(path) as f:
        rules = f.read()
    return rules

def create_file(day):
    file_text = f"\"\"\"https://adventofcode.com/2021/day/{day}\"\"\"\n\n"\
    f"from helper import read\n\n"\
    f"data = read(\"./inputs/{day}.txt\")\n\n"

    with open(f"./solutions/day{day}.py",'a') as f:
        f.write(file_text)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('day_number',type=int,help='Day to create file for.')
    args = parser.parse_args()
    create_file(args.day_number)