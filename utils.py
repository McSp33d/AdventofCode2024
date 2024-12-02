def read(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def read_int_lists(filename):
    data=read(filename)
    return [[int(i) for i in line.split(" ")] for line in data]