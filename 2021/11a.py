grid = []

with open("input11.txt") as f:
    for line in f.readlines():
        temp = []
        for char in line.strip():
            temp.append(int(char))
        temp.append(10000)
        grid.append(temp)
    grid.append([10000]*(len(grid[0])))

fs = 0
fps = []


def flash(x, y):
    global grid
    global pts
    if grid[x][y] > 9 and [x, y] not in pts and grid[x][y] < 10000:
        pts.append([x, y])
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    None
                else:
                    grid[x+i][y+j] += 1
                    flash(x+i, y+j)


for steps in range(100):
    pts = []
    for x in range(len(grid)-1):
        for y in range(len(grid[0])-1):
            grid[x][y] += 1
            flash(x, y)

    for x in range(len(grid)-1):
        for y in range(len(grid[0])-1):
            if grid[x][y] > 9:
                fs += 1
                grid[x][y] = 0

print(fs)
