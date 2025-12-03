from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)

ans = 0

for line in din:
    curr = ""
    start = 0
    line_list = list(map(int, list(line)))
    while len(curr) != 12:
        search = line_list[start : len(line) - (12 - len(curr)) + 1]
        idx = line_list.index(max(search), start)
        curr += line[idx]
        start = idx + 1
    ans += int(curr)

aocd_submit(ans)