from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

discs = []

for line in din:
    discs.append([line[1], line[3]])


def isgood(discs):
    for i, disc in enumerate(discs):
        if (disc[1] + i) % disc[0] != 0:
            return False
    return True
    

time = -1
while not isgood(discs):
    for disc in discs:
        disc[1] = (disc[1] + 1) % disc[0]
    time += 1

aocd_submit(time)