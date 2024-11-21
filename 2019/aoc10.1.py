input = """input redacted"""

list2 = []

inp = input.split("\n")

for x in range(0, 34):
    for y in range(0, 34):
        if inp[x][y] == "#":
            list2.append((x, y))

print(list2)

import random
import math

topscore = 0
pos = ""

perms = {}

i = 0

while len(list2) > 0:
    for thing2 in list2:
        perms[math.sqrt(((thing2[0] - 20)**2)+(thing2[1] - 23)**2)] = (thing2, math.atan2(thing2[1] - 23, thing2[0] - 20))
        list2.remove(thing2)
        if i == 199:
            print(thing2)
        i += 1

print(list2)


print(perms)
out = []
for thing in sorted(perms):
     out.append((thing, perms[thing]))

print(out[200])

"23 20"