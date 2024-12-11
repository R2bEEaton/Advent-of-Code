from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

factors = [16807, 48271]
rem = 2147483647

A, B = (line[0] for line in din)


def get_next(gen, factor, mult):
    gen *= factor
    gen %= rem
    while gen % mult != 0:
        gen *= factor
        gen %= rem
    return gen


ans = 0

for i in range(5_000_000):
    A = get_next(A, factors[0], 4)
    B = get_next(B, factors[1], 8)

    # print(A, B)
    # exit()

    if A & 0xFFFF == B & 0xFFFF:
        ans += 1

aocd_submit(ans)