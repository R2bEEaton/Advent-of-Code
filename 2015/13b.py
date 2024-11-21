import itertools

happ = {}
people = []

with open("input13.txt") as f:
    for line in f.readlines():
        line = line.split()
        val = int(line[3])
        if line[2] == "lose":
            val *= -1
        line[-1] = line[-1].replace(".", "")
        happ[line[0] + " " + line[-1]] = val
        if line[0] not in people:
            people.append(line[0])
        if line[-1] not in people:
            people.append(line[-1])

for person in people:
    happ[person + " You"] = 0
    happ["You " + person] = 0

people.append("You")

ll = list(itertools.permutations(people))

t = 0

for order in ll:
    c = 0
    for i in range(-1, len(order)-1):
        c += happ[order[i] + " " + order[i+1]]
        c += happ[order[i+1] + " " + order[i]]
    if c > t:
        t = c

print(t)
