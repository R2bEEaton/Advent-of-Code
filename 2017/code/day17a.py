from helpers.datagetter import aocd_data_in
from collections import deque

din, aocd_submit = aocd_data_in(split=False, numbers=False)
din = int(din)

spinlock = deque([0])

pos = 0
for i in range(1, 2017+1):
    pos += din
    pos %= i
    spinlock.insert(pos + 1, i)
    pos += 1

aocd_submit(spinlock[spinlock.index(2017) + 1])