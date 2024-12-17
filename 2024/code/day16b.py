from helpers.matrix import DIRS_URDL, from_grid
from helpers.datagetter import aocd_data_in
import heapq
import tqdm


din, aocd_submit = aocd_data_in(split=False, numbers=False)

M = from_grid(din)


def get_lowest_cost(start, goal, best):
    q = []
    heapq.heappush(q, (0, start))
    best_cost = float('inf')
    best_dir = -1
    seen = set()

    while q:
        cost, curr = heapq.heappop(q)
        pos = curr[:2]

        if curr in seen:
            continue
        seen.add(curr)

        if cost >= best_cost or cost > best:
            continue

        if (*pos, curr[2]) == goal or (pos[:2] == goal[:2] and goal[2] < 0):
            best_cost = min(best_cost, cost)
            best_dir = curr[2]
            continue

        for d in {(curr[2] + 1) % 4, curr[2], (curr[2] - 1) % 4}:
            new_pos = tuple(pos[i] + DIRS_URDL[d][i] for i in range(2))
            if M.get(new_pos) in {".", "E"}:
                heapq.heappush(q, (cost + (1001 if d != curr[2] else 1), (*new_pos, d)))

    return best_cost, best_dir, seen

best, _, seen = get_lowest_cost((*M.findall("S")[0], 1), (*M.findall("E")[0], -1), float('inf'))
ans = 0

for intermediate in tqdm.tqdm(set([loc[:2] for loc in seen])):
    S_i, bd, _ = get_lowest_cost((*M.findall("S")[0], 1), (*intermediate, -1), best)
    i_E, _, _ = get_lowest_cost((*intermediate, bd), (*M.findall("E")[0], -1), best - S_i)
    ans += S_i + i_E == best

aocd_submit(ans)