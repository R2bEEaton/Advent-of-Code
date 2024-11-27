from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)
din = [[int(x) for x in y.split('-')] for y in din]

possible = []


def good(i):
    for vals in din:
        x, y = vals
        if x <= i <= y:
            return False
    return True if i < 2**32 else False # Needed to add this check, which originally called len(possible) to be +1


for vals in din:
    if good(vals[1] + 1):
        possible.append(vals[1] + 1)

total = 0
for val in possible:
    i = val
    while good(i):
        i += 1
        total += 1

aocd_submit(total) # Seems to be same as len(possible) !?