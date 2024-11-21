xs = []
ys = []
grid = []
instructions = []

with open("input13.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith("fold"):
            instructions.append(line.split(" ")[2])
        elif line == "":
            None
        else:
            xs.append(int(line.split(",")[0]))
            ys.append(int(line.split(",")[1]))

for i in range(max(ys)+1):
    temp = []
    for j in range(max(xs)+1):
        temp.append(".")
    grid.append(temp)

for i in range(len(xs)):
    grid[ys[i]][xs[i]] = "X"

for instruction in instructions:
    val = int(instruction.split("=")[1])
    if instruction.startswith("y"):
        new_grid = []
        for y in range(val, len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "X":
                    grid[val-(y-val)][x] = "X"
        for y in range(val):
            new_grid.append(grid[y])
        grid = new_grid
    else:
        new_grid = []
        for y in range(len(grid)):
            for x in range(val, len(grid[0])):
                if grid[y][x] == "X":
                    grid[y][val-(x-val)] = "X"
        for y in range(len(grid)):
            temp = []
            for x in range(val):
                temp.append(grid[y][x])
            new_grid.append(temp)
        grid = new_grid

for y in grid:
    for x in y:
        if x == "X":
            print("#", end="")
        else:
            print(" ", end="")
    print()
