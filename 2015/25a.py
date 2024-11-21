t = 0
with open("input25.txt") as f:
    line = f.read().strip()
    x = int(line.split("column ")[1].replace(".", ""))
    y = int(line.split("row ")[1].split(",")[0])

for i in range(1, x+1):
    t += i

for i in range(0, y-1):
    t += x+i

v = 20151125
for i in range(t-1):
    v *= 252533
    v %= 33554393

print(v)
