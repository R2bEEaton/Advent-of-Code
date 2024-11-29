from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

tot = 0
for line in din:
    for x in line:
        for y in line:
            if x == y:
                continue
            if x % y == 0:
                tot += x / y

aocd_submit(tot)