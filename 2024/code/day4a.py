from helpers.datagetter import aocd_data_in
from helpers.matrix import Matrix

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

M = Matrix((len(din), len(din[0])))

for y in range(len(din)):
    for x in range(len(din[0])):
        M[(y, x)] = din[y][x]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

for y in range(len(din)):
    for x in range(len(din[0])):
        for dir in dirs:
            build = ""
            for i in range(4):
                n_char = M[(y+dir[0]*i,x+dir[1]*i)]
                if n_char != None:
                    build += M[(y+dir[0]*i,x+dir[1]*i)]
                else:
                    break
            if build == "XMAS":
                ans += 1

aocd_submit(ans)