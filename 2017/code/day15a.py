from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

factors = [16807, 48271]
rem = 2147483647

A, B = (line[0] for line in din)

ans = 0

for i in range(40_000_000):
    A *= factors[0]
    A %= rem

    B *= factors[1]
    B %= rem

    if A & 0xFFFF == B & 0xFFFF:
        ans += 1

aocd_submit(ans)