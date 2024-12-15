from helpers.matrix import from_grid
from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

for i, line in enumerate(din.split()[1:]):
    if line.count("#") == len(line):
        M = from_grid("\n".join(din.split()[0:i+2]))
        break

pos = M.findall('@')[0]
M.set(pos, ".")
moves = "".join(din.split()[i+2:])

dirs = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}


def movable(pos, dir):
    val_at = M.get(pos)
    if val_at == ".":
        M.set(pos, "O")
        return True
    elif val_at == "#":
        return False

    new_pos = tuple(pos[i] + dir[i] for i in range(2))
    new_val = M.get(new_pos)
    while new_val == "O":
        new_pos = tuple(new_pos[i] + dir[i] for i in range(2))
        new_val = M.get(new_pos)
    if movable(new_pos, dir):
        M.set(pos, ".")
        return True
    return False


for move in moves:
    new_pos = tuple(pos[i] + dirs[move][i] for i in range(2))
    val_at = M.get(new_pos)
    if val_at == "#":
        continue
    elif val_at == "O":
        if movable(new_pos, dirs[move]):
            pos = new_pos
    elif val_at == ".":
        pos = new_pos

ans = 0
for box in M.findall("O"):
    ans += 100 * box[0] + box[1]
aocd_submit(ans)