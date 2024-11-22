from helpers.datagetter import aocd_data_in
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=True, numbers=False)

letters = [defaultdict(int) for _ in range(len(din[0]))]

for line in din:
    for i, c in enumerate(line):
        letters[i][c] += 1

ans = ""
for col in letters:
    items = list(col.items())
    items.sort(key= lambda x: x[1])
    ans += items[0][0]

aocd_submit(ans)