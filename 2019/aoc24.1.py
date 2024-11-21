inp = """input redacted"""

inp = inp.split("\n")

world = []

for thing in inp:
    new = []
    for thing2 in thing:
        new.append(thing2)
    world.append(new)

def check_around(l, x, y):
    ans = 0
    try:
        if l[x+1][y] == "#":
            ans += 1

    except:
        None

    try:
        if l[x][y-1] == "#" and not y-1 < 0:
            ans += 1

    except:
        None

    try:
        if l[x-1][y] == "#" and not x-1 < 0:
            ans += 1

    except:
        None

    try:
        if l[x][y+1] == "#":
            ans += 1

    except:
        None

    return ans

for thing in world:
    print(thing)

def run(l):
    new_world = []
    for x in range(len(l)):
        new = []
        for y in range(len(l[x])):
            if l[x][y] == "#":
                if check_around(l, x, y) != 1:
                    new.append(".")
                else:
                    new.append("#")
            else:
                if check_around(l, x, y) == 1 or check_around(l, x, y) == 2:
                    new.append("#")
                else:
                    new.append(".")
        new_world.append(new)

    return new_world

print()

old_states = []

while True:
    world = run(world)
    for thing in world:
        print(thing)
    print()
    if world in old_states:
        print("WOOO")
        ans = 0
        x = 0
        for thing in world:
            for thing2 in thing:
                if thing2 == "#":
                    ans += 2 ** x
                x += 1
        print(ans)
        break
    old_states.append(world)