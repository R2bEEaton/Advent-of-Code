openers = ["<", "[", "(", "{"]
closers = [">", "]", ")", "}"]
score = {")": 3, "]": 57, "}": 1197, ">": 25137}


all = ""
rest = ""

def closesearch(line):
    old = "."
    while old != line:
        old = line
        line = line.replace("()", "")
        line = line.replace("[]", "")
        line = line.replace("{}", "")
        line = line.replace("<>", "")

    for i in range(len(line)-1):
        if line[i] in openers and line[i+1] in closers:
            return score[line[i+1]]
    return 0


t = 0
with open("input10.txt") as f:
    for line in f.readlines():
        line = line.strip()
        t += closesearch(line)
print(t)
