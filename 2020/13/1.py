data = []
with open("input.txt") as f:
    for line in f.readlines():
        data.append(line.strip())

buses = []
for id in data[1].split(","):
    if id != "x":
        buses.append(int(id))

start = int(data[0])
time = start
while True:
    for id in buses:
        if time % id == 0:
            print(id * (time-start))
            exit()
    time += 1