rules = {}

with open("input19.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if "=>" in line:
            try:
                rules[line.split(" => ")[0]].append(line.split(" => ")[1])
            except:
                rules[line.split(" => ")[0]] = [line.split(" => ")[1]]
        elif line != "":
            mol = line

i = 0
t = []

while i < len(mol):
    m = ""
    try:
        if mol[i] + mol[i+1] in rules.keys():
            m = mol[i] + mol[i+1]
            s = i
            i += 2
        else:
            raise IndexError
    except:
        m = mol[i]
        s = i
        i += 1

    if m in rules.keys():
        for thing in rules[m]:
            t.append(mol[:s] + thing + mol[i:])

u = []
for thing in t:
    if thing not in u:
        u.append(thing)

print(len(u))
