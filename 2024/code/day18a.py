import heapq
from helpers.matrix import DIRS_URDL, Matrix
from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

M = Matrix((71, 71))

for t, line in enumerate(din):
    M.set((line[1], line[0]), t + 1)

q = []
heapq.heappush(q, (0, (0, 0, 0)))
best_cost = float('inf')
seen = set()

while q:
    cost, curr = heapq.heappop(q)
    pos = curr[:2]
    t = curr[2]

    if curr in seen:
        continue
    seen.add(curr)

    if cost > best_cost:
        continue

    if 0 < M.get(pos) <= 1024:
        continue

    if pos == (70, 70):
        best_cost = min(best_cost, cost)
        continue

    for nei, val in M.neighbors(pos):
        if val is None:
            continue
        heapq.heappush(q, (cost + 1, (*nei, t + 1)))

aocd_submit(best_cost)