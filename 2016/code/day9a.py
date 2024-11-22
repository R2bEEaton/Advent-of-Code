from helpers.datagetter import aocd_data_in
import re

din, aocd_submit = aocd_data_in(split=False, numbers=False)

out = ""
duplicate = [1, 1]
marker = False

i = 0
while i < len(din):
    if din[i] == "(" and not marker:
        grouping = re.search(r'\(\d+x\d+\)', din[i:]).group()
        duplicate = [int(x) for x in re.findall(r'\d+', grouping)]
        i += len(grouping)
        marker = True
    else:
        out += "".join(din[i:i+duplicate[0]] * duplicate[1])
        i += duplicate[0]
        duplicate = [1, 1]
        marker = False

aocd_submit(len(out))
