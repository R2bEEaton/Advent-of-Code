import heapq
from helpers.matrix import DIRS_URDL, from_grid
from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

M = from_grid(din)
best = len(M.findall(".")) + 1

seen = set()
pos = M.findall("S")[0]
cost = 0

while M.get(pos) != "E":
    M.set(pos, cost)
    seen.add(pos)
    for nei, val in M.neighbors(pos):
        if val is None:
            continue
        if nei not in seen and val in ".E":
            pos = nei
            break
    cost += 1
M.set(pos, cost)

saves_100 = 0

for pos, val in M:
    if val == "#":
        continue
    for d in DIRS_URDL:
        new_pos = tuple(pos[i] + d[i] + d[i] for i in range(2))
        if M.get(new_pos) not in [None, "#"]:
            saves = M.get(new_pos) - M.get(pos) - 2
            if saves >= 100:
                saves_100 += 1

aocd_submit(saves_100)