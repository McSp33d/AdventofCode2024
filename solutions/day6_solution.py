from utils import *
import numpy as np

map=readMap("../input/day6_input")

guard_pos=np.array([-1,-1])
for y, line in enumerate(map):
    if "^" in line:
        guard_pos = np.array([line.index("^"), y])
        break

direction=np.array([0,-1])

def turn_right(direction):
    return np.array([-direction[1], direction[0]])

def make_guard_move(map, guard_pos, direction):
    next_pos=getIfInside(map, guard_pos+direction, " ")
    if next_pos=="#":
        return guard_pos, turn_right(direction)
    else:
        return guard_pos+direction, direction

#checks if guard moves in a loop
def containsLoop(map, guard_pos, direction, positions_encountered):
    visited=positions_encountered.copy()
    while isInside(map, guard_pos):
        guard_pos, direction = make_guard_move(map, guard_pos, direction)
        new_pos=(tuple(guard_pos), tuple(direction))
        if new_pos in visited:
            return True
        visited.add(new_pos)
    return False

guard_position_direction=[]
while isInside(map, guard_pos):
    guard_position_direction.append([guard_pos, direction])
    guard_pos, direction = make_guard_move(map, guard_pos, direction)
    setIfInside(map, guard_pos, "X")

count=1 #1 since initial position won't be counted
all_guard_positions=[]
for y, line in enumerate(map):
    count+=line.count("X")
print(f"Solution1: {count+1}")

c=0
tested_obstacle_positions=set()
positions_encountered=set()
for i, position in enumerate(guard_position_direction):
    guard_pos, direction = position
    obstacle_pos=tuple(guard_pos+direction)
    if getIfInside(map, obstacle_pos, " ")=="#":
        continue
    if obstacle_pos in tested_obstacle_positions:
        continue
    tested_obstacle_positions.add(obstacle_pos)
    setIfInside(map, obstacle_pos, "#")
    if containsLoop(map, guard_pos, direction, positions_encountered):
        c+=1
    setIfInside(map, obstacle_pos, ".")
    positions_encountered.add((tuple(guard_pos), tuple(direction)))

print(f"Solution2: {c}")
