from helpers.datagetter import aocd_data_in
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=True, numbers=True)
ans = 0

after = defaultdict(list)
before = defaultdict(list)
in_rules = True


def valid(line):
    for i, x in enumerate(line):
        print(i, x)
        for y in line[i+1:]:
            if y in before[x]:
                return False
        for y in line[:i]:
            if y in after[x]:
                return False
    return True


for line in din:
    if len(line) == 0:
        in_rules = False
        continue
    
    if in_rules:
        after[line[0]].append(line[1])
        before[line[1]].append(line[0])
        continue
    
    if valid(line):
        ans += line[len(line) // 2]

aocd_submit(ans)