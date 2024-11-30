from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=True)
curr = din[0]

seen = set()

def evolve(curr):
    idx = curr.index(max(curr))
    target = curr[idx]
    curr[idx] = 0

    for i in range(1, target + 1):
        curr[(idx + i) % len(curr)] += 1

    return curr

tot = 0
while tuple(curr) not in seen:
    seen.add(tuple(curr))
    curr = evolve(curr)
    tot += 1

seen.clear()
tot = 0
while tuple(curr) not in seen:
    seen.add(tuple(curr))
    curr = evolve(curr)
    tot += 1

aocd_submit(tot)