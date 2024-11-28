from helpers.datagetter import aocd_data_in
import itertools

din, aocd_submit = aocd_data_in(split=True, numbers=True)
din = din[2:]

positions = {}

for a in din:
    for b in din:
        if a == b:
            continue
        # print(a, b)
        if a[3] != 0 and a[3] <= b[4]:
            break
    else:
        if a[3] != 0:
            positions[(a[0], a[1])] = "#"
        else:
            positions[(a[0], a[1])] = "_"
        continue
    positions[(a[0], a[1])] = "."

for y in range(a[1] + 1):
    for x in range(a[0] + 1):
        print(positions[(x, y)], end="")
    print()
