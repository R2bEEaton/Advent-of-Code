x = 0
y = 0
c = {"(%s,%s)" % (x, y): 1}

with open("input3.txt") as f:
    for line in f.readlines():
        for i in range(0, len(line)):
            l = line[i]
            if l == "^":
                y += 1
            elif l == "v":
                y -= 1
            elif l == ">":
                x += 1
            else:
                x -= 1

            try:
                c["(%s,%s)" % (x, y)] += 1
            except:
                c["(%s,%s)" % (x, y)] = 1

print(len(c))
