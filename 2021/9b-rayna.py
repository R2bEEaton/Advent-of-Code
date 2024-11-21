grid = [[int(char) for char in line.strip()]+[9] for line in open("input9.txt")]
grid.append([9]*len(grid[0]))

basin_sizes = []
points = []


def getbasin(x ,y):
    global grid
    global points
    global point_count

    points.append([x, y])

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i != 0 != j != 0) and not all([i == 0, j == 0]):
                if grid[x+i][y+j] < 9 and [x+i, y+j] not in points:
                    points.append([x+i, y+j])
                    point_count += 1
                    getbasin(x+i, y+j)


for x in range(len(grid)-1):
    for y in range(len(grid[0])-1):
        if grid[x][y] < 9 and [x, y] not in points:
            point_count = 1
            getbasin(x, y)
            basin_sizes.append(point_count)

basin_sizes.sort()
print(basin_sizes[-3]*basin_sizes[-2]*basin_sizes[-1])
