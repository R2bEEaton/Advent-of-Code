from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)
din = int(din)

corner = int(din ** (1/2))
corner -= 1 if corner % 2 == 0 else 0
pos = [-(corner // 2), (corner // 2) + 1]
print(corner, pos)

diff = din - corner ** 2
print(diff)

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
facing = 0
cnt = 1

while (corner ** 2) + cnt != din:
    print((corner ** 2) + cnt, cnt, facing)
    pos[0] += dirs[facing][0]
    pos[1] += dirs[facing][1]
    cnt += 1
    if cnt % (corner + 1) == 0:
        facing += 1

aocd_submit(abs(pos[0]) + abs(pos[1]))