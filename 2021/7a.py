all = []

with open("input7.txt") as f:
    for el in f.read().split(","):
        all.append(int(el))

t = 100000000000000000000

for thing in range(min(all), max(all)):
    t2 = 0
    for crab in all:
        t2 += abs(crab - thing)
    if t2 < t:
        t = t2

print(t)
