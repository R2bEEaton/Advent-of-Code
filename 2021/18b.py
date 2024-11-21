import math
hw = []

with open("input18.txt") as f:
    for line in f.readlines():
        line = line.strip()
        hw.append(line)


def explode(line):
    deep = 0
    index = -1
    nums = []
    expl = []
    i = 0
    while i < len(line):
        char = line[i]
        if char == "[":
            deep += 1
        elif char == "]":
            deep -= 1
        if next_num(line[i:]) >= 0:
            if deep == 5 and len(expl) != 2:
                if index == -1:
                    index = i-1
                expl.append(len(nums))
            nums.append(next_num(line[i:]))
            i += len(str(next_num(line[i:])))-1
        i += 1

    old_nums = nums.copy()
    o = 0
    if expl[0] > 0:
        n = 0
        i = 0
        while i < len(line):
            if next_num(line[i:]) >= 0:
                if n == expl[0]-1:
                    nums[n] += nums[expl[0]]
                    o = len(str(nums[n]))-len(str(old_nums[n]))
                    break
                n += 1
                i += len(str(next_num(line[i:])))-1
            i += 1

    if expl[1] + 1 <= len(nums):
        n = 0
        i = 0
        while i < len(line):
            if next_num(line[i:]) >= 0:
                if n == expl[1] + 1:
                    nums[n] += nums[expl[1]]
                    break
                n += 1
                i += len(str(next_num(line[i:]))) - 1
            i += 1

    n = 0
    i = 0
    out = ""
    while i < len(line):
        if next_num(line[i:]) >= 0:
            if int(next_num(line[i:])) == old_nums[n]:
                out += str(nums[n])
            n += 1
            i += len(str(next_num(line[i:]))) - 1
        else:
            out += line[i]
        i += 1

    out = out[:index+o] + "0" + out[index+len(str(nums[expl[0]]))+len(str(nums[expl[1]]))+3+o:]
    return out


def split(line):
    nums = []
    out = ""
    i = 0
    found = False
    while i < len(line):
        if next_num(line[i:]) > 9 and not found:
            out += "[" + str(math.floor(int(line[i] + line[i+1]) / 2)) + "," + str(math.ceil(int(line[i] + line[i+1]) / 2)) + "]"
            i += len(str(next_num(line[i:]))) - 1
            found = True
        else:
            out += line[i]
        i += 1
    if not found:
        raise EOFError
    return out


def next_num(line):
    out = ""
    for char in line:
        if char.isnumeric():
            out += char
        else:
            break
    if out != "":
        return int(out)
    else:
        return -1


def reduce(thing):
    found = False
    while not found:
        oldthing = thing
        done = False
        try:
            thing = explode(thing)
            done = True
        except:
            None
        if not done:
            try:
                thing = split(thing)
                done = True
            except:
                None
        if not done:
            found = True
    return thing


def magnitude(things):
    if type(things) == int:
        return things
    return 3*magnitude(things[0]) + 2*magnitude(things[1])


mags = []
t = 0
for i in range(len(hw)):
    for j in range(len(hw)):
        if i != j:
            t += 1
            answer = reduce("[" + hw[i] + "," + hw[j] + "]")
            answer = magnitude(eval(answer))
            try:
                if answer > max(mags):
                    print(answer)
            except:
                None
            if t % 100 == 0:
                print("Iterations:", t)
            mags.append(answer)


print(max(mags))
print(t)
