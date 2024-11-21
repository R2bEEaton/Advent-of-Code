input = """input redacted"""

dicty = {}

for thing in input.split("\n"):
    d = thing.split(")")
    dicty[d[1]] = d[0]

print(dicty)

x = 0

list1 = []
list2 = []

com = 0
new = "SAN"
while com == 0:
    new = dicty[new]
    list1.append(new)
    x += 1
    #change to first thing that matches in the list below
    if new == "COM":
        com = 1


com = 0
new = "YOU"
while com == 0:
    new = dicty[new]
    list2.append(new)
    x += 1
    if new == "COM":
        com = 1

for thing in list1:
    for thing2 in list2:
        if thing == thing2:
            print(thing)
print(x)