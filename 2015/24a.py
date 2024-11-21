nums = []
desc = []

with open("input24.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        nums.append(int(line))

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
    ways([nums[i]], round(nums[i]), sum(nums)/3, i)

s = min(list(map(len, different)))
ts = []
for thing in different:
    if len(thing) == s:
        t = 1
        for i in thing:
            t *= i
        ts.append(t)

print(min(ts))
