grid = []

with open("input25.txt") as f:
    for line in f.readlines():
        line = line.strip()
        temp = []
        for char in line:
            if char == ".":
                temp.append(0)
            elif char == ">":
                temp.append(1)
            else:
                temp.append(2)
        grid.append(temp)

print(grid)


def move(grid):
    new_grid = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            match grid[row][col]:
                case 1:
                    if grid[row][(col+1) % len(grid[row])] == 0:
                        new_grid[row][col] = 0
                        new_grid[row][(col + 1) % len(grid[row])] = 1
                    else:
                        new_grid[row][col] = 1
                case 2:
                    new_grid[row][col] = 2

    grid = new_grid.copy()
    new_grid = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            match grid[row][col]:
                case 1:
                    new_grid[row][col] = 1
                case 2:
                    if grid[(row+1) % len(grid)][col] == 0:
                        new_grid[row][col] = 0
                        new_grid[(row+1) % len(grid)][col] = 2
                    else:
                        new_grid[row][col] = 2

    return new_grid

found = False
i = 0
while not found:
    i += 1
    old_grid = grid.copy()
    grid = move(grid)
    if grid == old_grid:
        print(i)
        exit()