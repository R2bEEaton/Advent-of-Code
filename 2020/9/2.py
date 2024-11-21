data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())

pl = 25
sum = 0

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
        sum = int(data[i])
        break

print(sum)
out = 0

for i in range(0, len(data)):
    total = 0
    adds = []
    for j in range(i, len(data)):
        adds.append(int(data[j]))
        total += int(data[j])
        if total == sum:
            out += sorted(adds)[0]
            out += sorted(adds)[-1]
            print(out)
            exit()
