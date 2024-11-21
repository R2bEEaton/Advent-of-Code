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
            x += 1
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

i = -1422
j = -957

list3 = """(-1422, -957)
(-1527, -957)
(-1527, -989)
(-1422, -989)
(-1305, -901)
(-1724, -687)
(-1834, -613)
(-1609, 441)
(-1569, 689)
(-1569, 484)
(-1774, 484)
(-2264, 498)
(-2291, 594)
(-2299, 594)
(-2396, 1011)
(-2396, 1037)
(-1678, 1850)"""

for thing in list3.split("\n"):
    print(eval(thing))
    print(list1.index(eval(thing)) + list2.index(eval(thing)))


"(-1422, -957)"
