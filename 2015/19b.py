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
            goal = line

mol = "e"


def next_mol(iters, mol):
    global goal
    if mol == goal:
        print(mol)
        print(iters)
        exit()
    if iters > 4:
        return
    else:
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

        for thing in t:
            print(thing)
            next_mol(iters+1, thing)


next_mol(0, mol)
