import copy


data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())

field = []
for rows in data:
    row = []
    for chair in rows:
        row.append(chair)
    field.append(row)


def aut(space):
    new_space = copy.deepcopy(space)
    for x in range(0, len(space)):
        for y in range(0, len(space[x])):
            neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if not (x+i < 0 or x+i > len(space)-1) and not (y+j < 0 or y+j > len(space[x])-1) and\
                            not (i == 0 and j == 0):
                        if space[x+i][y+j] == "#":
                            neighbors += 1

            if space[x][y] == "L" and neighbors == 0:
                new_space[x][y] = "#"
            elif space[x][y] == "#" and neighbors >= 4:
                new_space[x][y] = "L"


    print(new_space)
    return new_space


while True:
    old_space = copy.deepcopy(field)
    field = aut(field)
    if old_space == field:
        filled = 0
        for x in range(0, len(field)):
            for y in range(0, len(field[x])):
                if field[x][y] == "#":
                    filled += 1
        print(filled)
        break
