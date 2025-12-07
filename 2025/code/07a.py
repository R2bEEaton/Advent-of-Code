from helpers.datagetter import aocd_data_in
from helpers.matrix import from_grid

din, aocd_submit = aocd_data_in(split=False, numbers=False)

grid = from_grid(din)

ans = 0
beams = list(grid.findall('S'))

y = beams[0][0]
while y < grid.size[0]:
    new_beams = set()
    for beam in beams:
        if grid.get((beam[0] + 1, beam[1])) == "^":
            ans += 1
            if grid._is_in_bounds((beam[0] + 1, beam[1] - 1)):
                new_beams.add((beam[0] + 1, beam[1] - 1))
            if grid._is_in_bounds((beam[0] + 1, beam[1] + 1)):
                new_beams.add((beam[0] + 1, beam[1] + 1))
        else:
            new_beams.add((beam[0] + 1, beam[1]))
    y += 1
    beams = list(new_beams)

aocd_submit(ans)