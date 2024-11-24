from helpers.datagetter import aocd_data_in
from hashlib import md5
import functools
import re

din, aocd_submit = aocd_data_in(split=False, numbers=False)

keys = []

def check_next_1000(i, c):
    for j in range(i + 1, i + 1000):
        if c * 5 in hash(j):
            return True
    return False


@functools.cache
def hash(i):
    init = md5(bytes(din + str(i), encoding='UTF-8')).hexdigest()
    for _ in range(2016):
        init = md5(bytes(init, encoding='UTF-8')).hexdigest()
    return init


index = 0
while len(keys) != 64:
    matches = re.findall(r'(.)\1\1', hash(index))
    if matches:
        if check_next_1000(index, matches[0][0]):
            keys.append(index)
    index += 1

aocd_submit(keys[-1])
