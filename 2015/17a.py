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
t = 0


def ways(l, cur, goal, index):
    global nums
    global t
    for i in range(index+1, len(nums)):
        if cur + round(nums[i]) < goal:
            ways(l + [nums[i]], cur + round(nums[i]), goal, i)
        elif cur + round(nums[i]) == goal:
            t += 1


for i in range(len(nums)):
    ways([nums[i]], round(nums[i]), 150, i)

print(t)
