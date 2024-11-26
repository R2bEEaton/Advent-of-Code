from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

# elves = [i + 1 for i in range(int(din))]

# i = 1
# while len(elves) > 1:
#     # print(i, elves[i % len(elves)], elves)
#     del elves[i % len(elves)]
#     if i >= len(elves):
#         print(elves)
#         i = 1
#     else:
#         i += 1


def process(x, y, l, i):
    if l == 1:
        return x
    if l % 2 != 0:
        return process(x + 2 ** i, y, l // 2, i + 1)
    return process(x, y - (2 ** (i - 1)), l // 2, i + 1)


aocd_submit(process(1, int(din), int(din), 1))
