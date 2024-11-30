from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)
program = [int(x) for x in din]

idx = 0
steps = 0

while idx < len(program):
    temp = program[idx]
    if temp >= 3:
        program[idx] -= 1
    else:
        program[idx] += 1
    idx += temp
    steps += 1

aocd_submit(steps)