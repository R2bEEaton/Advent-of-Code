all = []
pos_dis = {}

with open("input7.txt") as f:
    for el in f.read().split(","):
        all.append(int(el))

t = 100000000000000000000


def step(num):
    try:
        return pos_dis[num]
    except:
        o = 0
        for i in range(num+1):
            o += i
        pos_dis[num] = o
        return o


for thing in range(min(all), max(all)):
    t2 = 0
    for crab in all:
        t2 += step(abs(crab - thing))
    if t2 < t:
        t = t2

print(t)
