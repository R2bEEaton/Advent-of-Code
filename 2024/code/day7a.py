from helpers.datagetter import aocd_data_in
from itertools import product

din, aocd_submit = aocd_data_in(split=True, numbers=True)
ans = 0

ops = ["+", "*"]

for line in din:
    eq = line[1:]
    for perm in product(ops, repeat=len(eq) - 1):
        equation = []
        for i in range(len(eq) - 1):
            equation.append(str(eq[i]))
            if len(equation) == 3:
                equation = [eval("".join([str(x) for x in equation]))]
            equation.append(perm[i])
        equation.append(str(eq[-1]))
        if eval("".join([str(x) for x in equation])) == line[0]:
            ans += line[0]
            break

aocd_submit(ans)