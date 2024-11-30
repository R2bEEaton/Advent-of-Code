from helpers.datagetter import aocd_data_in
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=True, numbers=False)

regs = defaultdict(int)

def cmp(inp):
    inp.insert(1, "regs['")
    inp.insert(3, "']")
    inp = " ".join(inp)
    inp = inp.replace("' ", "'")
    inp = inp.replace(" '", "'")
    return eval(f"True {inp} else False")

for line in din:
    line = line.split()
    regs[line[0]] += (int(line[2]) * (-1 if line[1] == "dec" else 1)) if cmp(line[3:]) else 0

aocd_submit(max(list(regs.values())))