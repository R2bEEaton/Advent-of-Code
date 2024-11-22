from helpers.datagetter import aocd_data_in
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=True, numbers=False)

ans = 0
for line in din:
    id = int(line[-10:-7])

    unenc = ""
    for i in range(len(line[:-10])):
        if not line[i].isalpha():
            continue
        unenc += chr(((ord(line[i]) - 97 + id % 26) % 26) + 97)
    if "north" in unenc and "object" in unenc:
        aocd_submit(id)
        exit()