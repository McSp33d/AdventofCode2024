def read(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def readMap(filename):
    return [[c for c in line] for line in read("../input/day6_input")]

def readIntLists(filename, delimiter=" "):
    data=readWords(filename, delimiter)
    output=[]
    for line in data:
        current_line=[]
        for word in line:
            try:
                current_line.append(int(word))
            except:
                pass
        output.append(current_line)
    return output

def readWords(filename, delimiter=" "):
    data=read(filename)
    output=[]
    for line in data:
        current_line=[]
        for word in line.split(delimiter):
            if word:
                current_line.append(word)
        output.append(current_line)
    return output


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


def isInside(map, pos):
    if 0 <= pos[0] < len(map[1]) and 0 <= pos[1] < len(map):
        return True
    return False


def setIfInside(map, pos, char):
    if isInside(map, pos):
        map[pos[1]][pos[0]] = char



def searchInDirection(data, word, pos, direction):
    for char in word:
        if char != getIfInside(data, pos):
            return False
        pos = (pos[0]+direction[0], pos[1]+direction[1])
    return True


def DFS(state, get_next_states, is_goal):
    stack=[state]
    while stack:
        state=stack.pop()
        if is_goal(state):
            return state
        for next_state in get_next_states(state):
            stack.append(next_state)
    return None


def BFS(state, get_next_states, is_goal):
    queue=[state]
    while queue:
        state=queue.pop(0)
        if is_goal(state):
            return state
        for next_state in get_next_states(state):
            queue.append(next_state)
    return None