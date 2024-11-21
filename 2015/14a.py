import math

reindeer = {}

with open("input14.txt") as f:
    for line in f.readlines():
        line = line.split()
        reindeer[line[0]] = list(map(int, [line[3], line[6], line[-2]]))

t = 2503
u = []
for r in reindeer:
    rem = t % (reindeer[r][1]+reindeer[r][2])
    if rem > reindeer[r][1]:
        rem = reindeer[r][1]
    u.append((math.floor(t/(reindeer[r][1]+reindeer[r][2]))*reindeer[r][0]*reindeer[r][1])+(rem*reindeer[r][0]))

print(max(u))
