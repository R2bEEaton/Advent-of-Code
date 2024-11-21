data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(int(line.strip()))

data = sorted(data)
data.append(data[-1]+3)

total = 0
diffs = [0, 0, 0, 0]

for jolt in data:
    diffs[jolt-total] += 1
    total = jolt

print(diffs[1]*diffs[3])
