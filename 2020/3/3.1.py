data = []

with open("3.txt") as f:
    for line in f.readlines():
        data.append(line)

pointer = 0
trees = 0

for line in data:
    line = line.strip()
    pos = line[pointer]
    if pos == "#":
        trees += 1

    print(pos)

    pointer += 3

    if pointer > len(line)-1:
        pointer -= len(line)

print(trees)
