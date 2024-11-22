from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

facing = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
pos = [0, 0]

for move in din.split(", "):
    if move[0] == 'R':
        facing += 1
    else:
        facing -= 1
    facing %= 4

    pos[0] += dirs[facing][0] * int(move[1:])
    pos[1] += dirs[facing][1] * int(move[1:])

aocd_submit(abs(pos[0]) + abs(pos[1]))
