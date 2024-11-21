data = []

with open("1.txt") as f:
    for thing in f.readlines():
        data.append(thing.strip())

for thing in data:
    thing = thing.strip()
    over = 2020 - int(thing)
    if str(over) in data:
        print(over * int(thing))
        break
