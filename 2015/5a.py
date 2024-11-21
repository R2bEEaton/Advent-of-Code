n = 0

with open("input5.txt") as f:
    for line in f.readlines():
        nice = True
        if line.count("a") + line.count("e") + line.count("i") + line.count("o") + line.count("u") < 3:
            nice = False

        found = False
        for i in range(0, 26):
            if (chr(97 + i) + chr(97 + i)) in line:
                found = True
                break
        if not found:
            nice = False

        for x in ['ab', 'cd', 'pq', 'xy']:
            if x in line:
                nice = False
                break

        if nice:
            n += 1

print(n)
