from helpers.datagetter import aocd_data_in
from collections import deque
import math

din, aocd_submit = aocd_data_in(split=False, numbers=False)
din = int(din)


def check_naive(din):
    elves = list(range(1, din + 1))

    while len(elves) != 1:
        del elves[len(elves) // 2]
        saved = elves[0]
        del elves[0]
        elves.append(saved)

    return elves[0]


def check_pattern(din):
    exponent = math.log(din, 3)
    closest = 3 ** int(exponent)
    curr = closest
    ans = 0
    while curr != din:
        if ans < closest:
            ans += 1
        else:
            ans += 2
        curr += 1
    return din if ans == 0 else ans


# for i in range(1, 1000):
#     if check_naive(i) != check_better(i):
#         print("WRong", i, check_naive(i), check_pattern(i))

aocd_submit(check_pattern(din))