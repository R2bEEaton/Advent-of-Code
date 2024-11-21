ones = [0]*12
zeroes = [0]*12

with open("input3.txt") as f:
    for line in f:
        for i in range(0, len(line)):
            if line[i] == "1":
                ones[i] += 1

            if line[i] == "0":
                zeroes[i] += 1

g = ""
e = ""
for i in range(0, 12):
    if ones[i] > zeroes[i]:
        g += "1"
        e += "0"
    else:
        g += "0"
        e += "1"

print(int(g, 2) * int(e, 2))
