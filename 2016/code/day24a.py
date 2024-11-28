from helpers.datagetter import aocd_data_in
import networkx as nx
from helpers.matrix import Matrix

din, aocd_submit = aocd_data_in(split=True, numbers=False)

grid = Matrix((len(din), len(din[0])))
nodes = {}

G = nx.Graph()

for y in range(len(din)):
    for x in range(len(din[0])):
        grid[(y, x)] = din[y][x]
        if din[y][x].isnumeric():
            G.add_node(int(din[y][x]))
            nodes[int(din[y][x])] = (y, x)

for node in G.nodes:
    seen = set(nodes[node])
    explore = [nodes[node]]
    steps = 0
    while explore:
        new_explore = []
        leave = False
        for pos in explore:
            if pos in seen:
                continue
            seen.add(pos)

            val = grid[pos]
            if val.isnumeric() and int(val) in G.nodes and int(val) != node:
                G.add_edge(node, int(val), weight=steps)

            for val, pos_1 in grid.neighbors(pos):
                if val != "#":
                    new_explore.append(tuple(pos_1))
            if leave:
                break
        explore = new_explore
        steps += 1

from networkx.classes.function import path_weight
from itertools import permutations

min_weight = float('inf')
for perm in permutations([x for x in G.nodes if x != 0]):
    try:
        weight = path_weight(G, tuple([0] + list(perm)), weight="weight")
        min_weight = min(min_weight, weight)
    except:
        None

aocd_submit(min_weight)