from helpers.datagetter import aocd_data_in
import networkx

din, aocd_submit = aocd_data_in(split=True, numbers=False)

G = networkx.DiGraph()

for line in din:
    nodes = line.split(": ")
    for node in nodes[1].split(" "):
        G.add_edge(nodes[0], node)

all_paths = list(networkx.all_simple_paths(G, source="you", target="out"))

aocd_submit(len(all_paths))