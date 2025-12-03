from helpers.datagetter import aocd_data_in
import re

din, aocd_submit = aocd_data_in(split=False, numbers=False)

ans = 0

for id in din.split(","):
    id1, id2 = id.split("-")
    for x in range(int(id1), int(id2) + 1):
        xs = str(x)
        if re.match(r"(.+?)\1+$", xs):
            ans += x

aocd_submit(ans)