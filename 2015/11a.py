inp = "cqjxjnds"
nums = [0]*8
for i in range(len(inp)):
    nums[i] = ord(inp[i]) - 97


def double(pwd):
    for i in range(len(pwd)-1):
        if pwd[i] == pwd[i+1]:
            return True
    return False


def good(pwd):
    found2 = True
    if 105 in pwd or 111 in pwd or 108 in pwd:
        found2 = False
        return False

    found1 = False
    for i in range(len(pwd)-2):
        if pwd[i] == pwd[i+1]-1 and pwd[i+1] == pwd[i+2]-1:
            found1 = True

    found3 = False
    for i in range(len(pwd)-1):
        if double(pwd[i:i+2]) and double(pwd[0:i] + ["X"] + pwd[i+2:len(pwd)]):
            found3 = True

    return all([found1, found2, found3])


while True:
    if nums == [25, 25, 25, 25, 25, 25, 25, 25]:
        nums = [0, 0, 0, 0, 0, 0, 0, 0]
    else:
        for i in range(len(nums)):
            if len(nums)-1-i == len(nums)-1:
                nums[len(nums)-1-i] += 1
            if nums[len(nums)-1-i] > 25:
                nums[len(nums)-1-i] = 0
                nums[len(nums)-2-i] += 1

    if good(nums):
        s = ""
        for thing in nums:
            s += chr(thing+97)
        print(s)
        exit()
