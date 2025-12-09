from helpers.datagetter import aocd_data_in
import itertools

din, aocd_submit = aocd_data_in(split=True, numbers=True)

ans = 0

for pair in itertools.combinations(din, r=2):
    a, b = pair
    size = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
    ans = max(ans, size)

aocd_submit(ans)