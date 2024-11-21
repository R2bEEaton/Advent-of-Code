import itertools

locations = []
dirs = {}

with open("input9.txt") as f:
    for line in f.readlines():
        line = line.split()
        if line[0] not in locations:
            locations.append(line[0])
        if line[2] not in locations:
            locations.append(line[2])
        dirs[line[0] + " " + line[2]] = int(line[4])
        dirs[line[2] + " " + line[0]] = int(line[4])

ll = list(itertools.permutations(locations))
dl = []

for thing in ll:
    d = 0
    for i in range(len(thing)):
        try:
            d += dirs[thing[i] + " " + thing[i+1]]
        except:
            None
    dl.append(d)

print(min(dl))
