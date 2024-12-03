from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)
ans = 0


def is_safe(line):
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

    return all_decreasing or all_increasing


for line in din:
    if is_safe(line):
        ans += 1
        continue

    for i in range(len(line)):
        line_copy = line.copy()
        del line_copy[i]
        if is_safe(line_copy):
            ans += 1
            break

aocd_submit(ans)