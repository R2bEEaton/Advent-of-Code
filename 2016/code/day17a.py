from helpers.datagetter import aocd_data_in
from astar import AStar
import math
import hashlib

din, aocd_submit = aocd_data_in(split=False, numbers=False)

class MazePath(AStar):
    def distance_between(self, n1, n2):
        x1, y1, _ = n1
        x2, y2, _ = n2
        return math.dist((x1, y1), (x2, y2))
    
    def heuristic_cost_estimate(self, current, goal):
        return self.distance_between(current, goal)
    
    def neighbors(self, node):
        x, y, key = node

        hashed = hashlib.md5(bytes(key, encoding='UTF-8')).hexdigest()[:4]
        doors = [True if x in 'bcdef' else False for x in hashed]
        directions = [(x, y - 1, 'U'), (x, y + 1, 'D'), (x - 1, y, 'L'), (x + 1, y, 'R')]
        valid = []
        for i, door in enumerate(doors):
            if door:
                valid.append(directions[i])

        return [(nx, ny, key + udlr) for nx, ny, udlr in valid if 0 <= nx <= 3 and 0 <= ny <= 3]
    
    def is_goal_reached(self, current, goal):
        x, y, _ = current
        return (x, y) == (3, 3)

m = MazePath().astar((0, 0, din), (3, 3, 0))
aocd_submit(list(m)[-1][2][len(din):])