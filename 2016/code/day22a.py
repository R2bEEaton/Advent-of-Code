from helpers.datagetter import aocd_data_in
import itertools

din, aocd_submit = aocd_data_in(split=True, numbers=True)
din = din[2:]

ans = 0

for a, b in itertools.combinations(din, 2):
    ans += a[3] != 0 and a[3] <= b[4]
    ans += b[3] != 0 and b[3] <= a[4]

aocd_submit(ans)