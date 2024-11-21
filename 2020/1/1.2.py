data = []

with open("1.txt") as f:
    for thing in f.readlines():
        data.append(thing.strip())

for first in data:
    for second in data:
        for third in data:
            if int(first)+int(second)+int(third) == 2020:
                print(int(first)*int(second)*int(third))
                exit()
