"""Helper functions to automate AOC"""

def read(path: str) -> str:
    """General Purpose Read a Text file and Return"""
    with open(path) as f:
        rules = f.read()
    return rules
