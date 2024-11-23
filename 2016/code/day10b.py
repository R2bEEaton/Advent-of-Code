from helpers.datagetter import aocd_data_in
from collections import defaultdict
import re

din, aocd_submit = aocd_data_in(split=True, numbers=False)

bots = defaultdict(list)
output = defaultdict(list)

for line in din:
    if line.startswith("value"):
        nums = re.findall(r'\d+', line)
        bots[nums[1]].append(int(nums[0]))

did_something = True
while did_something:
    did_something = False
    for line in din:
        if line.startswith("value"):
            continue
        nums = re.findall(r'.t \d+', line)
        instr = [x.split(" ") for x in nums]
        if len(bots[instr[0][1]]) != 2:
            continue
        did_something = True
        if instr[1][0][0] == "u":
            output[instr[1][1]].append(min(bots[instr[0][1]]))
        else:
            bots[instr[1][1]].append(min(bots[instr[0][1]]))
        if instr[2][0][0] == "u":
            output[instr[2][1]].append(max(bots[instr[0][1]]))
        else:
            bots[instr[2][1]].append(max(bots[instr[0][1]]))
        bots[instr[0][1]].clear()

aocd_submit(output['0'][0] * output['1'][0] * output['2'][0])
