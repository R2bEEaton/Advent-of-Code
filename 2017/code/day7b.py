from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)

supported_by = {}
weights = {}

for line in din:
    weights[line.split()[0]] = int(line.split("(")[1].split(")")[0])
    if line.split()[0] not in supported_by:
        supported_by[line.split()[0]] = ""
    if "-" not in line:
        continue
    for on in line.split('-> ')[1].split(", "):
        supported_by[on] = line.split()[0]

from collections import defaultdict
supports = defaultdict(list)
for disc, supp in supported_by.items():
    supports[supp].append(disc)

start = supports[''][0]

def recurse(disc):
    if len(supports[disc]) == 0:
        return weights[disc]
    
    out = []
    for child in supports[disc]:
        out.append(recurse(child))

    if min(out) != max(out):
        for i, o in enumerate(out):
            if out.count(o) != 1:
                continue
            aocd_submit(weights[supports[disc][i]] - (out[i] - out[(i + 1) % len(out)]))
        exit()

    return weights[disc] + sum(out)

recurse(start)
       
