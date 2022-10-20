"""https://adventofcode.com/2015/day/7"""

from helper import read

# READ INPUT
data = read("./2015/inputs/7.txt").strip().split("\n")
# TEST INPUT
# data = read("./2015/inputs/7-test.txt").strip().split("\n")
# PARSE INPUT


def check_overflow(value: int):
    if value < 0:
        return 65535 + value + 1
    elif value > 65535:
        return check_overflow(value - 65535)
    return value


# PART 1
data.sort()


def find_signals(data):
    results = {"a": None}
    while results["a"] is None:
        removed = []
        for x in data:
            left, right = x.split(" -> ")
            # AND, OR, LSHIFT, RSHIFT, NOT, Number
            # Base Number Signal
            if left.isdigit():
                results[right] = check_overflow(int(left))
                removed.append(x)
            elif "AND" in left:
                l1, l2 = left.split(" AND ")
                # left of AND is digit
                if l1.isdigit() and results.get(l2) is not None:
                    results[right] = check_overflow(int(l1) & int(results[l2]))
                    removed.append(x)
                # right of AND is digit
                elif l2.isdigit() and results.get(l1) is not None:
                    results[right] = check_overflow(int(l2) & int(results[l1]))
                    removed.append(x)
                # both are digits
                elif l2.isdigit() and l1.isdigit():
                    results[right] = check_overflow(int(l2) & int(l1))
                    removed.append(x)
                # neither are digits
                elif results.get(l1) is not None and results.get(l2) is not None:
                    results[right] = check_overflow(int(results[l1]) & int(results[l2]))
                    removed.append(x)
            elif "OR" in left:
                l1, l2 = left.split(" OR ")
                if results.get(l1) is not None and results.get(l2) is not None:
                    results[right] = check_overflow(int(results[l1]) | int(results[l2]))
                    removed.append(x)
            elif "LSHIFT" in left:
                l1, l2 = left.split(" LSHIFT ")
                if results.get(l1) is not None:
                    results[right] = check_overflow(int(results[l1]) << int(l2))
                    removed.append(x)
            elif "RSHIFT" in left:
                l1, l2 = left.split(" RSHIFT ")
                if results.get(l1) is not None:
                    results[right] = check_overflow(int(results[l1]) >> int(l2))
                    removed.append(x)
            elif "NOT" in left:
                _, l1 = left.split(" ")
                if results.get(l1) is not None:
                    results[right] = check_overflow(~int(results[l1]))
                    removed.append(x)
            elif left.isalpha() and right.isalpha() and results.get(left) is not None:
                results[right] = results[left]

            # alter the list by removing elements we already used
            data[:] = [x for x in data if x not in removed]
            # print(data)

    return results["a"]


part_1_answer = find_signals(data)
print(f"PART 1: {part_1_answer}")

# PART 2


def find_signals_b_overwrite(data, b_overwrite: str):
    results = {"a": None}
    while results["a"] is None:
        removed = []
        for x in data:
            left, right = x.split(" -> ")
            if right == "b":
                results[right] = b_overwrite
            else:
                # AND, OR, LSHIFT, RSHIFT, NOT, Number
                # Base Number Signal
                if left.isdigit():
                    results[right] = check_overflow(int(left))
                    removed.append(x)
                elif "AND" in left:
                    l1, l2 = left.split(" AND ")
                    # left of AND is digit
                    if l1.isdigit() and results.get(l2) is not None:
                        results[right] = check_overflow(int(l1) & int(results[l2]))
                        removed.append(x)
                    # right of AND is digit
                    elif l2.isdigit() and results.get(l1) is not None:
                        results[right] = check_overflow(int(l2) & int(results[l1]))
                        removed.append(x)
                    # both are digits
                    elif l2.isdigit() and l1.isdigit():
                        results[right] = check_overflow(int(l2) & int(l1))
                        removed.append(x)
                    # neither are digits
                    elif results.get(l1) is not None and results.get(l2) is not None:
                        results[right] = check_overflow(
                            int(results[l1]) & int(results[l2])
                        )
                        removed.append(x)
                elif "OR" in left:
                    l1, l2 = left.split(" OR ")
                    if results.get(l1) is not None and results.get(l2) is not None:
                        results[right] = check_overflow(
                            int(results[l1]) | int(results[l2])
                        )
                        removed.append(x)
                elif "LSHIFT" in left:
                    l1, l2 = left.split(" LSHIFT ")
                    if results.get(l1) is not None:
                        results[right] = check_overflow(int(results[l1]) << int(l2))
                        removed.append(x)
                elif "RSHIFT" in left:
                    l1, l2 = left.split(" RSHIFT ")
                    if results.get(l1) is not None:
                        results[right] = check_overflow(int(results[l1]) >> int(l2))
                        removed.append(x)
                elif "NOT" in left:
                    _, l1 = left.split(" ")
                    if results.get(l1) is not None:
                        results[right] = check_overflow(~int(results[l1]))
                        removed.append(x)
                elif (
                    left.isalpha() and right.isalpha() and results.get(left) is not None
                ):
                    results[right] = results[left]

            # alter the list by removing elements we already used
            data[:] = [x for x in data if x not in removed]
            # print(data)

    return results["a"]


part_2_answer = find_signals_b_overwrite(data, part_1_answer)
print(f"PART 2: {part_2_answer}")
