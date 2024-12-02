from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)
ans = 0

for line in din:
    all_increasing = True
    all_decreasing = True

    for i in range(len(line)  -1):
        if not (-3 <= (line[i+1] - line[i]) <= -1):
            all_decreasing = False
            break

    for i in range(len(line)  -1):
        if not (1 <= (line[i+1] - line[i]) <= 3):
            all_increasing = False
            break

    if all_decreasing or all_increasing:
        ans += 1

aocd_submit(ans)