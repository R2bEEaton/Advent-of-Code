from helpers.datagetter import aocd_data_in
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=True, numbers=True)
ans = 0
after = defaultdict(set)
in_rules = True
unique_nums = set()


def valid(line):
    for i, x in enumerate(line):
        for y in line[:i]:
            if y in after[x]:
                return False
    return True


bad = []

for line in din:
    if len(line) == 0:
        in_rules = False
        continue
    
    if in_rules:
        after[line[0]].add(line[1])
        unique_nums.add(line[0])
        continue
    
    if not valid(line):
        bad.append(line)


# Copied due to time and testing, cause I didn't know whether it would work
# https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if arr[i] in after[arr[i+1]]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break


for thing in bad:
    bubble_sort(thing)
    ans += thing[len(thing) // 2]

aocd_submit(ans)