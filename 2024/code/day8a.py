from helpers.datagetter import aocd_data_in
from helpers.matrix import *
from itertools import combinations
import numpy as np

din, aocd_submit = aocd_data_in(split=False, numbers=False)

M = from_grid(din)

antennae = defaultdict(list)

for pos, val in M:
    if val != ".":
        antennae[val].append(pos.copy())

antinodes = set()


def in_bounds(pos):
    return M._is_in_bounds(pos)


for a, poses in antennae.items():
    for comb in combinations(poses, 2):
        diff1 = np.subtract(comb[0], comb[1])
        diff2 = np.subtract(comb[1], comb[0])

        ant1 = np.add(comb[0], diff1)
        ant2 = np.add(comb[1], diff2)

        if in_bounds(ant1):
            antinodes.add(tuple(ant1))
            
        if in_bounds(ant2):
            antinodes.add(tuple(ant2))

aocd_submit(len(antinodes))