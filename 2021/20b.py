enh = []

with open("input20.txt") as f:
    lines = f.readlines()
    for char in lines[0].strip():
        if char == "#":
            enh.append(1)
        else:
            enh.append(0)
    grid = []
    for line in lines[2:]:
        temp = []
        for char in line.strip():
            if char == "#":
                temp.append(1)
            else:
                temp.append(0)
        grid.append(temp)


def pad(igrid, times, e):
    old = igrid
    for l in range(times):
        ngrid = []
        ngrid.append([e for i in range(len(old)+2)])
        for i in old:
            ngrid.append([e] + i + [e])
        ngrid.append([e for i in range(len(old)+2)])
        old = ngrid
    return old


def unpad(igrid, times):
    old = igrid
    for l in range(times):
        ngrid = []
        for i in old[1:-2]:
            ngrid.append(i[1:-2])
        old = ngrid
    return old


grid = pad(grid, 3, 0)
for e in range(1, 51):
    new_grid = [[0 for i in range(len(grid))] for j in range(len(grid))]
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid)-1):
            o = ""
            for i in range(-1, 2):
                for j in range(-1, 2):
                    o += str(grid[y+i][x+j])
            new_grid[y][x] = enh[int(o, 2)]
    grid = pad(unpad(new_grid, 1), 3, e % 2)


t = 0
for line in new_grid:
    for char in line:
        if char == 1:
            t += 1

print(t)
