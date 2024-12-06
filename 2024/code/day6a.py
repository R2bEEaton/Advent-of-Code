from helpers.datagetter import aocd_data_in
from helpers.matrix import Matrix

din, aocd_submit = aocd_data_in(split=True, numbers=False)

M = Matrix((len(din), len(din[0])))
ans = 0

for y in range(len(din)):
    for x in range(len(din[0])):
        M[(y, x)] = din[y][x]
        if din[y][x] == "^":
            pos = [y, x]

dir = 0
dirs = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

seen = set([tuple(pos)])

while M[pos]:
    forward = [pos[0] + dirs[dir][0], pos[1] + dirs[dir][1]]
    if M[forward] == "#":
        dir += 1
        dir %= 4
    else:
        pos = forward
        M[pos] = "X"
    seen.add(tuple(pos))

aocd_submit(len(seen) - 1)