data = []
with open("input.txt") as f:
    running = []
    for line in f.readlines():
        line = line.strip()
        if line != "":
            running.append(line)
        else:
            data.append(running)
            running = []
    data.append(running)

print(data)

count = 0

for group in data:
    alr_ans = {}
    for person in group:
        for answer in person:
            try:
                alr_ans[answer] += 1
            except:
                alr_ans[answer] = 1

    good = 0
    for key in alr_ans:
        if alr_ans[key] == len(group):
            good += 1
    count += good

print(count)
