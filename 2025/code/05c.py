from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

ans = 0

ranges = set()

for line in din:
    if line == []:
        break
    ranges.add(tuple(map(abs, line)))

parens = []

ranges = sorted(ranges)

for x in ranges:
    l, r = x
    parens.append((l, '('))
    parens.append((r, ')'))

new_ranges = set()

l = 0
c = 0
for x, p in sorted(parens):
    if p == '(' and c == 0:
        l = x

    if p == '(':
        c += 1
    else:
        c -= 1
    
    if c == 0:
        new_ranges.add((l, x))

for r in new_ranges:
    ans += r[1] - r[0] + 1

aocd_submit(ans)