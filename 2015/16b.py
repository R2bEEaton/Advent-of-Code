sues = []

with open("input16.txt") as f:
    for line in f.readlines():
        line = line.split()
        attrib = {}
        attrib[line[2].replace(":","")] = line[3].replace(",","")
        attrib[line[4].replace(":","")] = line[5].replace(",","")
        attrib[line[6].replace(":","")] = line[7].replace(",","")
        sues.append(attrib)

m = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

match = {}
for line in m.split("\n"):
    line = line.split()
    match[line[0].replace(":","")] = line[1]

for i in range(len(sues)):
    m = 0
    for e in sues[i]:
        if e in ['cats', 'trees'] and sues[i][e] > match[e]:
            m += 1
        elif e in ['pomeranians', 'goldfish'] and sues[i][e] < match[e]:
            m += 1
        elif sues[i][e] == match[e]:
            m += 1
    if m == 3:
        print(i+1)
