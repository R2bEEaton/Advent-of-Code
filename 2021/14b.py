import collections

instructions = {}

with open("input14.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if "-" not in line and line != "":
            template = line
        elif line != "":
            instructions[line.split(" ")[0]] = line.split(" ")[2]

pairs = {}
for i in range(len(template)-1):
    try:
        pairs[template[i]+template[i+1]] += 1
    except:
        pairs[template[i]+template[i+1]] = 1

for t in range(40):
    pairs2 = pairs.copy()
    for key in pairs2:
        pairs[key] -= pairs2[key]
        if pairs[key] < 0:
            pairs.pop(key)
        try:
            pairs[key[0] + instructions[key]] += pairs2[key]
        except:
            pairs[key[0] + instructions[key]] = pairs2[key]
        try:
            pairs[instructions[key] + key[1]] += pairs2[key]
        except:
            pairs[instructions[key] + key[1]] = pairs2[key]

ml = {}
for key in pairs:
    try:
        ml[key[0]] += pairs[key]
    except:
        ml[key[0]] = pairs[key]

least_common = collections.Counter(ml).most_common()[-1]
most_common = collections.Counter(ml).most_common()[0]
print(most_common[1] - least_common[1] + 1)