from helpers.datagetter import aocd_data_in
import itertools

din, aocd_submit = aocd_data_in(split=True, numbers=True)

ans = 0

for lines in itertools.batched(din, n=3):
    for x in range(3):
        good = True
        for comb in itertools.permutations([0, 1, 2], 3):
            if lines[comb[0]][x] + lines[comb[1]][x] <= lines[comb[2]][x]:
                good = False
                break
        if good:
            ans += 1

aocd_submit(ans)