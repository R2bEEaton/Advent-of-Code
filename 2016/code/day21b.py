from helpers.datagetter import aocd_data_in
import re
from collections import deque

din, aocd_submit = aocd_data_in(split=True, numbers=False)

text = deque([x for x in "fbgdceah"])
seen = set()
last = None


def swap_pos(text, x, y):
    temp = text[x]
    text[x] = text[y]
    text[y] = temp


while "".join(text) not in seen:
    seen.add("".join(text))
    last = "".join(text)

    for line in din:
        if line.startswith("swap position"):
            x, y = [int(x) for x in re.findall(r'(\d+)', line)]
            swap_pos(text, x, y)

        if line.startswith("swap letter"):
            x, y = re.findall(r'letter ([^\s]+)', line)
            idx = text.index(x)
            idy = text.index(y)
            swap_pos(text, idx, idy)


        if line.startswith("rotate"):
            if line.startswith("rotate b"):
                x = line.split()[-1]
                idx = text.index(x)
                text.rotate(1 + idx + (1 if idx >= 4 else 0))
            elif line.startswith("rotate r"):
                text.rotate(int(line.split()[2]))
            else:
                text.rotate(-int(line.split()[2]))

        if line.startswith("reverse position"):
            x, y = [int(x) for x in re.findall(r'(\d+)', line)]
            for i in range(0, (y-x+1) // 2):
                swap_pos(text, x+i, y-i)

        if line.startswith("move position"):
            x, y = [int(x) for x in re.findall(r'(\d+)', line)]
            temp = text[x]
            del text[x]
            text.insert(y, temp)

aocd_submit(last)