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
    found = False
    for char in path:
        if char.islower() and char in visited:
            found = True
        elif char.islower() and char not in ["start"]:
            visited.append(char)
    if found:
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
