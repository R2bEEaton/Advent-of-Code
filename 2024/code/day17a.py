from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

regs = {"A": din[0][0], "B": din[1][0], "C": din[2][0]}

IP = 0

program = din[4]
output = []

while IP < len(program):
    opcode = program[IP]
    operand_lit = program[IP+1]
    operand_combo = operand_lit if operand_lit < 4 else regs[chr(ord("A") + operand_lit - 4)]

    if opcode == 0:
        regs["A"] = regs["A"] // (2 ** operand_combo)
    elif opcode == 1:
        regs["B"] ^= operand_lit
    elif opcode == 2:
        regs["B"] = operand_combo % 8
    elif opcode == 3:
        if regs["A"]:
            IP = operand_lit
            IP -= 2
    elif opcode == 4:
        regs["B"] ^= regs["C"]
    elif opcode == 5:
        output.append(operand_combo % 8)
    elif opcode == 6:
        regs["B"] = regs["A"] // (2 ** operand_combo)
    elif opcode == 7:
        regs["C"] = regs["A"] // (2 ** operand_combo)

    IP += 2


aocd_submit(",".join([str(x) for x in output]))