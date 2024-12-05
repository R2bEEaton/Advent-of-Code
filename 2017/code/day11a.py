from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

dirs = {
    "ne": (0, -1, 1),
    "n": (-1, 0, 1),
    "nw": (-1, 1, 0),
    "sw": (0, 1, -1),
    "s": (1, 0, -1),
    "se": (1, -1, 0)
}

pos = [0, 0, 0]


def cube_dist(a):
    return (abs(a[0]) + abs(a[1]) + abs(a[2])) / 2


for move in din.split(","):
    dir = dirs[move]
    pos[0] += dir[0]
    pos[1] += dir[1]
    pos[2] += dir[2]

aocd_submit(int(cube_dist(pos)))