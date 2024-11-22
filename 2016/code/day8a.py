from helpers.datagetter import aocd_data_in
from helpers.matrix import Matrix
import re

din, aocd_submit = aocd_data_in(split=True, numbers=False)

screen = Matrix((6, 50), 0, wrap=True)

for line in din:
    nums = [int(x) for x in re.findall(r'\d+', line)]
    print(nums)
    if "rect" in line:
        for x in range(nums[0]):
            for y in range(nums[1]):
                screen.set((y, x), 1)
    elif "row" in line:
        new_row = Matrix((1, screen.size[1]), 0, wrap=True)
        for x in range(screen.size[1]):
            new_row.set((0, x), screen.get((nums[0], x - nums[1])))
        for x in range(screen.size[1]):
            screen.set((nums[0], x), new_row.get((0, x)))
    elif "column" in line:
        new_col = Matrix((screen.size[0], 1), 0, wrap=True)
        for y in range(screen.size[0]):
            new_col.set((y, 0), screen.get((y - nums[1], nums[0])))
        for y in range(screen.size[0]):
            screen.set((y, nums[0]), new_col.get((y, 0)))

ans = 0

for pos, val in screen:
    ans += val

aocd_submit(ans)