from helpers.datagetter import aocd_data_in
import itertools

din, aocd_submit = aocd_data_in(split=True, numbers=True)

ans = 0

for line in din:
    good = True
    for comb in itertools.permutations([0, 1, 2], 3):
        if line[comb[0]] + line[comb[1]] <= line[comb[2]]:
            good = False
            break
    if good:
        ans += 1

aocd_submit(ans)