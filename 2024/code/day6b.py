from helpers.datagetter import aocd_data_in
from helpers.matrix import Matrix
import copy

din, aocd_submit = aocd_data_in(split=True, numbers=False)
M = Matrix((len(din), len(din[0])))
ans = 0

for y in range(len(din)):
    for x in range(len(din[0])):
        M[(y, x)] = din[y][x]
        if din[y][x] == "^":
            pos = [y, x]

dirs = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def loops(obstruction, pos):
    dir = 0
    N = copy.deepcopy(M)
    N[obstruction] = "#"
    seen = set([tuple([*pos, dir])])
    while N[pos]:
        forward = [pos[0] + dirs[dir][0], pos[1] + dirs[dir][1]]
        if N[forward] == "#":
            dir += 1
            dir %= 4
        else:
            pos = forward
        if tuple([*pos, dir]) in seen:
            return True
        seen.add(tuple([*pos, dir]))
    return False


for y in range(len(din)):
    for x in range(len(din[0])):
        if [y, x] == pos:
            continue
        if loops((y, x), pos):
            ans += 1

aocd_submit(ans)