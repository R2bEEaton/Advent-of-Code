total = 0

with open("input2.txt") as f:
    for line in f.readlines():
        l = int(line.split("x")[0])
        w = int(line.split("x")[1])
        h = int(line.split("x")[2])
        total += min(2*l+2*w,2*w+2*h,2*h+2*l) + l*w*h

print(total)
