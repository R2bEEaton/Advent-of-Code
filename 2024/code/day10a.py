from helpers.datagetter import aocd_data_in
from helpers.matrix import *

din, aocd_submit = aocd_data_in(split=False, numbers=False)

M = from_grid(din, data_type=int)
trailheads = M.findall(0)
ans = 0

for head in trailheads:
    bfs = [head]
    ans = 0
    seen = set()
    while bfs:
        new_bfs = []
        for thing in bfs:
            if tuple(thing) in seen:
                continue
            seen.add(tuple(thing))
            if M.get(thing) == 9:
                ans += 1
                continue
            for val, pos in M.neighbors(thing):
                if val == M.get(thing) + 1:
                    new_bfs.append(pos)
        bfs = new_bfs

aocd_submit(ans)