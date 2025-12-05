from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

ans = 0

ranges = []
init = True

for line in din:
    if line == []:
        init = False
        continue
    if init:
        ranges.append(list(map(abs, line)))
    else:
        for r in ranges:
            if line[0] >= r[0] and line[0] <= r[1]:
                ans += 1
                break

aocd_submit(ans)