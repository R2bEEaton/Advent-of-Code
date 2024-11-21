data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())

pointer = 0
accumulator = 0

p_before = []


while True:
    instr = data[pointer].split(" ")[0]
    value = int(data[pointer].split(" ")[1])

    p_before.append(pointer)

    if instr == "acc":
        accumulator += value
        pointer += 1
    elif instr == "jmp":
        pointer += value
    elif instr == "nop":
        pointer += 1

    if pointer in p_before:
        print(accumulator)
        break
