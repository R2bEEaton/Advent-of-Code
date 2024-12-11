from itertools import product

pos = (0, 0, 0)
diag = True

deltas = product([-1, 0, 1], repeat=2)
for delta in deltas:
    if not diag and sum(abs(d) for d in delta) != 1:
        continue
    if diag and all(d == 0 for d in delta):
        continue

    neighbor_pos = tuple(p + d for p, d in zip(pos, delta))
    print(neighbor_pos)
