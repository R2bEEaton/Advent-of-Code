nums = []
desc = []

with open("input17.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        if float(line) in nums:
            line = float(line) + (1/2**i)
        nums.append(float(line))

nums.sort()
nums.reverse()
different = []


def ways(l, cur, goal, index):
    global nums
    global different
    for i in range(index+1, len(nums)):
        if cur + round(nums[i]) < goal:
            ways(l + [nums[i]], cur + round(nums[i]), goal, i)
        elif cur + round(nums[i]) == goal:
            different.append(l + [nums[i]])


for i in range(len(nums)):
    ways([nums[i]], round(nums[i]), 150, i)

t = 0
lens = min(list(map(len, different)))
for thing in different:
    if len(thing) == lens:
        t += 1
print(t)
