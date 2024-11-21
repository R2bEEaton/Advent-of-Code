data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())

print(data)
