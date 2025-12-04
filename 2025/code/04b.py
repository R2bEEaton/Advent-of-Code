from helpers.datagetter import aocd_data_in
from helpers.matrix import from_grid

din, aocd_submit = aocd_data_in(split=False, numbers=False)

ans = 0
grid = from_grid(din)

removed = True

while removed:
    removed = False
    for pos, val in grid:
        if val != '@':
            continue
        papers = 0
        for npos, nval in grid.neighbors(pos, diag = True):
            if nval == '@':
                papers += 1
        if papers < 4:
            grid.set(pos, '.')
            removed = True
            ans += 1

aocd_submit(ans)