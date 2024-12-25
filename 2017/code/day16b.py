from helpers.datagetter import aocd_data_in
from collections import deque

din, aocd_submit = aocd_data_in(split=False, numbers=False)

programs = tuple([chr(ord('a') + i) for i in range(16)])


def do_dance(programs):
    programs = deque(programs)
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
    return tuple(programs)


seen = set()
cycle = []
cycle_start = 0
for i in range(1000000000):
    programs = do_dance(programs)
    if programs in seen:
        cycle_start = cycle.index("".join(programs))
        break
    seen.add(programs)
    cycle.append("".join(programs))

aocd_submit(cycle[1000000000 % (len(cycle) - cycle_start) - 1])