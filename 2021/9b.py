grid = []

with open("input9.txt") as f:
    for line in f.readlines():
        temp = []
        for char in line.strip():
            temp.append(int(char))
        temp.append(100)
        grid.append(temp)
    grid.append([100]*(len(grid[0])))

lows = {}


def getlow(x ,y):
    global grid
    global lows
    c = grid[x][y]
    f = False

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i != 0 != j != 0) and not all([i == 0, j == 0]) and grid[x+i][y+j] < c:
                f = True
                return getlow(x+i, y+j)

    if not f:
        return [x, y]


for x in range(len(grid)-1):
    for y in range(len(grid[0])-1):
        if grid[x][y] != 9:
            l = " ".join(map(str, getlow(x, y)))
            try:
                lows[l] += 1
            except:
                lows[l] = 1

anss = []
for thing in lows:
    anss.append(lows[thing])
anss.sort()
print(anss[-3]*anss[-2]*anss[-1])
