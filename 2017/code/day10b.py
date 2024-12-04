import re
from helpers.datagetter import aocd_data_in
from collections import deque

din, aocd_submit = aocd_data_in(split=False, numbers=False)

din = [ord(x) for x in din] + [17, 31, 73, 47, 23]

size = 256
L = deque(x for x in range(size))

def reverse(arr, l, r):
    for i in range((r-l+1) // 2):
        temp = arr[(l+i)%size]
        arr[(l+i)%size] = arr[(r-i)%size]
        arr[(r-i)%size] = temp

pos = 0
skip_size = 0
for _ in range(64):
    for num in din:
        reverse(L, pos, pos + num - 1)
        pos += num + skip_size
        skip_size += 1

L = list(L)
out = ""
for i in range(0, 256, 16):
    res = 0
    for x in L[i:i+16]:
        res ^= x
    out += hex(res)[2:].zfill(2)

aocd_submit(out)