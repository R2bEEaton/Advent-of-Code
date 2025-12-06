from helpers.datagetter import aocd_data_in
from math import prod

din, aocd_submit = aocd_data_in(split=True, numbers=False)

ans = 0

curr_nums = []
for x in range(len(din[0]) - 1, -1, -1):
    new_num = ""
    for y in range(len(din)):
        if din[y][x] == "*":
            ans += prod(curr_nums) * int(new_num)
        if din[y][x] == "+":
            ans += sum(curr_nums) + int(new_num)
        new_num += din[y][x]
    
    try:
        curr_nums.append(int(new_num))
    except:
        curr_nums.clear()

aocd_submit(ans)