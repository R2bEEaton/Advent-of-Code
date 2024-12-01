from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

left = []
right = []

ans = 0
for line in din:
    left.append(line[0])
    right.append(line[1])

left = sorted(left)
right = sorted(right)

for i in range(len(left)):
    ans += abs(left[i] - right[i])

aocd_submit(ans)