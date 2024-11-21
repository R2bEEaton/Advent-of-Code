import operator
scanners = []

with open("input19.txt") as f:
    temp = []
    for line in f.readlines():
        line = line.strip()
        if "," in line:
            temp.append(list(map(int, line.split(","))))
        elif line == "":
            scanners.append(temp)
            temp = []
    scanners.append(temp)


def roll(v): return (v[0],v[2],-v[1])
def turn(v): return (-v[1],v[0],v[2])
def sequence (v):
    for cycle in range(2):
        for step in range(3):
            v = roll(v)
            yield v
            for i in range(3):
                v = turn(v)
                yield v
        v = roll(turn(roll(v)))


def orientations(line):
    o = []
    for first in line:
        temp = [first]
        #temp = []
        for second in line:
            temp.append(list(map(operator.sub, second, first)))
        o.append(temp)
    return o


def sim(first, second):
    t = 0
    for i in first:
        for j in second:
            if i == j:
                t += 1
    if t >= 12:
        return True
    return False


answers = []
for i in range(len(scanners)):
    p = []
    temp = []
    for j in range(len(scanners[i])):
        p.append(sequence((scanners[i][j])))
    o = []
    for j in range(len(scanners[i])):
        o.append("p[%s]" % j)
    for j in sorted(eval("zip(" + ", ".join(o) + ")")):
        for k in orientations(j):
            temp.append(k)
    answers.append(temp)


def common(i, j):
    global answers
    for first in answers[i]:
        for second in answers[j]:
            if sim(first, second):
                o = []
                for thing in set(str(first[1:]).replace("[[", "").replace("]]", "").split("], [") + str(second[1:]).replace("[[", "").replace("]]", "").split("], [")):
                    o.append(eval("[" + thing + "]"))
                print(first[0])
                return o
    return False


def path(i):
    o = []
    o.append(i)
    while path_to_zero[i] != 0:
        i = path_to_zero[i]
        o.append(i)
    o.append(0)
    return o


pairs = [[0, 24], [1, 6], [1, 10], [1, 19], [1, 23], [2, 15], [2, 18], [2, 21], [3, 12], [3, 13], [4, 21], [5, 16],
         [6, 11], [7, 11], [7, 20], [8, 12], [9, 12], [9, 22], [10, 17], [11, 21], [11, 23], [12, 14], [12, 15],
         [13, 15], [13, 18], [14, 17], [14, 22], [15, 17], [16, 24], [17, 21], [17, 23], [18, 24]]
path_to_zero = [0, 23, 18, 13, 21, 16, 11, 11, 12, 12, 17, 21, 3, 18, 12, 2, 24, 21, 24, 1, 7, 2, 11, 17, 0]

""""
for i in range(len(answers)):
    for j in range(len(answers)):
        if [i, j] in pairs:
            c = common(i, j)
            if c:
                print(c)
"""

for i in range(25):
    p = path(i)
    print(p)
    """
    for j in range(len(p)-1):
        print(p[j], p[j+1])
    print()
    """
