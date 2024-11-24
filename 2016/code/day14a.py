from helpers.datagetter import aocd_data_in
from hashlib import md5
import re

din, aocd_submit = aocd_data_in(split=False, numbers=False)

keys = []

def check_next_1000(i, c):
    for j in range(i + 1, i + 1000):
        if c * 5 in md5(bytes(din + str(j), encoding='UTF-8')).hexdigest():
            return True
    return False

index = 0
while len(keys) != 64:
    key = din + str(index)
    matches = re.findall(r'(.)\1\1', md5(bytes(key, encoding='UTF-8')).hexdigest())
    if matches:
        if check_next_1000(index, matches[0][0]):
            keys.append(index)
    index += 1

aocd_submit(keys[-1])
