import heapq
from helpers.matrix import DIRS_URDL, from_grid
from helpers.datagetter import aocd_data_in
import math
import tqdm

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

for pos, val in tqdm.tqdm(M):
    if val == "#":
        continue
    for new_pos, new_val in M:
        dist = abs(pos[0] - new_pos[0]) + abs(pos[1] - new_pos[1])
        if dist <= 20:
            if new_val not in [None, "#"]:
                saves = new_val - val - dist
                if saves >= 100:
                    saves_100 += 1

aocd_submit(saves_100)