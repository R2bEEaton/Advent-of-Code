inc = -1
old = 0

with open("input1.txt") as f:
    for line in f.readlines():
        if int(line) > old:
            inc += 1
        old = int(line)

print(inc)
