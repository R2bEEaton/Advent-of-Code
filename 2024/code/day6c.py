import copy
from helpers.datagetter import aocd_data_in
from collections import defaultdict
from itertools import combinations
import re
from helpers.matrix import Matrix

din, aocd_submit = aocd_data_in(split=True, numbers=False)

M = Matrix((len(din), len(din[0])))

ans = 0
obstacles = []

for y in range(len(din)):
    for x in range(len(din[0])):
        M[(y, x)] = din[y][x]
        if din[y][x] == "^":
            pos = [y, x]
        if din[y][x] == "#":
            obstacles.append((y, x))

print(M)
for comb in combinations(obstacles, 3):
    comb = sorted(comb, key=lambda a: a[0] + (a[1] / len(din[0])))
    print(comb)

aocd_submit(ans)