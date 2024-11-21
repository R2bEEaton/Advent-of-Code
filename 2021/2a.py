h = 0
d = 0

with open("input2.txt") as f:
    for line in f:
        if line.startswith("down "):
            d += int(line.split(" ")[1])
        elif line.startswith("up "):
            d -= int(line.split(" ")[1])
        else:
            h += int(line.split(" ")[1])

print(h*d)
