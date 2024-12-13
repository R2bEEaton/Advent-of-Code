from helpers.datagetter import aocd_data_in
import sympy as sp

din, aocd_submit = aocd_data_in(split=True, numbers=True)

tokens = 0

for i in range(0, len(din), 4):
    buttonA = din[i]
    buttonB = din[i+1]
    goal = [n + 10000000000000 for n in din[i+2]]

    try:
        a, b = sp.symbols('a, b', real=False)
        ans = sp.nsolve((sp.Eq(a * buttonA[0] + b * buttonB[0], goal[0]),
                    sp.Eq(a * buttonA[1] + b * buttonB[1], goal[1])), (a, b), (-1, 1))
        if ans[0] % 1 == 0 and ans[1] % 1 == 0:
            tokens += ans[0] * 3 + ans[1]
    except ValueError:
        pass

aocd_submit(int(tokens))