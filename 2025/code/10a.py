import heapq
from helpers.datagetter import aocd_data_in
import tqdm

din, aocd_submit = aocd_data_in(split=True, numbers=False)

ans = 0

def getFewest(curr, goal, buttons):
    pq = []

    # Originally ran without the seen set, but added it right after and saw a massive speedup so I kept it thinking I'd need it in Part Two
    seen = set()
    heapq.heappush(pq, (0, curr))
    
    while True:
        presses, curr = heapq.heappop(pq)
        if curr not in seen:
            seen.add(curr)
        else:
            continue
        for seq in buttons:
            # Was originally using tuples, but switched to bitwise operations for speed
            new_curr = curr ^ seq
            if new_curr == goal:
                return presses + 1
            heapq.heappush(pq, (presses + 1, new_curr))


for line in tqdm.tqdm(din):
    # What is with me and unnecessarily complicated one liners this year??
    goal, buttons = tuple([0 if x == "." else 1 for x in line.split(" ")[0][1:-1]]), [[int(y) for y in x[1:-1].split(",")] for x in line.split(" ")[1:-1]]
    # print("Goal", sum([(2 ** i) * x for i, x in enumerate(goal)]))
    # print([sum([(2 ** y) * 1 for y in x]) for x in buttons])
    ans += getFewest(0, sum([(2 ** i) * x for i, x in enumerate(goal)]), [sum([(2 ** y) * 1 for y in x]) for x in buttons])

aocd_submit(ans)