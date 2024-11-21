openers = ["<", "[", "(", "{"]
closers = [">", "]", ")", "}"]
score = {")": 3, "]": 57, "}": 1197, ">": 25137}
nscore = {")": 1, "]": 2, "}": 3, ">": 4}

all = ""
rest = ""
incomplete = []


def closesearch(line):
    orig = line
    old = "."
    while old != line:
        old = line
        line = line.replace("()", "")
        line = line.replace("[]", "")
        line = line.replace("{}", "")
        line = line.replace("<>", "")

    for i in range(len(line) - 1):
        if line[i] in openers and line[i + 1] in closers:
            return score[line[i + 1]]
    incomplete.append(orig)
    return 0


def auto(line):
    old = "."
    while old != line:
        old = line
        line = line.replace("()", "")
        line = line.replace("[]", "")
        line = line.replace("{}", "")
        line = line.replace("<>", "")

    line = list(line)
    line.reverse()
    news = ""
    for char in line:
        news += closers[openers.index(char)]
    t = 0
    for char in news:
        t *= 5
        t += nscore[char]
    return t


t = 0
with open("input10.txt") as f:
    for line in f.readlines():
        line = line.strip()
        t += closesearch(line)

t = []
for line in incomplete:
    t.append(auto(line))
t.sort()
print(t[len(t)//2])
