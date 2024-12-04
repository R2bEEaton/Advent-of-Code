import re
from helpers.datagetter import aocd_data_in
from collections import deque

din, aocd_submit = aocd_data_in(split=False, numbers=True)

size = 256
L = deque(x for x in range(size))

def reverse(arr, l, r):
    for i in range((r-l+1) // 2):
        temp = arr[(l+i)%size]
        arr[(l+i)%size] = arr[(r-i)%size]
        arr[(r-i)%size] = temp

pos = 0
skip_size = 0
for num in din[0]:
    reverse(L, pos, pos + num - 1)
    pos += num + skip_size
    skip_size += 1

aocd_submit(L[0] * L[1])