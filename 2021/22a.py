grid = {}

with open("input22.txt") as f:
    for line in f.readlines():
        line = line.strip()
        x, y, z = int(line.split("=")[1].split("..")[0]), int(line.split("=")[2].split("..")[0]), int(line.split("=")[3].split("..")[0])
        dx, dy, dz = int(line.split("=")[1].split("..")[1].split(",")[0]), int(line.split("=")[2].split("..")[1].split(",")[0]), int(line.split("=")[3].split("..")[1])

        if not (x < -50 or x > 50 or y < -50 or y > 50 or z < -50 or z > 50 or dx < -50 or dx > 50 or dy < -50 or dy > 50 or dz < -50 or dz > 50):
            on = line[1] == "n"
            for i in range(x, dx+1):
                for j in range(y, dy+1):
                    for k in range(z, dz+1):
                        if on:
                            grid[f"{i},{j},{k}"] = 1
                        else:
                            grid[f"{i},{j},{k}"] = 0

t = 0
for i in grid:
    if grid[i] == 1:
        t += 1

print(t)
