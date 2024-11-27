from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)
din = [[int(x) for x in y.split('-')] for y in din]

possible = []


def good(i):
    for vals in din:
        x, y = vals
        if x <= i <= y:
            return False
    return True


for vals in din:
    if good(vals[1] + 1):
        possible.append(vals[1] + 1)

aocd_submit(min(possible))