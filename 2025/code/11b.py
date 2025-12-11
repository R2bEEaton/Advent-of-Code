from collections import defaultdict
from helpers.datagetter import aocd_data_in
import networkx

din, aocd_submit = aocd_data_in(split=True, numbers=False)

G = networkx.DiGraph()
for line in din:
    nodes = line.split(": ")
    for node in nodes[1].split(" "):
        G.add_edge(nodes[0], node)

topo = list(networkx.topological_sort(G))


def getPaths(start, end):
    paths = defaultdict(int)
    paths[end] = 1
   
    for i in range(topo.index(end) - 1, -1, -1):
        node = topo[i]
        
        for adj in G.neighbors(node):
            paths[node] += paths[adj]

        if node == start:
            return paths[node]
    return 0
        

ans = (getPaths("svr", "fft") * getPaths("fft", "dac") * getPaths("dac", "out")) \
    + (getPaths("svr", "dac") * getPaths("dac", "fft") * getPaths("fft", "out"))
aocd_submit(ans)