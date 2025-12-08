from collections import defaultdict
from helpers.datagetter import aocd_data_in
import math
import itertools
import functools

din, aocd_submit = aocd_data_in(split=True, numbers=True)

closest = sorted(itertools.combinations(range(len(din)), r=2), key=functools.cmp_to_key(lambda x, y: math.dist(din[x[0]], din[x[1]]) - math.dist(din[y[0]], din[y[1]])))

circuits = []

x = 0

# Decently straightforward update.
while x == 0 or len(circuits[0]) != len(din):
    a, b = closest[x]

    ac = None
    bc = None

    for i, c in enumerate(circuits):
        if a in c:
            ac = i
        if b in c:
            bc = i

    if ac is not None and bc is not None:
        if ac != bc:
            circuits[ac].update(circuits[bc])
            del circuits[bc]
    elif ac is not None:
        circuits[ac].add(b)
    elif bc is not None:
        circuits[bc].add(a)
    else:
        circuits.append(set([a, b]))
    
    x += 1

ans = din[a][0] * din[b][0]

aocd_submit(ans)