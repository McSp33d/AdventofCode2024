def read(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def read_int_lists(filename):
    data=read(filename)
    return [[int(i) for i in line.split(" ")] for line in data]


def getIfInside(data, pos, return_char=""):
    """
    Return the character at a given position in a 2D list.

    If the position is out of bounds, return `return_char` (default: "") instead.

    :param data: The 2D list to search in.
    :param pos: A pair (x, y) that represents the position.
    :param return_char: The character to return if the position is out of bounds.
    :return: The character at the given position, or `return_char`.
    """
    x,y = pos
    if (0 <= y < len(data)) and (0 <= x < len(data[y])):
        return data[y][x]
    else:
        return return_char


def searchInDirection(data, word, pos, direction):
    for char in word:
        if char != getIfInside(data, pos):
            return False
        pos = (pos[0]+direction[0], pos[1]+direction[1])
    return True