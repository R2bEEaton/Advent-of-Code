most = []
least = []

with open("input3.txt") as f:
    for line in f.readlines():
        most.append(line.strip())
        least.append(line.strip())

index = 0
while len(most) > 1:
    ones = 0
    zeroes = 0

    for i in range(0, len(most)):
        if most[i][index] == "1":
            ones += 1
        else:
            zeroes += 1

    if ones >= zeroes:
        search = "1"
    else:
        search = "0"

    done = False
    while not done:
        found = False
        for j in range(0, len(most)):
            if most[j][index] != search:
                most.pop(j)
                found = True
                break
        if not found:
            done = True

    index += 1


index = 0
while len(least) > 1:
    ones = 0
    zeroes = 0

    for i in range(0, len(least)):
        if least[i][index] == "1":
            ones += 1
        else:
            zeroes += 1

    if ones < zeroes:
        search = "1"
    else:
        search = "0"

    done = False
    while not done:
        found = False
        for j in range(0, len(least)):
            if least[j][index] != search:
                least.pop(j)
                found = True
                break
        if not found:
            done = True

    index += 1
    
print(int(most[0], 2) * int(least[0], 2))
