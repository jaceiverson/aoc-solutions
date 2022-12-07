"""Helper functions to automate AOC"""

import pathlib
from typing import Any
from time import perf_counter_ns


def read(path: str) -> str:
    """General Purpose Read a Text file and Return"""
    return pathlib.Path(path).read_text()


def chunks(l: list, n: int = 5) -> list[list[Any]]:
    """
    params:
        l: taks in a list (or list like object)
        n: takes an int: default = 5 this is how big the smaller
            chunks will be
    returns:
        a list of lists with the smaller lists being size n
    """
    return [l[i : i + n] for i in range(0, len(l), n)]


"""
WRAPPERS
"""
# a timer wrapper to time functions in ns
def mytime(func):
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        end = perf_counter_ns()
        print(f"{func.__name__:>10} : {end-start:>10} ns")
        return result

    return wrapper


# average time decorator
def avgtime(func):
    def wrapper(*args, **kwargs):
        run_times = kwargs["run_times"] if "run_times" in kwargs else 1
        times = []
        for _ in range(run_times):
            start = perf_counter_ns()
            func()
            end = perf_counter_ns()
            times.append(end - start)
        print(f"{func.__name__:>10} : {sum(times)/len(times):>10} ns")

    return wrapper
