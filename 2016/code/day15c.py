from helpers.datagetter import aocd_data_in
from sympy.ntheory.modular import crt

din, aocd_submit = aocd_data_in(split=True, numbers=True)

mr = [[], []]

for i, line in enumerate(din + [[None, 11, None, 0]]):
    mr[0].append(line[1])
    mr[1].append(line[1] - (line[3] + i + 1) % line[1])

aocd_submit(crt(*mr, check=True)[0])
