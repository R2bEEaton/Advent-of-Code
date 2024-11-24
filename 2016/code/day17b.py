from helpers.datagetter import aocd_data_in
from astar import AStar
import math
import hashlib

din, aocd_submit = aocd_data_in(split=False, numbers=False)
    

def neighbors(node):
    x, y, key = node

    hashed = hashlib.md5(bytes(key, encoding='UTF-8')).hexdigest()[:4]
    doors = [True if x in 'bcdef' else False for x in hashed]
    directions = [(x, y - 1, 'U'), (x, y + 1, 'D'), (x - 1, y, 'L'), (x + 1, y, 'R')]
    valid = []
    for i, door in enumerate(doors):
        if door:
            valid.append(directions[i])

    return [(nx, ny, key + udlr) for nx, ny, udlr in valid if 0 <= nx <= 3 and 0 <= ny <= 3]


def is_goal_reached(current, goal):
    x, y, _ = current
    return (x, y) == (3, 3)


explore = [(0, 0, din)]
max_len = 0
i = 0
while explore:
    new_explore = []
    for item in explore:
        if is_goal_reached(item, (3, 3, 0)):
            max_len = max(max_len, len(item[2]) - len(din))
            continue
        new_explore.extend(neighbors(item))
    explore = new_explore
    i += 1

aocd_submit(max_len)