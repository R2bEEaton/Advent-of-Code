from helpers.datagetter import aocd_data_in
from astar import AStar
import math

din, aocd_submit = aocd_data_in(split=False, numbers=False)

def good(x, y):
    return str(bin(x*x + 3*x + 2*x*y + y + y*y + int(din))[2:]).count('1') % 2 == 0

class MazePath(AStar):
    def distance_between(self, n1, n2):
        return math.dist(n1, n2)
    
    def heuristic_cost_estimate(self, current, goal):
        return self.distance_between(current, goal)
    
    def neighbors(self, node):
        x, y = node
        return [(nx, ny) for nx, ny in[(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]if 0 <= nx and 0 <= ny and good(nx, ny)]

m = MazePath().astar((1, 1), (31, 39))
aocd_submit(len(list(m)) - 1)