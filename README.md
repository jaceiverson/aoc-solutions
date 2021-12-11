# AOC Util for Python
A library to help create files and pull inputs for the Advent of Code. Can be used to generate previous years input/files as well.

# AOC Star Summary
| Year   |   Stars |   Completion % |
|--------|---------|----------------|
| [2021] |      15 |          30    |
| [2020] |      14 |          28    |
| [2019] |         |           0    |
| [2018] |         |           0    |
| [2017] |         |           0    |
| [2016] |         |           0    |
| [2015] |         |           0    |
| TOTAL  |      29 |           8.29 |

# Automatic Summary Update 
You can automatically update your summary table like the one above. There are functions in the local helper modual that 
> 1. scrapes the AOC site to look at how many stars you have completed for each year
> 2. saves those numbers as markdown
> 3. replaces the existing table with the updated values

To do this you can run the command
```
python update-readme
```

Note: for this to happen, you must have saved your <a href=https://github.com/jaceiverson/aoc-util#Session-id-cookie>session id</a> as an enviornment variable.

## Instalation
### Clone Repo
Navigate to your desired directory in terminal. Run the `git clone` command to download the files:
```
git clone https://github.com/jaceiverson/aoc-util.git
```
Now you have the files on your machine

## Create virtual enviornment
I recommended to create a virtualenv using the <a href="https://pypi.org/project/virtualenv/" target="_blank">virtualenv library</a>. Follow these steps:

### install the package to main python instance
```
pip3 install virtualenv
```
### actually create the virtual enviornment
```
python3 -m virtualenv venv
```
### activate the enviornment
```
source venv/bin/activate
```
### install all the necessary packages
```
pip install requirements.txt -r
```

Now we are all installed and need one more step before the automation can begin

## Session id cookie
You will need to have your session id saved as an enviornment variable. In this project I use dotenv; this allows me to store these variables in a .env file, and access them in my code after using the `load_dotenv()` function.

1. Create a `.env` file in the main directory of the project
2. Save your session id in your .env file in this format
```
COOKIE_SESSION={YOUR_SESSION_ID_HERE}
```

Now you will be able to use the automation without a hitch. Carry on.

## Running the File Creation & Input Extraction Script
The automation of this project relys on the `newday` script. This will create a file (and directories if necessary), and pre-populate generic values (you can change this in the newday file). More information on the project <a href=https://github.com/jaceiverson/aoc-util#File-Structure>file structure</a>.<br>
You can run the script using the command line command and see the outputed file that would be created.

> year & day are populated when the script runs. By default they are today's date and year. This is changed using <a href=https://github.com/jaceiverson/aoc-util#Flags>flags</a>

#### Commandline Command
```
python newday
```
#### Output
```py
"""https://adventofcode.com/{year}/day/{day}"""

from helper import read

# READ INPUT
data = read("./{year}/inputs/{day}.txt")
# TEST INPUT
# data = read("./{year}/inputs/{day}-test.txt")
# PARSE INPUT

# PART 1

print(f"PART 1: {part_1_answer}")

# PART 2

print(f"PART 2: {part_2_answer}")
```
## Flags
Use flags to add additional arguments to the script. You will add the value after you type the flag. If you wanted to create a file and get the input for Dec 7, 2014's challenge, you would do the following
```
python newday -d 7 -y 2014 -i
```
### -i (--input)
Pulls the input for the day selected. Must have session id stored as an environment variable named COOKIE_SESSION in the .env file

default: False

### -d (--day)
Changes the day from today's date to any other daily puzzle. Selection is ints from 1-25.

default: today's date (int)

### -y (--year)
Changes the year from the current year to any of the previous. Selection is each year including and after 2015. (2015-)

default: today's year (int)

## Steps to make Unix Command
You can also follow these steps to make a Unix Command name "newday". This will allow you to run the script by only typing "newday" instead of the traditional python command "python newday".

 - chmod +x newday
 - mkdir -p ~/bin
 - cp newday ~/bin
 - export PATH=$PATH":$HOME/bin"

## File Structure
When you clone/fork and set up this repo for use, you should have the following file structure
```
advent_of_code/
└── src/
    └── helper/
        ├── __init__.py
        └── helper.py
        └── file_creation.py
        └── readme.py
└── 20**/
    └── input/
    └── solutions/
└── newday
└── update-readme
└── .env
└── venv
```