from helpers.datagetter import aocd_data_in
import numpy as np

din, aocd_submit = aocd_data_in(split=True, numbers=False)

ans = 0
pieces = []

for line in din:
    if ":" in line and not line.endswith(":"):
        x, y = map(int, line.split(":")[0].split("x"))
        required = map(int, line.split(": ")[1].split(" "))

        area = 0
        for i, count in enumerate(required):
            area += count * sum([sum(x) for x in pieces[i]])

        # Area's big enough for sure
        if x * y >= area:
            ans += 1
        
        continue
    
    if line.endswith(":"):
        new_piece = []
        continue
    elif line == "":
        pieces.append(new_piece)
        continue
    else:
        new_piece.append([0 if c == '.' else 1 for c in line])

aocd_submit(ans)