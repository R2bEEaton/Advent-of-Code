ingr = []

with open("input15.txt") as f:
    for line in f.readlines():
        line = [s.replace(",","").replace(":","") for s in line.split()]
        ingr.append(list(map(int, [line[(x+1)*2] for x in range(5)])))

tps = []
for i in range(1, 100):
    for j in range(1, 100-i+1):
        for k in range(1, 100-j-1):
            for l in range(1, 100-k-1):
                t = [i, j, k, l]
                if sum(t) == 100:
                    tps.append(t)

c = 0
for i in range(len(tps)):
    ans = [0]*(len(ingr[0])-1)
    for j in range(len(tps[i])):
        for l in range(len(ingr[j])-1):
            ans[l] += tps[i][j]*ingr[j][l]
    a = 1
    for thing in ans:
        if thing <= 0:
            a = 0
        a *= thing
    if a > c:
        c = a

print(c)
