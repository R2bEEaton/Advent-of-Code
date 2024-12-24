from helpers.datagetter import aocd_data_in
import networkx as nx
from pyvis.network import Network

din, aocd_submit = aocd_data_in(split=True, numbers=False)

wires = {}
gates = []

G = nx.DiGraph()

initial = True
for line in din:
    if line == "":
        initial = False
        continue
    
    if initial:
        wire, val = line.split(": ")
        wires[wire] = int(val)
    else:
        wire_a, gate, wire_b, _, wire = line.split(" ")
        gates.append((wire_a, gate, wire_b, wire))
        G.add_edge(wire_a, f"{wire_a}_{wire_b}_{gate}")
        G.add_edge(wire_b, f"{wire_a}_{wire_b}_{gate}")
        G.add_edge(f"{wire_a}_{wire_b}_{gate}", wire)

# Plot with pyvis
net = Network(
    directed = True,
    select_menu = True, # Show part 1 in the plot (optional)
    filter_menu = True, # Show part 2 in the plot (optional)
)
net.show_buttons() # Show part 3 in the plot (optional)
net.from_nx(G) # Create directly from nx graph
net.show('day24vis.html', notebook=False)