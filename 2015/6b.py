l = []
for i in range(1000):
    buffer = []
    for j in range(1000):
        buffer.append(0)
    l.append(buffer)

c = 0

with open("input6.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith("turn on") or line.startswith("turn off"):
            x1 = int(line.split(" ")[2].split(",")[0])
            y1 = int(line.split(" ")[2].split(",")[1])
            x2 = int(line.split(" ")[4].split(",")[0])
            y2 = int(line.split(" ")[4].split(",")[1])
        elif line.startswith("toggle"):
            x1 = int(line.split(" ")[1].split(",")[0])
            y1 = int(line.split(" ")[1].split(",")[1])
            x2 = int(line.split(" ")[3].split(",")[0])
            y2 = int(line.split(" ")[3].split(",")[1])

        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if "turn on" in line:
                    l[x][y] += 1
                elif "turn off" in line:
                    l[x][y] -= 1
                    if l[x][y] < 0:
                        l[x][y] = 0
                elif "toggle" in line:
                    l[x][y] += 2

for x in range(len(l)):
    for y in range(len(l)):
        c += l[x][y]

print(c)
