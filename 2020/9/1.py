data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())

pl = 25

for i in range(pl, len(data)):
    subs = []
    for j in range(i-pl, i):
        subs.append(int(data[j]))

    good = False
    for num in subs:
        if int(data[i])-num in subs and int(data[i])-num != num:
            good = True
            break

    if not good:
        print(data[i])
        break
