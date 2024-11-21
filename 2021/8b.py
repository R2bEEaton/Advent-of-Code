# Get inputs
with open("input8.txt") as f:
    inps = list(map(str, f.readlines()))

# A list of all numbers and their seven segment counterparts
num_list = [[1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1]]
# Total for the answer
total = 0
# I give up on comments, good luck
lnum = 0

for line in inps:
    lnum += 1
    deduc = {}
    unknown = []
    for thing in line.split():
        thing = "".join(sorted(thing))
        if len(thing) == 2:
            deduc[1] = thing
        elif len(thing) == 3:
            deduc[7] = thing
        elif len(thing) == 4:
            deduc[4] = thing
        elif len(thing) == 7:
            deduc[8] = thing
        else:
            unknown.append(thing)

    segs = [0]*7

    for i in range(len(deduc[7])):
        if deduc[7][i] not in deduc[1]:
            segs[0] = deduc[7][i]
    sz = []
    nine = ""
    ttf = []
    for u in unknown:
        u = "".join(sorted(u))
        if len(u) == 6:
            found = False
            for char in deduc[4]:
                if char not in u:
                    found = True
                    if u not in sz:
                        sz.append(u)
            if not found:
                nine = u
        if len(u) == 5 and u not in ttf:
            ttf.append(u)

    three = ""
    for num in ttf:
        for num2 in ttf:
            if num != num2:
                t = 0
                for char in num:
                    if char not in num2:
                        t += 1
                if t == 1:
                    three = num2
                    ttf.remove(num2)

    for char in nine:
        if char not in three:
            segs[1] = char

    for char in nine:
        if char not in deduc[4]+str(segs[0]):
            segs[6] = char

    for thing in sz:
        for char in deduc[1]:
            if char not in thing:
                segs[2] = char
                segs[5] = deduc[1].replace(char, "")

    for char in nine:
        if char not in deduc[7]+str(segs[1])+str(segs[6]):
            segs[3] = char

    for char in deduc[8]:
        if char not in segs:
            segs[4] = char

    final = ""
    for num in line.split(" | ")[1].split():
        temp = [0] * 7
        for char in num:
            temp[segs.index(char)] = 1
        final += str(num_list.index(temp))
    if "1" not in final and "4" not in final and "7" not in final and "8" not in final:
        print(lnum, int(final))
    total += int(final)

print(total)
