data = []
with open("input.txt") as f:
    running = ""
    for line in f.readlines():
        line = line.strip()
        if line != "":
            running += line
        else:
            data.append(running)
            running = ""
    data.append(running)

count = 0

for group in data:
    alr_ans = []
    for answer in group:
        if answer not in alr_ans:
            alr_ans.append(answer)
            count += 1

print(count)
