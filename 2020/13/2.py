data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())

buses = {}

ans = 1
c = 0
for id in data[1].split(","):
    if id != "x":
        buses[c] = int(id)
        ans *= int(id)
    c += 1

print(buses)
print(ans)
