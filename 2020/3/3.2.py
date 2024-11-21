data = []

with open("3.txt") as f:
    for line in f.readlines():
        data.append(line)


def slope(right, down):
    pointer = 0
    trees = 0

    for line in data[::down]:
        line = line.strip()
        pos = line[pointer]
        if pos == "#":
            trees += 1

        pointer += right

        if pointer > len(line)-1:
            pointer -= len(line)

    return trees


print(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))
