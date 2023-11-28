"""https://adventofcode.com/2016/day/9"""

from aoc_util import read
import math

# READ INPUT
data = read("./2016/inputs/9.txt").strip()
# TEST INPUT
# data = read("./2016/inputs/9-test.txt").strip().split("\n")
# PARSE INPUT


def test():
    # use the test data for this
    for x in data:
        new = decompress_file(x)
        print(new, len(new))


def parse_code(code: str) -> tuple:
    return map(int, code.strip("(").strip(")").split("x"))


def decompress_file(line: str) -> str:
    position = 0
    output_string = ""
    compression_format = ""
    inside_code = False
    while position < len(line):
        # define the character we are currently at
        char_ = line[position]
        # if the character is a '(' we are starting the code
        if char_ == "(":
            inside_code = True
        if inside_code:
            compression_format += char_
            if char_ == ")":
                # the code has ended, we need to parse the code and add the string
                chars_to_multiply, factor_to_multiply = parse_code(compression_format)
                output_string += (
                    line[position + 1 : position + 1 + chars_to_multiply]
                    * factor_to_multiply
                )
                position += chars_to_multiply
                inside_code = False
                compression_format = ""
        else:
            output_string += char_

        position += 1

    return output_string


# PART 1
part_1_answer = len(decompress_file(data))
print(f"PART 1: {part_1_answer}")

# PART 2
"""
test_a = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"

in this case the next 25 characters after the first '(3x3)ABC(2x3)XY(5x2)PQRST' are multiplied by 3
and the 18 characters after the 18x9 are '(3x2)TWO(5x7)SEVEN' and would be multiplied by 9

so to work out the entire string:
    --first section--
    ABC becomes 27 characters
    XY becomes 18 characters
    PQRST becomes 30
    X is stand alone 1
    --second section--
    TWO becomes 54 characters
    SEVEN becomes 35*9 characters 315
"""


def decompress_part_2(line: str) -> int:
    decompressed_length = 0
    current_multipliers = []
    inside_code = False
    compression_format = ""
    temp_string = ""
    position = 0
    while position < len(line):
        # define the character we are currently at
        char_ = line[position]
        # if the character is a '(' we are starting the code to multiply by
        if char_ == "(":
            if current_multipliers:
                m = [x[1] for x in current_multipliers if x[0] >= position]
                decompressed_length += math.prod(m) * len(temp_string)
            else:
                decompressed_length += len(temp_string)
            inside_code = True
            temp_string = ""
        if inside_code:
            compression_format += char_
            if char_ == ")":
                # the code has ended, we need to parse the code and add the string
                chars_to_multiply, factor_to_multiply = parse_code(compression_format)
                current_multipliers.append(
                    [chars_to_multiply + position + 1, factor_to_multiply]
                )
                inside_code = False
                compression_format = ""
        else:
            if any(x[0] == position for x in current_multipliers):
                m = [x[1] for x in current_multipliers if x[0] >= position]
                decompressed_length += math.prod(m) * len(temp_string)
                temp_string = ""

            temp_string += line[position]

        # decrease all the multipliers (as needed)
        position += 1

    m = [x[1] for x in current_multipliers if x[0] >= position]
    decompressed_length += math.prod(m) * len(temp_string)
    return decompressed_length


part_2_answer = decompress_part_2(data)
print(f"PART 2: {part_2_answer}")
# still pretty slow, but I am happy with this one
