p = [(17, 5, 1), (-2, -8, 8), (7, -6, 14), (1, -10, 4)]
q = p.copy()

#p = [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]
c = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
coords = []

def newvel(p, c):
    ans = []
    coo = []
    i = 0
    for thing in p:
        x = 0
        y = 0
        z = 0
        for thing2 in p:
            if thing[0] > thing2[0]:
                x -= 1
            elif thing[0] != thing2[0]:
                x += 1

            if thing[1] > thing2[1]:
                y -= 1
            elif thing[1] != thing2[1]:
                y += 1

            if thing[2] > thing2[2]:
                z -= 1
            elif thing[2] != thing2[2]:
                z += 1
        coords.append((thing[0], thing[1], thing[2]))
        ans.append((thing[0]+x+c[i][0], thing[1]+y+c[i][1], thing[2]+z+c[i][2]))
        coo.append((x+c[i][0], y+c[i][1], z+c[i][2]))
        i += 1
    return ans, coo


for i in range(0, 1000):
    p, c = newvel(p, c)
    print(p)
    print(c)
    print("====")

print(p)
print(c)

print("thing")

m = []
for thing in p:
    t = 0
    for thing2 in thing:
        t += abs(thing2)
    m.append(t)

n = []
for thing in c:
    t = 0
    for thing2 in thing:
        t += abs(thing2)
    n.append(t)

a = 0
for i in range(0, len(m)):
    a += m[i]*n[i]

print(a)
