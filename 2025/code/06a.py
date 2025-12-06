from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)
# Just the quickest way in the moment I could think of to get the last line
ops = aocd_data_in(split=True, numbers=False)[0][-1].split()

ans = 0

for y in range(len(din[0])):
    s = ""
    for x in range(len(din) - 1):
        s += str(din[x][y])
        s += ops[y]
    ans += eval(str(s[:-1]))

aocd_submit(ans)