n = 0

with open("input5.txt") as f:
    for line in f.readlines():
        line = line.strip()

        found1 = False
        found2 = False
        for i in range(0, len(line)):
            try:
                find = line[i] + line[i+1]
                if find in line[0:i] + " " + line[i+2:len(line)]:
                    found1 = True
            except:
                None

            try:
                if line[i] == line[i+2]:
                    found2 = True
            except:
                None

        if found1 and found2:
            n += 1

print(n)
