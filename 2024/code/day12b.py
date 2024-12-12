from collections import defaultdict
from helpers.matrix import DIRS_URDL, DIRS_DIAG, from_grid
from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

M = from_grid(din, data_type=str)

seen = set()
regions_cells = defaultdict(set)

for pos, val in M:
    if pos in seen:
        continue
    seen.add(pos)

    next = [pos]
    region = regions_cells[pos]
    while next:
        curr = next.pop()
        region.add(curr)
        for dir in DIRS_URDL:
            npos = tuple(curr[i] + dir[i] for i in range(2))
            if npos in seen:
                continue
            if M.get(npos) == val:
                seen.add(npos)
                next.append(npos)


def count_continuous(l):
    inside = False
    sides = 0
    for n in l:
        if n == 1 and inside == False:
            inside = True
            sides += 1
        elif n == 0:
            inside = False
    return sides


ans = 0

for pos, vals in regions_cells.items():
    ys = [y for y, x in vals]
    xs = [x for y, x in vals]
    origin = (min(ys), min(xs))
    val = M.get(pos)
    br = (max(ys) + 1, max(xs) + 1)
    sides = 0

    # Count up and down sides for each row
    for y in range(origin[0], br[0]):
        top_edge = []
        bottom_edge = []
        for x in range(origin[1], br[1]):
            if (y, x) not in vals:
                top_edge.append(0)
                bottom_edge.append(0)
                continue
            top_edge.append(1 if (y-1, x) not in vals else 0)
            bottom_edge.append(1 if (y+1, x) not in vals else 0)
        sides += count_continuous(top_edge)
        sides += count_continuous(bottom_edge)

    # Count left and right sides for each column
    for x in range(origin[1], br[1]):
        left_edge = []
        right_edge = []
        for y in range(origin[0], br[0]):
            if (y, x) not in vals:
                left_edge.append(0)
                right_edge.append(0)
                continue
            left_edge.append(1 if (y, x-1) not in vals else 0)
            right_edge.append(1 if (y, x+1) not in vals else 0)
        sides += count_continuous(left_edge)
        sides += count_continuous(right_edge)

    ans += len(vals) * sides

aocd_submit(ans)