import math

reindeer = {}

with open("input14.txt") as f:
    for line in f.readlines():
        line = line.split()
        reindeer[line[0]] = list(map(int, [line[3], line[6], line[-2], 0, 0]))

for t in range(1, 2503+2):
    m = 0
    for r in reindeer:
        rem = t % (reindeer[r][1]+reindeer[r][2])
        if rem > reindeer[r][1]:
            rem = reindeer[r][1]
        reindeer[r][3] = (math.floor(t/(reindeer[r][1]+reindeer[r][2]))*reindeer[r][0]*reindeer[r][1])+(rem*reindeer[r][0])
        if reindeer[r][3] > m:
            m = reindeer[r][3]
    for r in reindeer:
        if reindeer[r][3] == m:
            reindeer[r][4] += 1

c = 0
for r in reindeer:
    if reindeer[r][4] > c:
        c = reindeer[r][4]
print(c)
