with open("input21.txt") as f:
    lines = f.readlines()
    p = int(lines[0].split(" ")[-1].strip())
    e = int(lines[1].split(" ")[-1].strip())

ps = 0
es = 0
die = 1
turn = -1
rolls = 0


def roll(die):
    global rolls
    rolls += 1
    t = 0
    for i in range(3):
        t += die+i
    return t, ((die + 2) % 100) + 1


while ps < 1000 and es < 1000:
    t, die = roll(die)
    if turn == -1:
        p += t
        p = ((p - 1) % 10) + 1
        ps += p
    else:
        e += t
        e = ((e - 1) % 10) + 1
        es += e
    turn *= -1

print(min(ps, es) * rolls * 3)
