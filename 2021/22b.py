grid = []

with open("input22.txt") as f:
    for line in f.readlines():
        line = line.strip()
        x, y, z = int(line.split("=")[1].split("..")[0]), int(line.split("=")[2].split("..")[0]), int(line.split("=")[3].split("..")[0])
        dx, dy, dz = int(line.split("=")[1].split("..")[1].split(",")[0]), int(line.split("=")[2].split("..")[1].split(",")[0]), int(line.split("=")[3].split("..")[1])
        on = line.split()[0] == "on"
        grid.append([on, [x, y, z], [dx, dy, dz]])


print(grid)

def overlap(first, second):
    x, y, z = first[1]
    dx, dy, dz = [x + 1 for x in first[2]]
    a, b, c = second[1]
    da, db, dc = [x + 1 for x in second[2]]
    return max(min(da, dx)-max(a, x), 0) * max(min(db, dy)-max(b, y), 0) * max(min(dc, dz)-max(c, z), 0)


def vol(first): return (first[2][0]+1 - first[1][0]) * (first[2][1]+1 - first[1][1]) * (first[2][2]+1 - first[1][2])


t = 0

for i in range(len(grid)):
    if grid[i][0]:
        t += vol(grid[i])
        for j in range(i-1, -1, -1):
            if grid[j][0]:
                t -= overlap(grid[i], grid[j])
            else:
                break
    else:
        for j in range(i-1, -1, -1):
            t -= overlap(grid[i], grid[j])
            print("Overlap: ", overlap(grid[i], grid[j]))
    print(t)

print(t)
