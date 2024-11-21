inc = -1
old = 0

try:
    with open("input1.txt") as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            new = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
            if new > old:
                inc += 1
            old = new
except:
    None

print(inc)
