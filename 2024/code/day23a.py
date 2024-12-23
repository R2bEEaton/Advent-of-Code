from helpers.datagetter import aocd_data_in
import networkx

din, aocd_submit = aocd_data_in(split=True, numbers=False)

G = networkx.Graph()

for line in din:
    a, b = line.split("-")
    G.add_edge(a, b)


def get_paths(start, goal, cost, G):
    q = [[start]]
    paths = set()
    while q:
        path = q.pop(0)
        curr = path[-1]

        if len(path) > cost:
            continue

        for nei in G.neighbors(curr):
            if nei == goal and len(path) == 3:
                paths.add(tuple(sorted(path)))
                continue
            if nei in path:
                continue
            q.append(path + [nei])
    return paths


tot = set()
for n in G:
    if not n.startswith('t'):
        continue
    tot |= get_paths(n, n, 4, G)

aocd_submit(len(tot))