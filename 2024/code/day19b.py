from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)

patterns = sorted(din[0].split(", "), key=lambda x: len(x))
designs = din[2:]


def make_design(curr, design, avail, seen):
    if curr in seen:
        return seen[curr]

    if curr == design:
        return 1

    tot = 0
    for n in avail:
        if design.startswith(curr + n):
            tot += make_design(curr + n, design, avail, seen)
    seen[curr] = tot
    return tot


ans = 0
for i, design in enumerate(designs):
    ans += make_design("", design, patterns, dict())

aocd_submit(ans)