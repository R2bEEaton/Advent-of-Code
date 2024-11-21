good = 0

with open("2.txt") as f:
    for line in f.readlines():
        min = int(line.split("-")[0])
        max = int(line.split("-")[1].split(" ")[0])

        letter = line.split(" ")[1].split(":")[0]
        password = line.split(": ")[1]

        if password[min-1] == letter or password[max-1] == letter:
            if password[min-1] != password[max-1]:
                good += 1
                print(line)

print(good)