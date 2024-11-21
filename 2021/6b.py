days = [0]*9

with open("input6.txt") as f:
    for line in f.readlines():
        for thing in line.split(","):
            days[int(thing)] += 1

for day in range(256):
    new_days = [0]*9
    for i in range(9):
        if i == 0:
            new_days[8] = days[i]
        elif i == 7:
            new_days[6] = days[0] + days[7]
        else:
            new_days[i-1] = days[i]
    days = new_days


c = 0
for thing in days:
    c += thing
print(c)