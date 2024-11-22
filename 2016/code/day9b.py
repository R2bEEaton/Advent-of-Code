from helpers.datagetter import aocd_data_in
import re

din, aocd_submit = aocd_data_in(split=False, numbers=False)

def expand(s):
    if "(" not in s:
        return len(s)

    tot = 0
    while True:
        try:
            marker = re.match(r'([^\(]*)(\(\d+x\d+\))', s).groups()
            s = s[sum(len(x) for x in marker):]
            dup = [int(x) for x in re.findall(r'\d+', marker[1])]
            tot += len(marker[0]) + expand(s[:dup[0]]) * dup[1]
            s = s[dup[0]:]
        except:
            break

    tot += len(s)
    return tot

aocd_submit(expand(din))