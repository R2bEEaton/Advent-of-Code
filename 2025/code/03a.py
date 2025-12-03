from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)

ans = 0

for line in din:
    highest = 0
    for x in range(len(line)):
        for y in range(x + 1, len(line)):
            highest = max(highest, int(line[x] + line[y]))
    ans += highest

aocd_submit(ans)