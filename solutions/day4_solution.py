from utils import *

data=read("../input/day4_input")

def add(pos, direction):
    return (pos[0]+direction[0], pos[1]+direction[1])

def sol1():
    count = 0
    directions=[(1,-1), (1,0), (1,1), (0,1), (0,-1), (-1,0), (-1,1), (-1,-1)]
    for y in range(len(data)):
        for x in range(len(data[y])):
            for direction in directions:
                if searchInDirection(data, "XMAS", (x,y), direction): count+=1
    return count

def sol2():
    count = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x]=="A":
                pos=(x,y)
                #search up
                if getIfInside(data, add(pos, (1,1)))=="S" and getIfInside(data, add(pos, (-1,1)))=="S":
                    if getIfInside(data, add(pos, (1,-1)))=="M" and getIfInside(data, add(pos, (-1,-1)))=="M": count+=1
                #search right
                if getIfInside(data, add(pos, (1,1)))=="S" and getIfInside(data, add(pos, (1,-1)))=="S":
                    if getIfInside(data, add(pos, (-1,1)))=="M" and getIfInside(data, add(pos, (-1,-1)))=="M": count += 1
                #search left
                if getIfInside(data, add(pos, (-1,1)))=="S" and getIfInside(data, add(pos, (-1,-1)))=="S":
                    if getIfInside(data, add(pos, (1,1)))=="M" and getIfInside(data, add(pos, (1,-1)))=="M": count += 1
                #search down
                if getIfInside(data, add(pos, (1,-1)))=="S" and getIfInside(data, add(pos, (-1,-1)))=="S":
                    if getIfInside(data, add(pos, (1,1)))=="M" and getIfInside(data, add(pos, (-1,1)))=="M": count += 1
    return count

print(f"Solution 1: {sol1()}")
print(f"Solution 2: {sol2()}")
