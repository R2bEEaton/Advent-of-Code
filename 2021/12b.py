dict = {}

with open("input12.txt") as f:
    for line in f.readlines():
        line = line.strip().split("-")
        try:
            dict[line[1]].append(line[0])
        except:
            dict[line[1]] = [line[0]]
        try:
            dict[line[0]].append(line[1])
        except:
            dict[line[0]] = [line[1]]

print(dict)
winners = []

def isbad(path):
    visited = []
    found = {}
    ends = 0
    for char in path:
        if char.islower() and char not in ["start", "end"]:
            try:
                found[char] += 1
            except:
                found[char] = 1
        if char == "end":
            ends += 1
    if ends > 1:
        return True
    f = False
    for key in found:
        if found[key] == 2 and f:
            return True
        elif found[key] == 2 and not f:
            f = True
        elif found[key] > 2:
            return True

    return False


def findstart(path):
    global winners
    if path[-1] == "start":
        winners.append(path)
        return
    if isbad(path):
        return
    for next in dict[path[-1]]:
        findstart(path + [next])


findstart(["end"])
print(len(winners))
