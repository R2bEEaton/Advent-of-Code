from helpers.matrix import DIRS_URDL, from_grid
from helpers.datagetter import aocd_data_in
import heapq


din, aocd_submit = aocd_data_in(split=False, numbers=False)

M = from_grid(din)

q = []
heapq.heappush(q, (0, (*M.findall("S")[0], 1)))
best_cost = float('inf')
seen = set()

while q:
    cost, curr = heapq.heappop(q)
    pos = curr[:2]

    if curr in seen:
        continue
    seen.add(curr)

    if cost >= best_cost:
        continue

    if M.get(pos) == "E":
        best_cost = min(best_cost, cost)
        continue

    for d in [(curr[2] + 1) % 4, curr[2], (curr[2] - 1) % 4]:
        new_pos = tuple(pos[i] + DIRS_URDL[d][i] for i in range(2))
        if M.get(new_pos) in ".E":
            heapq.heappush(q, (cost + (1001 if d != curr[2] else 1), (*new_pos, d)))

aocd_submit(best_cost)