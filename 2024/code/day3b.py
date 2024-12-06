from helpers.datagetter import aocd_data_in
import re

din, aocd_submit = aocd_data_in(split=False, numbers=False)
din += "don't()"
ans = 0

i = 0
while i < len(din) and i != -1:
    for mul in re.findall(r'mul\(\d{1,3},\d{1,3}\)', din[i:din.find("don't()", i)]):
        ans += int(re.findall(r'(\d+)', mul)[0]) * int(re.findall(r'(\d+)', mul)[1])
    i = din.find("do()", din.find("don't()", i))

aocd_submit(ans)