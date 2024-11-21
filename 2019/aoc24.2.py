inp = """input redacted"""

inp = inp.split("\n")

world = {}

new_thing = []
for thing in inp:
    new = []
    for thing2 in thing:
        new.append(thing2)
    new_thing.append(new)
world[0] = new_thing

def check_around(l, ly, x, y):
    ans = 0
    try:
        if l[ly][x+1][y] == "#":
            ans += 1

    except:
        None

    try:
        if l[ly][x][y-1] == "#" and not y-1 < 0:
            ans += 1

    except:
        None

    try:
        if l[ly][x-1][y] == "#" and not x-1 < 0:
            ans += 1

    except:
        None

    try:
        if l[ly][x][y+1] == "#":
            ans += 1

    except:
        None

    return ans

def run(l):
    layer = []
    new = []
    for i in sorted(l):
        layer.append(i)
        print(i)

    print("reee")

    for ly in layer:
        new_world = []

        for x in range(len(l[ly])):
            new = []
            for y in range(len(l[ly])):
                if l[ly][x][y] == "#":
                    if check_around(l, ly, x, y) != 1:
                        new.append(".")
                    else:
                        new.append("#")
                else:
                    if check_around(l, ly, x, y) == 1 or check_around(l, ly, x, y) == 2:
                        new.append("#")
                    else:
                        new.append(".")
            new_world.append(new)
        new[ly] = new_world

    return new

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