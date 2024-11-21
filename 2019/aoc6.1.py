input = """input redacted"""

dicty = {}

for thing in input.split("\n"):
    d = thing.split(")")
    dicty[d[1]] = d[0]

print(dicty)

x = 0

for thing in dicty:
    print(thing, "ree")
    com = 0
    new = thing
    while com == 0:
        new = dicty[new]
        x += 1
        if new == "COM":
            com = 1

print(x)