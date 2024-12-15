from helpers.matrix import from_grid
from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

for i, line in enumerate(din.split()[1:]):
    if line.count("#") == len(line):
        M = from_grid("\n".join(din.split()[0:i+2]).replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@."))
        break

pos = M.findall('@')[0]
M.set(pos, ".")
moves = "".join(din.split()[i+2:])
boxes = M.findall('[')[0]

dirs = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}


def move_lr(pos, dir):
    orig_pos = pos
    while M.get(pos) not in "#.":
        pos = tuple(pos[i] + dir[i] for i in range(2))
    if M.get(pos) == "#":
        return
    
    if dir == (0, -1):
        M.set(pos, "[")
    else:
        M.set(pos, "]")
    pos = tuple(pos[i] - dir[i] for i in range(2))
    while pos != orig_pos:
        if M.get(pos) == "[":
            M.set(pos, "]")
        else:
            M.set(pos, "[")
        pos = tuple(pos[i] - dir[i] for i in range(2))
    M.set(pos, ".")


def check_safe(pos, dir):
    # print("checking", pos, dir)
    
    good = []
    prev = tuple(pos[i] - dir[i] for i in range(2))
    if M.get(pos) == ".":
        if M.get(prev) == "]":
            if M.get((pos[0], pos[1] - 1)) == ".":
                # print("free", pos)
                return [pos]
        elif M.get(prev) == "[":
            if M.get((pos[0], pos[1] + 1)) == ".":
                # print("free", pos)
                return [pos]
        else:
            # print("free", pos)
            return [pos]
    
    if M.get(pos) == "#":
        # print("bad", pos)
        return ["bad"]

    new_pos = tuple(pos[i] + dir[i] for i in range(2))
    # print("new_pos", new_pos)
    if M.get(pos) == "[":
        # print("checking above [")
        # print("checking directly above [", new_pos)
        good.extend(check_safe(new_pos, dir))
        # print("checking right and above ]", (new_pos[0], new_pos[1] + 1))
        good.extend(check_safe((new_pos[0], new_pos[1] + 1), dir))
    elif M.get(pos) == "]":
        # print("checking above ]")
        # print("checking directly above ]", new_pos)
        good.extend(check_safe(new_pos, dir))
        # print("checking left and above ]", (new_pos[0], new_pos[1] - 1))
        good.extend(check_safe((new_pos[0], new_pos[1] - 1), dir))
    # print("checked ahead", good)
    return good


def move_ud(pos, dir):
    locs = check_safe(pos, dir)
    # print(locs)
    while locs:
        if "bad" in locs:
            break
        if locs == [pos]:
            break
        for loc in set(locs):
            from_loc = tuple(loc[i] - dir[i] for i in range(2))
            M.set(loc, M.get(from_loc))
            M.set(from_loc, ".")
        locs = check_safe(pos, dir)
        # print(locs)


for move in moves:
    # print(move)
    new_pos = tuple(pos[i] + dirs[move][i] for i in range(2))
    val_at = M.get(new_pos)
    if val_at == "#":
        continue
    elif val_at in "[]":
        if move in "<>":
            # print("move lr")
            move_lr(new_pos, dirs[move])
            if M.get(new_pos) == ".":
                pos = new_pos
        else:
            # print("move ud", pos)
            move_ud(new_pos, dirs[move])
            if M.get(new_pos) == ".":
                pos = new_pos
    elif val_at == ".":
        pos = new_pos
    # print(M, pos, move)
    # input("continue?")

ans = 0
for box in M.findall("["):
    ans += 100 * box[0] + box[1]
aocd_submit(ans)