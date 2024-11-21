import re


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
    count = 0
    for criteria in checks:
        if "%s:" % criteria in thing:
            count += 1
    if count == 7:
        count = 0
        for field in thing.split(" "):
            if field != "":
                criterion = field.split(":")[0]
                value = field.split(":")[1]
                if criterion == "byr" and 1920 <= int(value) <= 2002:
                    count += 1
                if criterion == "iyr" and 2010 <= int(value) <= 2020:
                    count += 1
                if criterion == "eyr" and 2020 <= int(value) <= 2030:
                    count += 1
                if criterion == "hgt":
                    if value.endswith("in") and 59 <= int(value.split("in")[0]) <= 76:
                        count += 1
                    elif value.endswith("cm") and 150 <= int(value.split("cm")[0]) <= 193:
                        count += 1
                if criterion == "hcl" and value.startswith("#") and re.search(r'^#(?:[A-F0-9]{6})', value.upper()):
                    count += 1
                if criterion == "ecl" and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    count += 1
                if criterion == "pid" and value.isnumeric() and len(value) == 9:
                    count += 1

        if count == 7:
            good += 1

print(good)
