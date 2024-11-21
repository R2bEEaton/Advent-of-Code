data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())

bags = {}

for line in data:
    outer = line.split(" bags contain ")[0]
    inner = line.split(" bags contain ")[1].replace(".", "").split(", ")
    for i in range(0, len(inner)):
        inner[i] = " ".join(inner[i].split(" ")[1:-1])

    for thing in inner:
        try:
            bags[thing].append(outer)
        except:
            bags[thing] = [outer]

print(bags)

nodes = []


def tree(bag):
    global nodes
    try:
        for thing in bags[bag]:
            tree(thing)
    except:
        None
    if bag not in nodes:
        nodes.append(bag)


tree("shiny gold")
print(len(nodes)-1)
