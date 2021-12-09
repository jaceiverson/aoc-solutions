## AOC Util for Python
A library to help create files and pull inputs for the Advent of Code. Can be used to generate previous years input/files as well.


## AOC Star Summary
| Year   |   Stars |   Completion % |
|--------|---------|----------------|
| [2021] |      10 |          20    |
| [2020] |      14 |          28    |
| [2019] |         |           0    |
| [2018] |         |           0    |
| [2017] |         |           0    |
| [2016] |         |           0    |
| [2015] |         |           0    |
| TOTAL  |      24 |           6.86 |

## AOC - Automation
You can just run the script using the command line command:
```
python newday
```
## File Structure
When you clone/fork this repo you will have the following file structure
```
advent_of_code/
└── src/
    └── helper/
        ├── __init__.py
        └── helper.py
└── 20**/
    └── input/
    └── solutions/
└── newday
```
## Flags
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