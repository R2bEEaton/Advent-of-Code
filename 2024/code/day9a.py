from helpers.datagetter import aocd_data_in
import re

din, aocd_submit = aocd_data_in(split=False, numbers=False)

ans = 0

file = True
data = []
id = 0

for num in din:
    num = int(num)
    for _ in range(num):
        data.append(id if file else '.')
    if file:
        id += 1
    file = not file

l = 0
r = len(data) -1


def swap(data, l, r):
    temp = data[l]
    data[l] = data[r]
    data[r] = temp

while l <= r:
    while data[l] != ".":
        l += 1
    while data[r] == ".":
        r -= 1
    swap(data, l, r)

swap(data, l, r)


for i, num in enumerate(data):
    if num == ".":
        break
    ans += i * int(num)

aocd_submit(ans)