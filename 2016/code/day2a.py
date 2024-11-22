from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
pos = [1, 1]

passcode = ""

for line in din:
    for dir in line:
        if pos[0] == 0 and dir == "U":
            continue
        if pos[0] == 2 and dir == "D":
            continue
        if pos[1] == 0 and dir == "L":
            continue
        if pos[1] == 2 and dir == "R":
            continue
        pos[0] += dirs[dir][0]
        pos[1] += dirs[dir][1]
    passcode += str(keypad[pos[0]][pos[1]])

aocd_submit(passcode)