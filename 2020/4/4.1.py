data = []

with open("4.txt") as f:
    running = ""
    for thing in f.readlines():
        if thing != "\n":
            running += thing.replace("\n", " ")
        else:
            data.append(running)
            running = ""
    data.append(running)

checks = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
good = 0

for thing in data:
    print(thing, "\n")
    count = 0
    for criteria in checks:
        if "%s:" % criteria in thing:
            count += 1
    if count == 7:
        good += 1

print(good)
