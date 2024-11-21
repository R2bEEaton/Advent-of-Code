lanternfish = []

with open("input6.txt") as f:
    for line in f.readlines():
        for thing in line.split(","):
            lanternfish.append(int(thing))

for i in range(80):
    for j in range(len(lanternfish)):
        lanternfish[j] -= 1
        if lanternfish[j] < 0:
            lanternfish[j] = 6
            lanternfish.append(8)

print(len(lanternfish))
