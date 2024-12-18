import heapq
from helpers.matrix import DIRS_URDL, Matrix
from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

M = Matrix((71, 71))

for t, line in enumerate(din):
    M.set((line[1], line[0]), t + 1)


def check_after(X):
    q = []
    heapq.heappush(q, (0, (0, 0, 0)))
    best_cost = float('inf')
    seen = set()

    while q:
        cost, curr = heapq.heappop(q)
        pos = curr[:2]
        t = curr[2]

        if pos in seen:
            continue
        seen.add(pos)

        if cost > best_cost:
            continue

        if 0 < M.get(pos) <= X:
            continue

        if pos == (70, 70):
            best_cost = min(best_cost, cost)
            continue

        for nei, val in M.neighbors(pos):
            if val is None:
                continue
            heapq.heappush(q, (cost + 1, (*nei, t + 1)))

    return best_cost != float('inf')


# Wasn't actually solved like this, I did it by spot checking 2000 and 3000 and noticed it got blocked between that, so I kept lowering the range until I found it.
# I could code this up but I want to go to bed, so I just put it like this for completeness.
x = 0
while check_after(x):
    x += 1

aocd_submit(",".join([str(i) for i in din[x-1]]))
