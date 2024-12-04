from helpers.datagetter import aocd_data_in
from helpers.matrix import Matrix

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

M = Matrix((len(din), len(din[0])))

for y in range(len(din)):
    for x in range(len(din[0])):
        M[(y, x)] = din[y][x]

patterns = [
    ['S S',
     ' A ',
     'M M'],

    ['M S',
     ' A ',
     'M S'],

    ['M M',
     ' A ',
     'S S'],

    ['S M',
     ' A ',
     'S M']
]

for y in range(len(din)):
    for x in range(len(din[0])):
        for pat in patterns:
            tot = 0
            for dy in range(3):
                build = ""
                for dx in range(3):
                    if dx == 1 and dy in [0, 2]:
                        build += ' '
                        continue
                    elif dx in [0, 2] and dy == 1:
                        build += ' '
                        continue
                    next_c = M[(y+dy,x+dx)]
                    if next_c != None:
                        build += M[(y+dy,x+dx)]
                    else:
                        break
                if build == pat[dy]:
                    tot += 1
            if tot == 3:
                ans += 1

aocd_submit(ans)