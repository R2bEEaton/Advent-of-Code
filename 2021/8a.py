with open("input8.txt") as f:
    inps = list(map(str, f.readlines()))

t = 0
for line in inps:
    for thing in line.split("| ")[1].split():
        if len(thing) in [2, 3, 4, 7]:
            t += 1

print(t)
