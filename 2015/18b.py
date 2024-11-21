grid = []

with open("input18.txt") as f:
    for line in f.readlines():
        temp = []
        for thing in line.strip():
            if thing == "#":
                temp.append(1)
            else:
                temp.append(0)
        temp.append(0)
        grid.append(temp)
    grid.append([0]*(len(grid)+1))


def nbrs(x, y):
    global grid
    n = 0
    n += grid[x-1][y-1]
    n += grid[x-1][y]
    n += grid[x-1][y+1]
    n += grid[x][y-1]
    n += grid[x][y+1]
    n += grid[x+1][y-1]
    n += grid[x+1][y]
    n += grid[x+1][y+1]
    return n


for i in range(100):
    new_grid = [[0]*len(grid) for _ in range(len(grid))]
    grid[0][0] = 1
    grid[len(grid)-2][0] = 1
    grid[0][len(grid)-2] = 1
    grid[len(grid)-2][len(grid)-2] = 1

    for x in range(len(grid[0])-1):
        for y in range(len(grid[0])-1):
            if grid[x][y] == 1 and nbrs(x, y) not in [2, 3]:
                new_grid[x][y] = 0
            elif grid[x][y] == 1:
                new_grid[x][y] = 1
            if grid[x][y] == 0 and nbrs(x, y) == 3:
                new_grid[x][y] = 1

    new_grid[0][0] = 1
    new_grid[len(grid)-2][0] = 1
    new_grid[0][len(grid)-2] = 1
    new_grid[len(grid)-2][len(grid)-2] = 1
    grid = new_grid

t = 0
for thing in grid:
    t += sum(thing)
print(t)
