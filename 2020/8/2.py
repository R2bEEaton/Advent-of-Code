data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())


def game(code):
    pointer = 0
    accumulator = 0

    p_before = []

    while True:
        instr = code[pointer].split(" ")[0]
        value = int(code[pointer].split(" ")[1])

        p_before.append(pointer)

        if instr == "acc":
            accumulator += value
            pointer += 1
        elif instr == "jmp":
            pointer += value
        elif instr == "nop":
            pointer += 1

        if pointer == len(code):
            print("GOOD", accumulator)
            break

        if pointer in p_before:
            break


for i in range(0, len(data)):
    instr = data[i].split(" ")[0]
    if instr == "nop":
        data[i] = data[i].replace("nop", "jmp")
        game(data)
        data[i] = data[i].replace("jmp", "nop")
    if instr == "jmp":
        data[i] = data[i].replace("jmp", "nop")
        game(data)
        data[i] = data[i].replace("nop", "jmp")
