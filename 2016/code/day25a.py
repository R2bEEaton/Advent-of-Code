from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)


def try_it(n, t):
    regs = {'a': n, 'b': 0, 'c': 0, 'd': 0}

    program = []

    for line in din:
        line = line.split(" ")

        instr = line[0]
        x = line[1]
        y = None if len(line) < 3 else line[2]

        program.append([instr, x, y])


    last_val = 1
    i = 0
    steps = 0
    while i < len(program) and steps < t:
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
            elif instr == "out":
                if x in regs:
                    val = regs[x]
                else:
                    val = int(x)
                if last_val == val or (last_val == 1 and val != 0) or (last_val == 0 and val != 1):
                    return False
                last_val = val
        except:
            None

        i += 1
        steps += 1

    return True

for i in range(1, 100_000):
    out = try_it(i, 1_000_000)
    if out:
        break

aocd_submit(i)