from collections import defaultdict
from helpers.matrix import DIRS_URDL, from_grid
from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

M = from_grid(din, data_type=str)

seen = set()
regions = defaultdict(int)
perimeters = defaultdict(int)

for pos, val in M:
    if pos in seen:
        continue
    seen.add(pos)

    next = [pos]
    seen_this_time = set()
    seen_this_time.add(pos)
    while next:
        curr = next.pop()
        for dir in DIRS_URDL:
            npos = tuple(curr[i] + dir[i] for i in range(2))
            if npos in seen_this_time:
                continue
            if M.get(npos) == val:
                seen.add(npos)
                seen_this_time.add(npos)
                next.append(npos)
            else:
                perimeters[pos] += 1
    regions[pos] = len(seen_this_time)

ans = 0
for i, j in zip(regions.values(), perimeters.values()):
    ans += i * j

aocd_submit(ans)