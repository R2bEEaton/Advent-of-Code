import time
start = time.time()

grid = []

with open("input15.txt") as f:
    for line in f.readlines():
        temp = []
        for char in line.strip():
            temp.append(int(char))
        grid.append(temp)

import numpy as np
orig = np.array(grid)
orig -= 1
new = orig.copy()
new = np.append(new, (orig+1), axis=1)
new = np.append(new, (orig+2), axis=1)
new = np.append(new, (orig+3), axis=1)
new = np.append(new, (orig+4), axis=1)
orig = new.copy()
new = np.append(new, (orig+1), axis=0)
new = np.append(new, (orig+2), axis=0)
new = np.append(new, (orig+3), axis=0)
new = np.append(new, (orig+4), axis=0)

grid = []
for y in range(len(new)):
    temp = []
    for x in range(len(new)):
        if new[y][x] > 8:
            temp.append(new[y][x] % 9 + 1)
        else:
            temp.append(new[y][x] + 1)
    temp.append(100)
    grid.append(temp)
grid.append([100]*len(grid[0]))

unvisited = []
visited = []
distances = {}
for i in range(len(grid)-1):
    for j in range(len(grid)-1):
        unvisited.append([i, j])
        distances[str("[%s, %s]" % (i, j))] = 10000000
distances["[0, 0]"] = 0
undistances = {}
undistances["[0, 0]"] = 0


def dists(dists):
    global unvisited
    global visited
    global distances
    global undistances
    for key in dists:
        pos = eval(key)
        if pos not in visited:
            oldval = distances[key]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    val = grid[pos[0] + i][pos[1] + j]
                    if abs(i) != abs(j) and [pos[0]+i, pos[1]+j] not in visited and val != 100:
                        place = "[%s, %s]" % (pos[0]+i, pos[1]+j)
                        try:
                            if oldval + val < distances[place]:
                                newval = oldval + val
                                distances[place] = newval
                                undistances[place] = newval
                        except:
                            None
            unvisited.remove([pos[0], pos[1]])
            undistances.pop("[%s, %s]" % (pos[0], pos[1]))
            visited.append([pos[0], pos[1]])
            return


while len(unvisited) > 0:
    undistances = {k: v for k, v in sorted(undistances.items(), key=lambda item: item[1])}
    dists(undistances)

    if len(unvisited) % 1000 == 0:
        print(len(unvisited))

print(distances["[%s, %s]" % (len(grid)-2, len(grid)-2)])
print(time.time() - start)
