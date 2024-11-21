c = 0
with open('input8.txt') as f:
    for line in f.readlines():
        line = line.strip()
        c += len(line) - len(eval(line))

print(c)
