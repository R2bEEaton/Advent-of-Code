data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())


x = 0
y = 0

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
pointer = 1

for line in data:
    instr = line[0]
    value = int(line[1:])

    if instr == "F":
        x += dir[pointer][0] * value
        y += dir[pointer][1] * value
    if instr == "R":
        pointer += int(value/90)
        if pointer > 3:
            pointer = abs(pointer-4)
    if instr == "L":
        pointer -= int(value/90)
        if pointer < 0:
            pointer = pointer+4

    if instr == "N":
        y += value
    if instr == "E":
        x += value
    if instr == "S":
        y -= value
    if instr == "W":
        x -= value

print(abs(x) + abs(y))
