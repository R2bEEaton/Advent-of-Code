from helpers.datagetter import aocd_data_in
import networkx as nx

din, aocd_submit = aocd_data_in(split=True, numbers=False)

G = nx.Graph()

for line in din:
    a, b = line.split("-")
    G.add_edge(a, b)

cliques = nx.find_cliques(G)
largest = max(cliques, key=len)

aocd_submit(",".join(sorted(largest)))