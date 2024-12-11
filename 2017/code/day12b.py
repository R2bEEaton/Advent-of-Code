from helpers.datagetter import aocd_data_in
import networkx

din, aocd_submit = aocd_data_in(split=True, numbers=True)

G = networkx.Graph()

for line in din:
    for num in line[1:]:
        G.add_edge(line[0], num)

aocd_submit(len(list(networkx.connected_components(G))))