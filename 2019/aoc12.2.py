import math

p = [(17, 5, 1), (-2, -8, 8), (7, -6, 14), (1, -10, 4)]

p = [(4, 12, 13), (-9, 14, -3), (-7, -1, 2), (-11, 17, -1)]
q = p.copy()
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


def find_lcm(p, c, k):
    i = 0
    while True:
        p, c = newvel(p, c)
        w = 0
        for j in range(4):
            if p[j][k] != q[j][k]:
                w = 1
        if w == 0:
            return i+2
        i += 1

def lcm(a, b):
    return int(a * b / math.gcd(a, b))


print(lcm(lcm(find_lcm(p, c, 0), find_lcm(p, c, 1)), find_lcm(p, c, 2)))
