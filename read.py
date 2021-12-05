def read(path):
    with open(path) as f:
        rules = f.read()
    return rules
