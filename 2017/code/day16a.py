from helpers.datagetter import aocd_data_in
from collections import deque

din, aocd_submit = aocd_data_in(split=False, numbers=False)

programs = deque([chr(ord('a') + i) for i in range(16)])

for instr in din.split(","):
    if instr[0] == "s":
        programs.rotate(int(instr[1:]))
    elif instr[0] == "x":
        params = [int(x) for x in instr[1:].split("/")]
        temp = programs[params[0]]
        programs[params[0]] = programs[params[1]]
        programs[params[1]] = temp
    elif instr[0] == "p":
        params = [programs.index(x) for x in instr[1:].split("/")]
        temp = programs[params[0]]
        programs[params[0]] = programs[params[1]]
        programs[params[1]] = temp

aocd_submit("".join(programs))