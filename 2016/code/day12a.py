from helpers.datagetter import aocd_data_in
from collections import defaultdict
import re

din, aocd_submit = aocd_data_in(split=True, numbers=False)

regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

i = 0
while i < len(din):
    line = din[i].split(" ")

    instr = line[0]
    x = line[1]
    y = 0 if len(line) < 3 else line[2]

    if instr == "cpy":
        if x in regs:
            regs[y] = regs[x]
        else:
            regs[y] = int(x)
    elif instr == "inc":
        regs[x] += 1
    elif instr == "dec":
        regs[x] -= 1
    elif instr == "jnz":
        val = 0
        if x in regs:
            val = regs[x]
        else:
           val = int(x)
        if val != 0:
            i += int(y)
            continue
    i += 1

aocd_submit(regs['a'])