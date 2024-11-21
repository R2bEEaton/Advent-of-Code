import collections

instructions = {}

with open("input14.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if "-" not in line and line != "":
            template = line
        elif line != "":
            instructions[line.split(" ")[0]] = line.split(" ")[2]

for t in range(10):
    inserts = []
    for i in range(len(template)-1):
        if template[i]+template[i+1] in instructions.keys():
            inserts.append(instructions[template[i]+template[i+1]])
        else:
            inserts.append("")

    new = []
    for i in range(len(template)):
        new.append(template[i])
        try:
            if inserts[i] != "":
                new.append(inserts[i])
        except:
            None
    template = "".join(new)

least_common = collections.Counter(template).most_common()[-1]
most_common = collections.Counter(template).most_common()[0]
print(most_common[1] - least_common[1])