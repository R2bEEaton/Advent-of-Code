line1 = "input redacted"
line2 = "input redacted"

x = 0
y = 0
list1 = []
list2 = []
for thing in line1.split(","):
    if thing[0] == "R":
        for i in range(0, int(thing[1:])):
            list1.append((x, y))
            x+=1
    if thing[0] == "L":
        for i in range(0, int(thing[1:])):
            list1.append((x, y))
            x -= 1
    if thing[0] == "U":
        for i in range(0, int(thing[1:])):
            list1.append((x, y))
            y += 1
    if thing[0] == "D":
        for i in range(0, int(thing[1:])):
            list1.append((x, y))
            y -= 1

x = 0
y = 0
for thing in line2.split(","):
    if thing[0] == "R":
        for i in range(0, int(thing[1:])):
            list2.append((x, y))
            x+=1
    if thing[0] == "L":
        for i in range(0, int(thing[1:])):
            list2.append((x, y))
            x -= 1
    if thing[0] == "U":
        for i in range(0, int(thing[1:])):
            list2.append((x, y))
            y += 1
    if thing[0] == "D":
        for i in range(0, int(thing[1:])):
            list2.append((x, y))
            y -= 1

import tqdm

print(list1)
print(list2)

for thing in list1:
    for thing2 in list2:
        if thing == thing2:
            print(thing)
