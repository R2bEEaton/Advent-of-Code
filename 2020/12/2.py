import numpy as np


data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())


x = 0
y = 0

offset = [10, 1]


def rotate(value, offset):
    theta = np.deg2rad(value)
    r = np.array(((np.cos(theta), -np.sin(theta)),
                  (np.sin(theta), np.cos(theta))))

    v = np.array((offset[0], offset[1]))
    return [round(r.dot(v)[0]), round(r.dot(v)[1])]

for line in data:
    instr = line[0]
    value = int(line[1:])

    if instr == "F":
        for i in range(0, value):
            x += offset[0]
            y += offset[1]
    if instr == "R":
        offset = rotate(-value, offset)
    if instr == "L":
        offset = rotate(value, offset)

    if instr == "N":
        offset[1] += value
    if instr == "E":
        offset[0] += value
    if instr == "S":
        offset[1] -= value
    if instr == "W":
        offset[0] -= value

print(abs(x) + abs(y))
