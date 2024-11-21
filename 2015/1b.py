fl = 0

with open("input1.txt") as f:
    for line in f.readlines():
        for i in range(0, len(line)):
            if line[i] == ")":
                fl -= 1
            else:
                fl += 1
            if fl == -1:
                print(i+1)
                break

print(fl)