biggest = 0

with open("5.txt") as f:
    for line in f.readlines():
        row = line[:7].replace("F", "0").replace("B", "1")
        column = line[7:].replace("L", "0").replace("R", "1")
        answer = int(row, 2) * 8 + int(column, 2)

        if answer > biggest:
            biggest = answer

print(biggest)
