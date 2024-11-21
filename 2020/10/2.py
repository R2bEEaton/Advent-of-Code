data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(int(line.strip()))

data = sorted(data)
data.append(data[-1]+3)

print(data)


paths = {}

for path in data:
    paths[path] = []
    for i in range(1, 4):
        if path-i in data:
            paths[path].append(path-i)

print(paths)


rev = []

for thing in paths.values():
    rev = [thing] + rev

found = []

out = 1
for thing in rev:
    running = 0
    for item in thing:
        if item not in found:
            running += 1
            found.append(item)
    out *= running

print(found)
print(out)
