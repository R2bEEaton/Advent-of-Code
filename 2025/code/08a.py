from collections import defaultdict
from helpers.datagetter import aocd_data_in
import math
import itertools
import functools

din, aocd_submit = aocd_data_in(split=True, numbers=True)

# Spent a while on this line for some reason
closest = sorted(itertools.combinations(range(len(din)), r=2), key=functools.cmp_to_key(lambda x, y: math.dist(din[x[0]], din[x[1]]) - math.dist(din[y[0]], din[y[1]])))

circuits = []

# Had some ugly code for this that I scrapped, using a seen dictionary to keep track of which points were in each circuit for O(1) lookups but I scrapped it.
# Unfortunately, my code was RIGHT and I was getting it wrong because I was multiplying the length of every circuit instead of just the top three!!!
# After recoding it much better this way and getting the same answer, I re-read the question and realized the issue with the top three.
for x in range(1000):
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

clen = sorted(len(x) for x in circuits)

ans = clen[-1] * clen[-2] * clen[-3]

aocd_submit(ans)