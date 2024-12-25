from helpers.datagetter import aocd_data_in
import numpy as np

din, aocd_submit = aocd_data_in(split=True, numbers=False)

keys = []
locks = []

for i in range(0, len(din), 8):
    line = din[i:i+7]
    if line[0].count("#") == 5:
        line = [[x for x in y] for y in line]
        line = np.transpose(line)
        lock_heights = [np.count_nonzero(x == "#") - 1 for x in line]
        locks.append(lock_heights)
    else:
        line = [[x for x in y] for y in reversed(line)]
        line = np.transpose(line)
        key_heights = [np.count_nonzero(x == "#") - 1 for x in line]
        keys.append(key_heights)

ans = 0
for key in keys:
    for lock in locks:
        if np.max(np.add(key, lock)) <= 5:
            ans += 1

aocd_submit(ans)