from helpers.datagetter import aocd_data_in
import re

din, aocd_submit = aocd_data_in(split=False, numbers=False)
ans = 0

for mul in re.findall(r'mul\(\d{1,3},\d{1,3}\)', din):
    ans += int(re.findall(r'(\d+)', mul)[0]) * int(re.findall(r'(\d+)', mul)[1])

aocd_submit(ans)