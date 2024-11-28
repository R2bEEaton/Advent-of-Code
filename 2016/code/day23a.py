from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)

regs = {'a': 7, 'b': 0, 'c': 0, 'd': 0}

program = []

for line in din:
    line = line.split(" ")

    instr = line[0]
    x = line[1]
    y = None if len(line) < 3 else line[2]

    program.append([instr, x, y])

i = 0
while i < len(program):
    instr, x, y = program[i]

    try:
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

            if y in regs:
                valy = regs[y]
            else:
                valy = int(y)

            if val != 0:
                i += valy
                continue
        elif instr == "tgl":
            if x in regs:
                val = regs[x]
            else:
                val = int(x)
            if i + val < len(program):
                toggle = program[i + val]
                if toggle[2] is None:
                    toggle[0] = "dec" if toggle[0] == "inc" else "inc"
                else:
                    toggle[0] = "cpy" if toggle[0] == "jnz" else "jnz"
    except:
        None

    i += 1

aocd_submit(regs['a'])