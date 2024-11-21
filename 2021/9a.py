grid = []

with open("input9.txt") as f:
    for line in f.readlines():
        temp = []
        for char in line.strip():
            temp.append(int(char))
        temp.append(100)
        grid.append(temp)
    grid.append([100]*(len(grid[0])))

lows = []


def getlow(x ,y):
    global grid
    global lows
    c = grid[x][y]

    if grid[x][y-1] > c and grid[x][y+1] > c and grid[x-1][y] > c and grid[x+1][y] > c and [x, y] not in lows:
        lows.append([x, y])


for x in range(len(grid)-1):
    for y in range(len(grid[0])-1):
        getlow(x, y)

t = 0
for thing in lows:
    t += grid[thing[0]][thing[1]] + 1
print(t)
