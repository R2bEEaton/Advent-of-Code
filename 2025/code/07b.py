from helpers.datagetter import aocd_data_in
from helpers.matrix import from_grid
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=False, numbers=False)

grid = from_grid(din)

ans = 0
beams = defaultdict(int)
beams[list(grid.findall('S'))[0]] = 1


def get_next_beams(beam):
    new_beams = []
    if grid.get((beam[0] + 1, beam[1])) == "^":
        if grid._is_in_bounds((beam[0] + 1, beam[1] - 1)):
            new_beams.append((beam[0] + 1, beam[1] - 1))
        if grid._is_in_bounds((beam[0] + 1, beam[1] + 1)):
            new_beams.append((beam[0] + 1, beam[1] + 1))
    else:
        new_beams.append((beam[0] + 1, beam[1]))
    return new_beams


y = list(beams.keys())[0][0]
while y < grid.size[0]:
    new_beams = defaultdict(int)
    for beam in beams:
        for nbeam in get_next_beams(beam):
            new_beams[nbeam] += beams[beam]

    beams = new_beams
    y += 1

aocd_submit(sum(beams.values()))