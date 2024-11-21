total = 0

with open("input2.txt") as f:
    for line in f.readlines():
        l = int(line.split("x")[0])
        w = int(line.split("x")[1])
        h = int(line.split("x")[2])
        total += 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)

print(total)
