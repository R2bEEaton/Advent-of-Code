from helpers.datagetter import aocd_data_in
from itertools import product
import math

din, aocd_submit = aocd_data_in(split=True, numbers=True)
ans = 0


def evaluate(eq):
    if eq[1] == "||":
        return [eq[0] * 10 ** math.ceil(math.log(eq[2], 10)) + eq[2]]
    elif eq[1] == "+":
        return [eq[0] + eq[2]]
    elif eq[1] == "*":
        return [eq[0] * eq[2]]

bad = []
ops = ["+", "*"]

for line in din:
    eq = line[1:]
    for perm in product(ops, repeat=len(eq) - 1):
        equation = []
        for i in range(len(eq) - 1):
            equation.append(eq[i])
            if len(equation) == 3:
                equation = evaluate(equation)
            equation.append(perm[i])
        equation.append(eq[-1])
        if evaluate(equation)[0] == line[0]:
            ans += line[0]
            break
    else:
        bad.append(line)

print("test")

ops = ["+", "*", "||"]

for n, line in enumerate(bad):
    eq = line[1:]
    for perm in product(ops, repeat=len(eq) - 1):
        equation = []
        for i in range(len(eq) - 1):
            equation.append(eq[i])
            if len(equation) == 3:
                equation = evaluate(equation)
            equation.append(perm[i])
        equation.append(eq[-1])
        if evaluate(equation)[0] == line[0]:
            ans += line[0]
            break
    print(n)

aocd_submit(ans)