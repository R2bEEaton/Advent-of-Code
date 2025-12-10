from helpers.datagetter import aocd_data_in
import tqdm
import numpy as np
from scipy.optimize import linprog

din, aocd_submit = aocd_data_in(split=True, numbers=False)

ans = 0


def getFewestSolver(goal, buttons):
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

    arrs = []
    for button in buttons:
        arr = [0] * len(goal)
        for b in button:
            arr[b] = 1
        arrs.append(arr)

    C = np.array(arrs)
    c = np.ones(C.shape[0])

    A_eq = C.T
    b_eq = np.array(goal)

    result = linprog(c, A_eq=A_eq, b_eq=b_eq, integrality=np.ones(C.shape[0]))

    return result.fun


for line in tqdm.tqdm(din):
    goal, buttons = tuple([int(x) for x in line.split(" ")[-1][1:-1].split(",")]), [[int(y) for y in x[1:-1].split(",")] for x in line.split(" ")[1:-1]]
    # print(goal, buttons)
    ans += getFewestSolver(goal, buttons)

aocd_submit(ans)