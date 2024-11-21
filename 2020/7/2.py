data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())

bags = {}

for line in data:
    outer = line.split(" bags contain ")[0]
    inner = line.split(" bags contain ")[1].replace(".", "").split(", ")
    for i in range(0, len(inner)):
        inner[i] = " ".join(inner[i].split(" ")[:-1])

    bags[outer] = inner

print(bags)

count = 0


def tree(bag):
    global count
    try:
        for thing in bags[bag]:
            for i in range(0, int(thing.split(" ")[0])):
                tree(" ".join(thing.split(" ")[1:]))
                count += 1
    except:
        None


tree("shiny gold")
print(count)


