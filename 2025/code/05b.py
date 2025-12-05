from helpers.datagetter import aocd_data_in
import itertools

din, aocd_submit = aocd_data_in(split=True, numbers=True)

ans = 0

ranges = set()

for line in din:
    if line == []:
        break
    ranges.add(tuple(map(abs, line)))

overlap = True
while overlap:
    overlap = False
    for pair in itertools.combinations(ranges, r=2):
        a, b = sorted(pair)
        # A and B overlap
        if b[0] <= a[1] and b[1] >= a[1]:
            ranges.remove(a)
            ranges.remove(b)
            ranges.add((a[0], b[1]))
            overlap = True
            break
        # B is contained in A
        if a[0] <= b[0] and a[1] >= b[1]:
            ranges.remove(b)
            overlap = True
            break

for r in ranges:
    ans += r[1] - r[0] + 1

aocd_submit(ans)