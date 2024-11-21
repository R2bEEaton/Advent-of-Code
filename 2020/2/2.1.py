good = 0

with open("2.txt") as f:
    for line in f.readlines():
        min = int(line.split("-")[0])
        max = int(line.split("-")[1].split(" ")[0])

        letter = line.split(" ")[1].split(":")[0]
        password = line.split(": ")[1]

        if min <= password.count(letter) <= max:
            good += 1

print(good)