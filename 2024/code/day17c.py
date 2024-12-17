from helpers.datagetter import aocd_data_in
import pygad

din, aocd_submit = aocd_data_in(split=True, numbers=True)
program = din[4]


def to_bin(l):
    o = 0
    for i in range(len(l)):
        o |= l[len(l) - 1 - i] << i
    return o


def checkA(A_val):
    regs = {"A": A_val, "B": din[1][0], "C": din[2][0]}
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
    return output

initial_population = []

for j in range(16):
    for i in range(8):
        a = '111' * (j) + bin(i)[2:].zfill(3) + '111' * (15-j)
        print(len(a))
        initial_population.append([int(x) for x in a])


def fitness_func(ga_instance, solution, solution_idx):
    init = to_bin(solution)
    if not (35184372088832 < init < 108951210856193):
        return 0
    out = checkA(init)
    fitness = (sum([out[i] == program[i] for i in range(min(len(out), len(program)))])) / len(program)
    return fitness


def on_gen(ga_instance):
    print("Generation : ", ga_instance.generations_completed, "Fitness of the best solution :", ga_instance.best_solution()[1])


while True:
    ga_instance = pygad.GA(num_generations=10000,
                        num_parents_mating=16,
                        fitness_func=fitness_func,
                        initial_population=initial_population,
                        gene_type=int,
                        gene_space=[0, 1],
                        on_generation=on_gen,
                        stop_criteria="reach_1",
                        crossover_type="uniform"
                    )

    ga_instance.run()
    A_val = ga_instance.best_solution()[0]
    A_val = to_bin(A_val)
    if (checkA(A_val) == program):
        aocd_submit(A_val)

# ga_instance.plot_fitness()